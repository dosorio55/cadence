import { createInterface } from 'node:readline'

process.stdout.write('{"type":')
setTimeout(() => process.stdout.write('"ready"}\n'), 5)

createInterface({ input: process.stdin }).on('line', (line) => {
  const request = JSON.parse(line)

  if (request.path === 'crash') process.exit(1)
  if (request.path === 'timeout') return

  if (request.path === 'malformed') {
    process.stdout.write('not json\n')
    return
  }

  const message =
    request.path === 'error'
      ? { id: request.id, error: 'Audio inválido' }
      : {
          id: request.id,
          chords: [
            { start_time: request.path === 'invalid' ? -1 : 0, end_time: 2.5, chord: 'C:maj' }
          ]
        }

  process.stdout.write(`${JSON.stringify(message)}\n`)
})
