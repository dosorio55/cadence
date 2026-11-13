# Chord worker

Requires Python 3.11+ and builds on each target OS/architecture (no cross-compilation).
From `apps/cadence-electron/python`:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[build]'
.venv/bin/python build.py
```

On Windows use `py -3 -m venv .venv`, then `.venv\Scripts\python.exe` instead of
`.venv/bin/python`. Build output is `dist/chord-worker/chord-worker` (`.exe` on
Windows). Copy the **whole directory**, including `_internal`, to Electron's
`resources/chord-worker`; no Python installation is needed at runtime.

The Git dependency is pinned to `d8ab9ac99bce081bb79065d717f96e2c3b2099c8` in
`https://github.com/openmirlab/lv-chordia.git` (confirmed reachable). Pip may download
large Torch/CUDA dependencies. For an intentionally CPU-only build, install a
compatible `torch>=2.13.0` CPU wheel from the official PyTorch CPU index **before**
installing this project. Default `LVChordiaSession()` device selection is unchanged;
GPU-capable builds need a suitable Torch distribution and host driver.

For a local editable source override, replace the dependency-install command above
with these commands (verify the sibling checkout is at the pinned revision first):

```sh
git -C ../../lv-chordia rev-parse HEAD
.venv/bin/python -m pip install -e ../../lv-chordia 'pyinstaller>=6.16,<7'
.venv/bin/python -m pip install --no-deps -e .
```

This installs the existing library, never edits it. Its weights must already exist;
the build verifies every checkpoint against `checkpoints.toml` and never downloads
weights. Installed shared data comes from `<sys.prefix>/share/lv-chordia/weights`;
editable installs fall back to the source checkout's `weights`. The spec bundles
weights at `share/lv-chordia/weights`, package data (including `checkpoints.toml` and
chord dictionaries), and runtime dependencies. A frozen-only runtime hook makes
`sys.prefix` point to PyInstaller's content directory so the unmodified library's
shared-data resolver finds those weights.

## Protocol and checks

Run `.venv/bin/python -u worker.py`. Startup emits `{"type":"ready"}` after one
successful load, or `{"type":"fatal","error":"..."}` and exit 1. Each input line
must contain exactly `{"id":1,"path":"/absolute/local/audio.wav"}`. Valid positive
integer IDs are echoed in `{"id":1,"chords":[...]}` or `{"id":1,"error":"..."}`.
Malformed input without a valid ID receives `{"id":null,"error":"..."}`. URLs,
relative paths and non-files are rejected; unsupported/corrupt audio produces a
request error. The worker does not sniff formats or duplicate UI size restrictions.
Errors do not end the session; stdin EOF closes it. All library stdout, including
native descriptor-1 writes, goes to stderr. Protocol lines are always flushed.

From `apps/cadence-electron`, run the dependency-free fake-session tests:

```sh
python3 -m unittest discover -s tests/python -v
```

Real inference smoke (absolute fixture path shown for this checkout; substitute your
own audio):

```sh
printf '%s\n' '{"id":1,"path":"/home/alejandro/Projects/Development/Personal/music/piano-lab/apps/lv-chordia/tests/fixtures/yellow.wav"}' | .venv/bin/python -u worker.py
printf '%s\n' '{"id":1,"path":"/home/alejandro/Projects/Development/Personal/music/piano-lab/apps/lv-chordia/tests/fixtures/yellow.wav"}' | dist/chord-worker/chord-worker
```

Both should emit ready, then chords, and exit on EOF; model diagnostics belong only
to stderr. These real-inference/frozen checks require the installed dependencies;
the implementation environment had Python 3.14 but no Torch, librosa or PyInstaller,
so no large dependency download or real inference/build was attempted.
