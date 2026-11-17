import type * as Tone from 'tone'
import type { Progression } from '../../types'
import {
  getMetronomeBeats,
  getPlaybackNotes,
  getTiming,
  midiFrequency,
  ticksPerBeat
} from './playback-plan.ts'

type SampleLoader = (
  context: Tone.Context,
  signal: AbortSignal
) => Promise<Record<string, AudioBuffer>>

export class LessonAudioEngine {
  private tone: typeof Tone
  private progression: Progression
  private context: Tone.Context
  private limiter: Tone.Limiter
  private sampler?: Tone.Sampler
  private click?: Tone.Synth
  private loadSamples: SampleLoader
  private samples?: Promise<Record<string, AudioBuffer>>
  private abort = new AbortController()
  private generation = 0
  private disposed = false
  private playing = false
  private position = 0
  private startedAt = 0
  private tempo: number
  private loop = false
  private metronome = false
  private clickVolume = 0.25

  constructor(tone: typeof Tone, progression: Progression, loadSamples: SampleLoader) {
    this.tone = tone
    this.progression = progression
    this.loadSamples = loadSamples
    this.tempo = progression.bpm
    this.context = new tone.Context({ latencyHint: 'interactive', lookAhead: 0.08 })
    this.context.transport.PPQ = ticksPerBeat
    this.limiter = new tone.Limiter({ context: this.context, threshold: -1 }).toDestination()
  }

  async play(): Promise<boolean> {
    if (this.disposed || this.playing) {
      return false
    }

    const generation = ++this.generation
    await this.context.resume()

    this.samples ??= this.loadSamples(this.context, this.abort.signal).catch((error: unknown) => {
      this.samples = undefined
      throw error
    })

    const samples = await this.samples

    if (this.disposed || generation !== this.generation) {
      return false
    }

    const totalBeats = getTiming(this.progression).totalBeats

    if (this.position >= totalBeats) {
      this.position = 0
    }

    this.sampler = new this.tone.Sampler({
      context: this.context,
      urls: samples,
      attack: 0.005,
      release: 0.15,
      volume: -10
    }).connect(this.limiter)

    this.click = new this.tone.Synth({
      context: this.context,
      oscillator: { type: 'sine' },
      envelope: { attack: 0.001, decay: 0.025, sustain: 0, release: 0.01 }
    }).connect(this.limiter)

    this.setMetronome(this.metronome, this.clickVolume)

    const transport = this.context.transport
    transport.cancel(0)
    transport.bpm.value = this.tempo
    transport.loopStart = 0
    transport.loopEnd = `${Math.round(totalBeats * ticksPerBeat)}i`
    transport.loop = this.loop

    for (const note of this.progression.notes) {
      transport.schedule(
        (time) => {
          if (generation !== this.generation) {
            return
          }

          this.sampler?.triggerAttackRelease(
            midiFrequency(note.midi),
            (note.durationBeats * 60) / this.tempo,
            time,
            note.velocity / 127
          )
        },
        `${Math.round(note.startBeat * ticksPerBeat)}i`
      )
    }

    for (const click of getMetronomeBeats(this.progression)) {
      transport.schedule(
        (time) => {
          if (generation !== this.generation) {
            return
          }

          this.click?.triggerAttackRelease(
            click.accent ? 1320 : 880,
            0.025,
            time,
            click.accent ? 1 : 0.6
          )
        },
        `${Math.round(click.beat * ticksPerBeat)}i`
      )
    }

    this.startedAt = this.context.now()

    for (const note of getPlaybackNotes(this.progression, this.position)) {
      if (note.resumed) {
        this.sampler.triggerAttackRelease(
          midiFrequency(note.midi),
          (note.durationBeats * 60) / this.tempo,
          this.startedAt,
          note.velocity / 127
        )
      }
    }

    transport.start(this.startedAt, (this.position * 60) / this.tempo)
    this.playing = true
    return true
  }

  getBeat(): number {
    if (!this.playing || this.context.immediate() < this.startedAt) {
      return this.position
    }

    return Math.min(
      getTiming(this.progression).totalBeats,
      Math.max(0, this.context.transport.getTicksAtTime(this.context.immediate()) / ticksPerBeat)
    )
  }

  get audible(): boolean {
    return this.playing && this.context.immediate() >= this.startedAt
  }

  get interrupted(): boolean {
    return this.playing && this.context.state !== 'running'
  }

  pause(): void {
    this.position = this.getBeat()
    this.halt()
  }

  stop(atEnd = false): void {
    this.halt()
    this.position = atEnd ? getTiming(this.progression).totalBeats : 0
  }

  private halt(): void {
    this.generation++
    this.playing = false
    this.context.transport.stop(this.context.immediate())
    this.context.transport.cancel(0)

    // Disconnect the run: lookahead attacks and already-scheduled release tails must also go silent.
    this.sampler?.disconnect()
    this.sampler?.dispose()
    this.sampler = undefined
    this.click?.disconnect()
    this.click?.dispose()
    this.click = undefined
  }

  setTempo(tempo: number): void {
    this.stop()
    this.tempo = tempo
  }

  setLoop(loop: boolean): void {
    this.loop = loop && this.progression.loopable
    this.context.transport.loop = this.loop
  }

  setMetronome(enabled: boolean, volume: number): void {
    this.metronome = enabled
    this.clickVolume = volume
    this.click?.volume.setValueAtTime(
      enabled && volume > 0 ? 20 * Math.log10(volume) : -Infinity,
      this.context.immediate()
    )
  }

  dispose(): void {
    this.disposed = true
    this.abort.abort()
    this.halt()
    this.limiter.dispose()
    this.context.dispose()
  }
}
