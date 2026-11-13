import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


WORKER = Path(__file__).resolve().parents[2] / "python" / "worker.py"
spec = importlib.util.spec_from_file_location("chord_worker", WORKER)
worker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(worker)


class FakeSession:
    def __init__(self):
        self.loads = 0
        self.paths = []
        self.closed = False

    def load(self):
        self.loads += 1
        print("loading ensemble")

    def infer(self, path):
        self.paths.append(path)
        print("running inference")
        return [{"start_time": 0.0, "end_time": 1.25, "chord": "C:maj"}]

    def close(self):
        self.closed = True
        print("closing ensemble")


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.audio = Path(self.temp.name) / "song.wav"
        self.audio.touch()
        self.session = FakeSession()

    def run_worker(self, requests, factory=None):
        source = "".join(json.dumps(request) + "\n" for request in requests)
        output = io.StringIO()
        logs = io.StringIO()
        with contextlib.redirect_stderr(logs):
            status = worker.run(io.StringIO(source), output, factory or (lambda: self.session))
        return status, [json.loads(line) for line in output.getvalue().splitlines()], logs.getvalue()

    def test_reuses_one_default_session_and_closes_at_eof(self):
        calls = []

        def factory():
            calls.append(1)
            return self.session

        status, messages, logs = self.run_worker(
            [{"id": number, "path": str(self.audio)} for number in (1, 2)], factory
        )
        self.assertEqual(status, 0)
        self.assertEqual(calls, [1])
        self.assertEqual(self.session.loads, 1)
        self.assertEqual(self.session.paths, [str(self.audio)] * 2)
        self.assertTrue(self.session.closed)
        self.assertEqual(messages, [
            {"type": "ready"},
            {"id": 1, "chords": [{"start_time": 0.0, "end_time": 1.25, "chord": "C:maj"}]},
            {"id": 2, "chords": [{"start_time": 0.0, "end_time": 1.25, "chord": "C:maj"}]},
        ])
        self.assertIn("loading ensemble", logs)
        self.assertEqual(logs.count("running inference"), 2)
        self.assertIn("closing ensemble", logs)

    def test_rejects_nonlocal_or_nonfile_paths_before_inference(self):
        paths = ["https://example.com/audio.wav", "file:///tmp/audio.wav", "relative.wav",
                 str(self.audio.parent), str(self.audio.parent / "missing.wav"), "\x00", "", None, 5]
        status, messages, _ = self.run_worker([
            {"id": number, "path": path} for number, path in enumerate(paths, 1)
        ])
        self.assertEqual(status, 0)
        self.assertEqual(self.session.paths, [])
        self.assertEqual([message["id"] for message in messages[1:]], list(range(1, len(paths) + 1)))
        self.assertTrue(all(message["error"] for message in messages[1:]))

    def test_invalid_requests_are_errors_and_do_not_end_session(self):
        invalid = [None, [], "text", {}, {"id": True, "path": str(self.audio)},
                   {"id": 0, "path": str(self.audio)}, {"id": -1, "path": str(self.audio)},
                   {"id": 1.5, "path": str(self.audio)}, {"id": "1", "path": str(self.audio)},
                   {"id": 3}, {"id": 4, "path": str(self.audio), "method": "close"}]
        status, messages, _ = self.run_worker(invalid + [{"id": 5, "path": str(self.audio)}])
        self.assertEqual(status, 0)
        self.assertTrue(all("error" in message for message in messages[1:-1]))
        self.assertEqual(messages[1]["id"], None)
        self.assertEqual(messages[-3]["id"], 3)
        self.assertEqual(messages[-2]["id"], 4)
        self.assertEqual(messages[-1]["id"], 5)
        self.assertEqual(self.session.paths, [str(self.audio)])

    def test_bad_json_inference_and_serialization_errors_recover(self):
        outcomes = [RuntimeError("bad decoder"), [{"start_time": float("nan")}], []]

        def infer(path):
            result = outcomes.pop(0)
            if isinstance(result, Exception):
                raise result
            return result

        self.session.infer = infer
        output = io.StringIO()
        source = "not json\n" + "".join(
            json.dumps({"id": number, "path": str(self.audio)}) + "\n" for number in (1, 2, 3)
        )
        with contextlib.redirect_stderr(io.StringIO()):
            status = worker.run(io.StringIO(source), output, lambda: self.session)
        messages = [json.loads(line) for line in output.getvalue().splitlines()]
        self.assertEqual(status, 0)
        self.assertIsNone(messages[1]["id"])
        self.assertIn("error", messages[1])
        self.assertEqual(messages[2], {"id": 1, "error": "bad decoder"})
        self.assertIn("error", messages[3])
        self.assertEqual(messages[4], {"id": 3, "chords": []})
        self.assertTrue(self.session.closed)

    def test_startup_failure_is_fatal_and_partial_session_is_closed(self):
        def fail():
            print("failed load log")
            raise RuntimeError("missing weights")

        self.session.load = fail
        status, messages, logs = self.run_worker([])
        self.assertEqual(status, 1)
        self.assertEqual(messages, [{"type": "fatal", "error": "missing weights"}])
        self.assertIn("failed load log", logs)
        self.assertTrue(self.session.closed)

        status, messages, _ = self.run_worker([], fail)
        self.assertEqual(status, 1)
        self.assertEqual(messages, [{"type": "fatal", "error": "missing weights"}])

    def test_empty_eof_and_cleanup_failure_do_not_pollute_protocol(self):
        def fail_close():
            raise RuntimeError("cleanup failed")

        self.session.close = fail_close
        status, messages, logs = self.run_worker([])
        self.assertEqual(status, 0)
        self.assertEqual(messages, [{"type": "ready"}])
        self.assertIn("session cleanup failed: cleanup failed", logs)

    def test_entrypoint_isolates_import_python_and_native_stdout(self):
        module = Path(self.temp.name) / "lv_chordia.py"
        module.write_text(
            'import os\n'
            'print("import log", flush=True)\n'
            'os.write(1, b"native import log\\n")\n'
            'class LVChordiaSession:\n'
            '    def __init__(self): pass\n'
            '    def load(self): print("load log", flush=True)\n'
            '    def infer(self, path):\n'
            '        os.write(1, b"native inference log\\n")\n'
            '        print("inference log", flush=True)\n'
            '        return []\n'
            '    def close(self): print("close log", flush=True)\n',
            encoding="utf-8",
        )
        process = subprocess.Popen(
            [sys.executable, "-u", str(WORKER)],
            env={**os.environ, "PYTHONPATH": self.temp.name},
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True,
        )
        try:
            # Reading before EOF also checks that ready and each response are flushed.
            self.assertEqual(json.loads(process.stdout.readline()), {"type": "ready"})
            for number in (1, 2):
                process.stdin.write(json.dumps({"id": number, "path": str(self.audio)}) + "\n")
                process.stdin.flush()
                self.assertEqual(json.loads(process.stdout.readline()), {"id": number, "chords": []})
            process.stdin.close()
            process.wait(timeout=10)
            self.assertEqual(process.returncode, 0)
            self.assertEqual(process.stdout.read(), "")
            logs = process.stderr.read()
            for message in ("import log", "native import log", "load log", "native inference log",
                            "inference log", "close log"):
                self.assertIn(message, logs)
            self.assertEqual(logs.count("load log"), 1)
        finally:
            if process.poll() is None:
                process.kill()
                process.wait()
            for stream in (process.stdin, process.stdout, process.stderr):
                stream.close()


if __name__ == "__main__":
    unittest.main()
