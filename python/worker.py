"""Persistent JSON-lines adapter; stdout belongs exclusively to the protocol."""

import contextlib
import json
import os
from pathlib import Path
import sys


def load_session():
    from lv_chordia import LVChordiaSession

    return LVChordiaSession()


def send(output, message):
    output.write(json.dumps(message, allow_nan=False) + "\n")
    output.flush()


def validate_request(request):
    if not isinstance(request, dict):
        raise ValueError("request must be an object")

    request_id = request.get("id")
    if type(request_id) is not int or request_id <= 0:
        raise ValueError("id must be a positive integer")

    if set(request) != {"id", "path"}:
        raise ValueError("request must contain only id and path")

    path = request["path"]
    if not isinstance(path, str) or not path or "://" in path or "\x00" in path:
        raise ValueError("path must be an absolute local audio file")

    audio = Path(path)
    if not audio.is_absolute() or not audio.is_file():
        raise ValueError("path must be an absolute existing local file")

    return path


def run(input_stream, output, session_factory=load_session):
    session = None
    try:
        try:
            with contextlib.redirect_stdout(sys.stderr):
                session = session_factory()
                session.load()
        except Exception as error:
            send(output, {"type": "fatal", "error": str(error) or type(error).__name__})
            return 1

        send(output, {"type": "ready"})
        for line in input_stream:
            request_id = None
            try:
                request = json.loads(line)
                if isinstance(request, dict):
                    candidate = request.get("id")
                    if type(candidate) is int and candidate > 0:
                        request_id = candidate

                path = validate_request(request)
                with contextlib.redirect_stdout(sys.stderr):
                    chords = session.infer(path)
                    # Serialize before writing so invalid library output cannot leave a partial line.
                    response = json.dumps({"id": request_id, "chords": chords}, allow_nan=False)
            except Exception as error:
                send(output, {"id": request_id, "error": str(error) or type(error).__name__})
            else:
                output.write(response + "\n")
                output.flush()

        return 0
    finally:
        if session is not None:
            try:
                with contextlib.redirect_stdout(sys.stderr):
                    session.close()
            except Exception as error:
                print(f"session cleanup failed: {error}", file=sys.stderr, flush=True)


def main():
    # A separate descriptor keeps native C/C++ writes to fd 1 off the protocol too.
    with os.fdopen(os.dup(sys.stdout.fileno()), "w", encoding="utf-8", buffering=1) as protocol:
        sys.stdout.flush()
        os.dup2(sys.stderr.fileno(), sys.stdout.fileno())
        if os.name == "nt":
            import ctypes
            import msvcrt

            stderr_handle = msvcrt.get_osfhandle(sys.stderr.fileno())
            if not ctypes.windll.kernel32.SetStdHandle(-11, ctypes.c_void_p(stderr_handle)):
                raise ctypes.WinError()

        sys.stdin.reconfigure(encoding="utf-8")
        return run(sys.stdin, protocol)


if __name__ == "__main__":
    raise SystemExit(main())
