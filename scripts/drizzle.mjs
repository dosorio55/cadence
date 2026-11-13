import { spawnSync } from 'node:child_process'
import { createRequire } from 'node:module'
import { dirname, join } from 'node:path'
import electron from 'electron'

const require = createRequire(import.meta.url)
const result = spawnSync(
  electron,
  [join(dirname(require.resolve('drizzle-kit')), 'bin.cjs'), ...process.argv.slice(2)],
  {
    stdio: 'inherit',
    env: { ...process.env, ELECTRON_RUN_AS_NODE: '1' }
  }
)

if (result.error) throw result.error
process.exit(result.status ?? 1)
