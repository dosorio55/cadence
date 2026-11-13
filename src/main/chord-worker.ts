import { spawn, type ChildProcessWithoutNullStreams } from 'node:child_process'
import type { ChordSegment } from '../shared/api'

interface WorkerOptions {
  executable: string
  args?: string[]
  startupTimeoutMs?: number
  analysisTimeoutMs?: number
}

interface PendingAnalysis {
  id: number
  resolve: (chords: ChordSegment[]) => void
  reject: (error: Error) => void
  timer: ReturnType<typeof setTimeout>
}

export class ChordWorker {
  private child?: ChildProcessWithoutNullStreams
  private starting?: Promise<void>
  private ready = false
  private busy = false
  private disposed = false
  private sequence = 0
  private pending?: PendingAnalysis
  private stopChild?: (error?: Error) => void
  private readonly options: WorkerOptions

  constructor(options: WorkerOptions) {
    this.options = options
  }

  async analyze(path: string): Promise<ChordSegment[]> {
    if (this.disposed) throw new Error('El motor de análisis está cerrado.')
    if (this.busy) throw new Error('Ya hay un análisis en curso.')

    this.busy = true

    try {
      await this.start()
      if (this.disposed) throw new Error('El motor de análisis está cerrado.')

      return await new Promise<ChordSegment[]>((resolve, reject) => {
        const id = ++this.sequence
        const timer = setTimeout(
          () => {
            this.stopChild?.(
              new Error('El análisis superó el tiempo máximo. Intenta con un audio más corto.')
            )
          },
          this.options.analysisTimeoutMs ?? 15 * 60_000
        )

        this.pending = { id, resolve, reject, timer }
        this.child!.stdin.write(`${JSON.stringify({ id, path })}\n`, (error) => {
          if (error) this.stopChild?.()
        })
      })
    } finally {
      this.busy = false
    }
  }

  dispose(): void {
    this.disposed = true
    this.stopChild?.()
  }

  private start(): Promise<void> {
    if (this.ready) return Promise.resolve()
    if (this.starting) return this.starting
    if (this.child) {
      return Promise.reject(new Error('El motor se está cerrando. Intenta nuevamente.'))
    }

    this.starting = new Promise<void>((resolve, reject) => {
      const child = spawn(this.options.executable, this.options.args ?? [], {
        shell: false,
        windowsHide: true,
        stdio: ['pipe', 'pipe', 'pipe']
      })
      this.child = child
      let buffer = ''
      let diagnostics = ''
      let stopped = false
      let killTimer: ReturnType<typeof setTimeout> | undefined

      const startupTimer = setTimeout(() => {
        fail(new Error('El motor de acordes tardó demasiado en iniciar.'))
      }, this.options.startupTimeoutMs ?? 120_000)

      const fail = (error: Error): void => {
        if (stopped) return

        stopped = true
        this.ready = false
        this.starting = undefined
        clearTimeout(startupTimer)
        reject(error)

        if (this.pending) {
          clearTimeout(this.pending.timer)
          this.pending.reject(error)
          this.pending = undefined
        }

        child.stdin.destroy()
        child.kill()
        killTimer = setTimeout(() => child.kill('SIGKILL'), 2000)
        killTimer.unref()
      }

      this.stopChild = (error) => fail(error ?? new Error('El motor de acordes se detuvo.'))

      child.stdout.setEncoding('utf8')
      child.stderr.setEncoding('utf8')
      child.stderr.on('data', (chunk: string) => {
        diagnostics = (diagnostics + chunk).slice(-4000)
      })
      child.stdin.on('error', (error) => fail(error))
      child.on('error', (error) => {
        fail(new Error(`No se pudo iniciar el motor de acordes: ${error.message}`))
      })
      child.on('close', () => {
        fail(new Error(`El motor de acordes se cerró inesperadamente. ${diagnostics.trim()}`))
        clearTimeout(killTimer)
        this.child = undefined
        this.starting = undefined
        this.stopChild = undefined
      })
      child.stdout.on('data', (chunk: string) => {
        if (stopped) return
        buffer += chunk

        if (buffer.length > 16 * 1024 * 1024) {
          fail(new Error('La respuesta del motor de acordes es demasiado grande.'))
          return
        }

        let boundary: number

        while ((boundary = buffer.indexOf('\n')) !== -1) {
          const line = buffer.slice(0, boundary)
          buffer = buffer.slice(boundary + 1)

          try {
            const message = JSON.parse(line)

            if (!this.ready) {
              if (message.type === 'fatal' && typeof message.error === 'string') {
                throw new Error(message.error)
              }

              if (message.type !== 'ready') throw new Error('El motor no confirmó su inicio.')

              this.ready = true
              clearTimeout(startupTimer)
              resolve()
              continue
            }

            const pending = this.pending
            if (!pending || message.id !== pending.id) {
              throw new Error('Respuesta inesperada del motor.')
            }

            if (typeof message.error === 'string') {
              clearTimeout(pending.timer)
              this.pending = undefined
              pending.reject(new Error(message.error))
              continue
            }

            assertChords(message.chords)
            clearTimeout(pending.timer)
            this.pending = undefined
            pending.resolve(message.chords)
          } catch (error) {
            fail(error instanceof Error ? error : new Error('Respuesta inválida del motor.'))
            return
          }
        }
      })
    })

    return this.starting
  }
}

function assertChords(value: unknown): asserts value is ChordSegment[] {
  if (!Array.isArray(value)) throw new Error('El motor devolvió acordes inválidos.')

  let previousEnd = 0

  for (const chord of value) {
    if (
      !chord ||
      typeof chord.chord !== 'string' ||
      chord.chord.length === 0 ||
      !Number.isFinite(chord.start_time) ||
      !Number.isFinite(chord.end_time) ||
      chord.start_time < previousEnd ||
      chord.end_time < chord.start_time
    ) {
      throw new Error('El motor devolvió acordes inválidos.')
    }

    previousEnd = chord.end_time
  }
}
