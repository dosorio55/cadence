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

`pnpm build:unpack`, `pnpm build:linux`, `pnpm build:win` and `pnpm build:mac` produce desktop packages on supported build hosts. Signing, notarization and publishing are not configured for release.

## Application boundaries

- `src/renderer/src/app/`: curriculum library and lesson workspace. Hash routes work with packaged `file:` URLs, including stage/example links and reloads.
- `src/renderer/src/components/ui/`: the existing official shadcn Base UI primitives. Semantic Studio theme tokens live in `src/renderer/src/app/globals.css`. Fonts are packaged locally; no Google Fonts request is needed.
- `src/main/curriculum*.ts`: read-only approved JSON loaders, bundled into the main process. Only library metadata or the requested lesson crosses the typed preload bridge (`src/shared/api.ts`). The renderer has no filesystem, SQL or generic IPC API.
- `lesson-content/`: complete source delivery, including approved JSON, JSON Schemas, drafts, archives, tools, audit evidence, MIDI and the reference SQLite artifact. Copied without changing file bytes; Python environments/caches are not copied. See its README for authoring/validation commands. Historical audit paths and wording are preserved.

All 90 lessons, 400 stages and 402 progressions are available. Audio, piano-roll/keyboard rendering, MIDI input and saved self-assessment were not implemented in the source app and remain placeholders/session-only. Theme preference remains local to the desktop app; existing browser theme settings are not imported.

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

Run `pnpm dev`: open a lesson, switch stages and alternative examples, reload a stage URL, toggle both sidebars and switch light/dark themes. These visual checks and installer/platform checks are separate from the automated data, SQLite, IPC and theme tests.
