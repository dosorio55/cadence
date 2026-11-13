import assert from 'node:assert/strict'
import test from 'node:test'
import { once } from 'node:events'
import { fileURLToPath } from 'node:url'
import { ChordWorker } from '../src/main/chord-worker.ts'

const fixture = new URL('./fixtures/chord-worker.mjs', import.meta.url)

function createWorker(options = {}) {
  return new ChordWorker({
    executable: process.execPath,
    args: [fileURLToPath(fixture)],
    startupTimeoutMs: 5000,
    analysisTimeoutMs: 1000,
    ...options
  })
}

test('worker handles fragmented readiness, reuses the process and survives file errors', async () => {
  const worker = createWorker()

  try {
    const first = worker.analyze('/audio.wav')
    await assert.rejects(worker.analyze('/other.wav'), /curso/)
    assert.deepEqual(await first, [{ start_time: 0, end_time: 2.5, chord: 'C:maj' }])
    const child = worker.child
    await assert.rejects(worker.analyze('error'), /Audio inválido/)
    await worker.analyze('/second.wav')
    assert.equal(worker.child, child)

    const closed = once(child, 'close')
    worker.dispose()
    await closed
    await assert.rejects(worker.analyze('/audio.wav'), /cerrado/)
  } finally {
    worker.dispose()
  }
})

test('worker rejects malformed results and exits without leaving a process running', async () => {
  for (const path of ['malformed', 'invalid', 'crash']) {
    const worker = createWorker()

    try {
      await assert.rejects(worker.analyze(path))

      if (worker.child) await once(worker.child, 'close')
      assert.equal(worker.child, undefined)
    } finally {
      worker.dispose()
    }
  }
})

test('analysis deadline terminates the worker and allows a fresh process', async () => {
  const worker = createWorker({ analysisTimeoutMs: 100 })

  try {
    await assert.rejects(worker.analyze('timeout'), /tiempo máximo/)
    if (worker.child) await once(worker.child, 'close')
    assert.equal((await worker.analyze('/audio.wav'))[0].chord, 'C:maj')
  } finally {
    worker.dispose()
  }
})

test('startup failure and startup deadline reject without hanging', async () => {
  const missing = createWorker({ executable: '/cadence-missing-python' })
  const stalled = createWorker({
    args: ['-e', 'setInterval(() => {}, 1000)'],
    startupTimeoutMs: 100
  })

  try {
    await assert.rejects(missing.analyze('/audio.wav'), /No se pudo iniciar/)
    await assert.rejects(stalled.analyze('/audio.wav'), /iniciar/)
  } finally {
    missing.dispose()
    stalled.dispose()
  }
})
