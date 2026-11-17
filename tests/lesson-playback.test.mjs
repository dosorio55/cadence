import assert from 'node:assert/strict'
import { readFileSync, statSync } from 'node:fs'
import test from 'node:test'
import { getLesson } from '../src/main/curriculum.ts'
import { LessonAudioEngine } from '../src/renderer/src/app/lessons/[lessonId]/components/player/audio-engine.ts'
import { pianoSampleFiles } from '../src/renderer/src/app/lessons/[lessonId]/components/player/piano-samples.ts'
import {
  getTiming,
  getMetronomeBeats,
  getPlaybackNotes,
  ticksPerBeat
} from '../src/renderer/src/app/lessons/[lessonId]/components/player/playback-plan.ts'

const progression = getLesson('lesson-rhythm-004').stages[1].progressions[0]

function audioHarness(load = async () => ({ C4: {} })) {
  const contexts = []
  const samplers = []
  const clicks = []

  class Context {
    time = 0
    state = 'running'
    transport = {
      bpm: { value: 120 },
      events: [],
      ticks: 0,
      schedule(callback, position) {
        this.events.push({ callback, position })
      },
      cancel() {
        this.events = []
      },
      start(time, offset) {
        this.startTime = time
        this.offset = offset
      },
      stop(time) {
        this.stopTime = time
      },
      getTicksAtTime() {
        return this.ticks
      }
    }
    constructor() {
      contexts.push(this)
    }
    immediate() {
      return this.time
    }
    now() {
      return this.time + 0.08
    }
    resume() {
      return Promise.resolve()
    }
    dispose() {
      this.disposed = true
    }
  }

  class Node {
    attacks = []
    volume = {
      setValueAtTime: (value) => {
        this.gain = value
      }
    }
    connect() {
      return this
    }
    toDestination() {
      return this
    }
    triggerAttackRelease(...args) {
      this.attacks.push(args)
    }
    disconnect() {
      this.disconnected = true
    }
    dispose() {
      this.disposed = true
    }
  }

  class Sampler extends Node {
    constructor() {
      super()
      samplers.push(this)
    }
  }
  class Synth extends Node {
    constructor() {
      super()
      clicks.push(this)
    }
  }

  const tone = { Context, Limiter: Node, Sampler, Synth }
  return {
    create: (example = progression) => new LessonAudioEngine(tone, example, load),
    contexts,
    samplers,
    clicks
  }
}

test('schedules the actual anticipation, velocity and meter on one clock, with full-bar loop bounds', async () => {
  const audio = audioHarness()
  const engine = audio.create()
  engine.setLoop(true)
  engine.setMetronome(true, 0.25)
  assert.equal(await engine.play(), true)
  const transport = audio.contexts[0].transport
  const noteEvents = transport.events.slice(0, progression.notes.length)
  assert.equal(transport.PPQ, 960)
  assert.equal(transport.bpm.value, progression.bpm)
  assert.equal(transport.loopEnd, '15360i')
  assert.equal(transport.loop, true)
  assert.ok(noteEvents.some((event) => event.position === `${11.5 * ticksPerBeat}i`))
  assert.ok(!noteEvents.some((event) => event.position === `${12 * ticksPerBeat}i`))

  noteEvents[0].callback(10)
  assert.deepEqual(audio.samplers[0].attacks[0], [
    440 * 2 ** ((progression.notes[0].midi - 69) / 12),
    (progression.notes[0].durationBeats * 60) / progression.bpm,
    10,
    progression.notes[0].velocity / 127
  ])
  const metronome = transport.events.slice(progression.notes.length)
  assert.equal(metronome.length, 16)
  metronome[0].callback(10)
  metronome[1].callback(11)
  assert.equal(audio.clicks[0].attacks[0][0], 1320)
  assert.equal(audio.clicks[0].attacks[1][0], 880)
  assert.equal(audio.clicks[0].attacks[0][3], 1)
  assert.equal(audio.clicks[0].attacks[1][3], 0.6)
  engine.setMetronome(false, 0.25)
  assert.equal(audio.clicks[0].gain, -Infinity)
  engine.setLoop(false)
  assert.equal(transport.loop, false)
  engine.dispose()
})

