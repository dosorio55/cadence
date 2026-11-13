import { spawnSync } from 'node:child_process'
import { accessSync, constants } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { join } from 'node:path'

const root = fileURLToPath(new URL('../', import.meta.url))
const executableName = process.platform === 'win32' ? 'chord-worker.exe' : 'chord-worker'
const executable = join(root, 'python', 'dist', 'chord-worker', executableName)
const targetPlatform = process.argv[3]

if (targetPlatform && targetPlatform !== process.platform) {
  console.error(`El motor Python debe construirse en el sistema de destino: ${targetPlatform}.`)
  process.exit(1)
}

if (process.argv[2] === 'build') {
  const python = join(
    root,
    'python',
    '.venv',
    process.platform === 'win32' ? 'Scripts/python.exe' : 'bin/python'
  )
  const result = spawnSync(python, [join(root, 'python', 'build.py')], {
    cwd: root,
    stdio: 'inherit',
    shell: false
  })

  if (result.error) {
    console.error(`No se pudo iniciar Python: ${result.error.message}. Consulta README.md.`)
    process.exit(1)
  }

  if (result.status !== 0) process.exit(result.status ?? 1)
}

try {
  accessSync(executable, process.platform === 'win32' ? constants.F_OK : constants.X_OK)
} catch {
  console.error(
    'Falta el motor Python empaquetado. Ejecuta pnpm chords:build antes de crear el instalador.'
  )
  process.exit(1)
}
