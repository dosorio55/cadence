# Cadence desktop

Offline Electron + React piano practice studio, migrated from `../cadence`. The original app is preserved; this app does not require it at runtime or build time.

## Run

From `apps/cadence-electron` with Node 24 and pnpm 11:

```sh
pnpm install
pnpm dev
pnpm test
pnpm typecheck
pnpm lint
pnpm build
pnpm start
```

`pnpm build:unpack`, `pnpm build:linux`, `pnpm build:win` and `pnpm build:mac` produce desktop packages after building the Python worker below. Build on the target OS and architecture; the platform scripts reject cross-OS packaging because the bundled Python executable is platform-specific. Signing, notarization and publishing are not configured for release.

## Application boundaries

- `src/renderer/src/app/`: curriculum library and lesson workspace. Hash routes work with packaged `file:` URLs, including stage/example links and reloads.
- `src/renderer/src/components/ui/`: the existing official shadcn Base UI primitives. Semantic Studio theme tokens live in `src/renderer/src/app/globals.css`. Fonts are packaged locally; no Google Fonts request is needed.
- `src/main/curriculum*.ts`: read-only approved JSON loaders, bundled into the main process. Only library metadata or the requested lesson crosses the typed preload bridge (`src/shared/api.ts`). The renderer has no filesystem, SQL or generic IPC API.
- `lesson-content/`: complete source delivery, including approved JSON, JSON Schemas, drafts, archives, tools, audit evidence, MIDI and the reference SQLite artifact. Copied without changing file bytes; Python environments/caches are not copied. See its README for authoring/validation commands. Historical audit paths and wording are preserved.

All 90 lessons, 400 stages and 402 progressions are available. Each selected stage now has piano playback, a synchronized falling-note roll and highlighted keyboard/chord cards. MIDI input remains unimplemented and self-assessment remains session-only. Theme preference remains local to the desktop app; existing browser theme settings are not imported.

## Lesson playback

Press **Reproducir** to hear the selected stage's actual note events through Tone.js and locally bundled Salamander Grand Piano samples. No MIDI-file parsing, external synthesizer or internet connection is required. Play/pause/stop, complete-example looping, tempo (40–180 quarter notes/minute), metronome toggle, separate click volume and a visual beat indicator share one audio clock. The metronome clicks the denominator's note value and accents the first pulse in each bar; for example, 6/8 has six eighth-note clicks while BPM stays in quarter notes.

Changing tempo stops and resets playback. Pause/resume rearticulates held notes for their remaining duration. Changing stages/examples, navigating away, hiding the app or an audio-context interruption silences the current run. Loops include trailing rests through the full notated duration, rather than ending at the last note-off. These controls do not grade the student's playing or save completion.

The 30 MP3 samples occupy approximately 2 MB and are copied unchanged from Tone.js's audio collection at revision `869b6f8d9cddb47d966238c012041480b1ce517a`. Original recordings: Alexander Holm, **CC BY 3.0**, not Tone.js's software license. Source notices, attribution and the full license ship under `src/renderer/public/audio/salamander/` and are copied to the production renderer. Credits are also visible below the player. This compact set pitch-shifts intermediate notes and scales velocity; it is not the original multi-velocity-layer library.

## Local chord recognition

The header's **Analizar acordes** link opens a separate recording-analysis screen. Select a local WAV, FLAC or OGG file (maximum 200 MB); Cadence returns estimated chord labels with start/end times in seconds. Results are session-only and do not modify approved lessons. This is whole-file recognition, not microphone streaming, note transcription, playback or performance grading. No recording is uploaded and no HTTP server is started.

The main process opens the native file dialog and starts one persistent Python worker on first use. Only `analyzeAudio()` crosses the sandboxed preload bridge; React cannot submit filesystem paths or arbitrary commands. Requests and replies use JSON lines over stdin/stdout; library diagnostics go to stderr. The supervisor validates responses, rejects concurrent analyses, stops a failed worker, and terminates it at application shutdown. Startup has a two-minute deadline; each analysis has a fifteen-minute deadline. A subsequent attempt can start a new worker after the previous one exits.

### Development setup

Requires Python 3.11+ in addition to Node/pnpm. From this directory on Linux/macOS:

```sh
python3 -m venv python/.venv
python/.venv/bin/python -m pip install -e './python[build]'
pnpm dev
```

On Windows use `py -3 -m venv python/.venv` and `python/.venv/Scripts/python.exe` for the install command. The library is installed from a pinned Git revision; `../lv-chordia` is neither moved nor modified and is not needed at application runtime. Model weights are included by that package. Installation requires internet; subsequent local analysis does not.

The default Torch installation can download several GB of CUDA libraries on Linux. The verified Linux CUDA build occupies approximately 5.1 GiB before installer compression; this is the runtime plus dependencies, not just the model weights. GPU/CPU auto-detection remains unchanged. See [`python/README.md`](python/README.md) for an intentionally CPU-only environment or a local editable-library install.

### Distribute without requiring users to install Python

```sh
pnpm chords:build
pnpm chords:check
pnpm build:unpack
```

`chords:build` uses PyInstaller to produce `python/dist/chord-worker/`, including the interpreter, dependencies and verified model weights. Electron Builder copies the whole directory outside ASAR into `resources/chord-worker/`. Installer commands fail early if the executable is missing; do not copy a development virtualenv into an installer. Build separately for every target OS/architecture and verify the resulting package there. GPU drivers, when using CUDA, remain a host requirement.

Focused protocol/lifecycle tests do not need model dependencies:

```sh
node --experimental-strip-types --test tests/chord-worker.test.mjs
python3 -m unittest discover -s tests/python -v
```

## SQLite and Drizzle

Drizzle uses `better-sqlite3` exclusively in the main process. Startup opens `cadence.sqlite` under Electron's `app.getPath('userData')`, with WAL and foreign keys enabled; shutdown closes it. No external server, PostgreSQL client, `DATABASE_URL` or `.env` is required.

The source Drizzle schema was empty, so `src/main/db/schema.ts` deliberately remains empty: there are no existing application tables or remote records to migrate. Curriculum stays immutable JSON; `lesson-content/examples/curriculum.sqlite` remains an untouched reference artifact, not the writable application database. This migration does not add saved progress.

```sh
pnpm db:generate
pnpm db:migrate
pnpm db:studio --host 127.0.0.1
```

Tooling defaults to a separate `cadence.dev.sqlite` in this directory. To target another local file, set `CADENCE_DB_PATH` to its absolute path. Quit the app before applying migrations to its database. With the empty schema, generation reports no schema changes. When application tables are added, generated migrations must also be packaged and applied during startup before using those tables; no migrations are needed yet.

The SQLite native module must target Electron's ABI, not the system Node ABI. `pnpm install` lets `electron-builder install-app-deps` build it; pnpm's generic native build is disabled for this package. Tests and Drizzle CLI run through Electron in Node mode to use that same binary. After changing Electron versions or a manual Node rebuild, reinstall dependencies/rebuild for Electron before running the app.

## Manual checks

Run `pnpm dev`: open a lesson and press **Reproducir**; verify piano sound, roll/key/chord alignment, pause/resume, full-example repeat and the metronome accent/volume. Change tempo and confirm playback resets; change stage/example or leave the page and confirm no notes remain sounding. Reload a stage URL, toggle both sidebars and switch light/dark themes. Also open **Analizar acordes**, cancel the picker, then analyze an audio file: chord times and estimates should appear, with errors shown for unreadable audio. Close the app after analysis and confirm no chord worker remains. These visual checks and installer/platform checks are separate from the automated data, SQLite, IPC, worker and theme tests.