test('pause silences pending voices; resume restores only the remaining sustain; stop and tempo reset', async () => {
  const example = {
    ...progression,
    bpm: 120,
    notes: [
      { ...progression.notes[0], id: 'held', midi: 60, startBeat: 0, durationBeats: 4 },
      { ...progression.notes[0], id: 'next', midi: 60, startBeat: 4, durationBeats: 1 }
    ]
  }
  const audio = audioHarness()
  const engine = audio.create(example)
  await engine.play()
  const context = audio.contexts[0]
  const pendingCallback = context.transport.events[0].callback
  context.time = 2
  context.transport.ticks = 2.5 * ticksPerBeat
  engine.pause()
  assert.equal(engine.getBeat(), 2.5)
  assert.equal(audio.samplers[0].disconnected, true)
  assert.equal(audio.samplers[0].disposed, true)
  assert.equal(context.transport.events.length, 0)
  await engine.play()
  assert.equal(context.transport.offset, 1.25)
  assert.equal(audio.samplers[1].attacks.length, 1)
  assert.equal(audio.samplers[1].attacks[0][1], 0.75)
  pendingCallback(10)
  assert.equal(audio.samplers[1].attacks.length, 1)
  engine.setTempo(90)
  assert.equal(engine.getBeat(), 0)
  assert.equal(audio.samplers[1].disconnected, true)
  await engine.play()
  assert.equal(context.transport.bpm.value, 90)
  engine.stop(true)
  assert.equal(engine.getBeat(), 16)
  await engine.play()
  assert.equal(context.transport.offset, 0)
  engine.dispose()
  assert.equal(context.disposed, true)
})

test('a late sample load cannot start after navigation or Stop, and failed loads can be retried', async () => {
  let complete
  let signal
  const audio = audioHarness(async (_context, abortSignal) => {
    signal = abortSignal
    return new Promise((resolve) => {
      complete = resolve
    })
  })
  const engine = audio.create()
  const starting = engine.play()
  await Promise.resolve()
  engine.dispose()
  complete({ C4: {} })
  assert.equal(await starting, false)
  assert.equal(signal.aborted, true)
  assert.equal(audio.samplers.length, 0)

  const stoppedEngine = audio.create()
  const stoppedLoad = stoppedEngine.play()
  await Promise.resolve()
  stoppedEngine.stop()
  complete({ C4: {} })
  assert.equal(await stoppedLoad, false)
  assert.equal(audio.samplers.length, 0)
  stoppedEngine.dispose()

  let attempts = 0
  const retryAudio = audioHarness(async () => {
    if (++attempts === 1) throw new Error('decode failed')
    return { C4: {} }
  })
  const retryEngine = retryAudio.create()
  await assert.rejects(retryEngine.play(), /decode failed/)
  assert.equal(await retryEngine.play(), true)
  assert.equal(attempts, 2)
  retryEngine.dispose()
})

test('preserves fractional timing, trailing rests and compound-meter clicks; ships all licensed samples', () => {
  const example = { ...progression, totalBars: 2, timeSignature: { numerator: 6, denominator: 8 } }
  assert.deepEqual(getTiming(example), { beatUnit: 0.5, beatsPerBar: 3, totalBeats: 6 })
  const clicks = getMetronomeBeats(example)
  assert.equal(clicks.length, 12)
  assert.deepEqual(
    clicks.filter((click) => click.accent).map((click) => click.beat),
    [0, 3]
  )
  assert.equal(clicks.at(-1).beat, 5.5)
  const notes = getPlaybackNotes(
    {
      ...example,
      notes: [
        { id: 'ended', startBeat: 0, durationBeats: 1 / 3 },
        { id: 'held', startBeat: 1 / 3, durationBeats: 2 },
        { id: 'future', startBeat: 3, durationBeats: 1 }
      ]
    },
    1
  )
  assert.deepEqual(
    notes.map((note) => note.id),
    ['held', 'future']
  )
  assert.equal(notes[0].startBeat, 1)
  assert.ok(Math.abs(notes[0].durationBeats - 4 / 3) < 1e-12)
  assert.equal(notes[0].resumed, true)
  assert.equal(notes[1].resumed, false)

  const root = new URL('../src/renderer/public/audio/salamander/', import.meta.url)
  assert.equal(pianoSampleFiles.length, 30)
  assert.equal(
    pianoSampleFiles.reduce((size, name) => size + statSync(new URL(name, root)).size, 0),
    2012677
  )
  assert.match(readFileSync(new URL('ATTRIBUTION.txt', root), 'utf8'), /Alexander Holm/)
  assert.match(readFileSync(new URL('LICENSE.txt', root), 'utf8'), /Attribution 3.0/)
})
