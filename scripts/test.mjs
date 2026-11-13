import { spawnSync } from 'node:child_process'
import { readdirSync } from 'node:fs'
import electron from 'electron'

const tests = readdirSync('tests').filter((file) => file.endsWith('.test.mjs'))
const result = spawnSync(
  electron,
  ['--experimental-strip-types', '--test', ...tests.map((file) => `tests/${file}`)],
  {
    stdio: 'inherit',
    env: { ...process.env, ELECTRON_RUN_AS_NODE: '1' }
  }
)

if (result.error) throw result.error
process.exit(result.status ?? 1)
