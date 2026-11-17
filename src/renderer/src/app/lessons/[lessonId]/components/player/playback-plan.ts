import type { Progression } from '../../types'

export const ticksPerBeat = 960

export function getTiming(progression: Progression) {
  const beatUnit = 4 / progression.timeSignature.denominator
  const beatsPerBar = progression.timeSignature.numerator * beatUnit

  return { beatUnit, beatsPerBar, totalBeats: progression.totalBars * beatsPerBar }
}

export function getPlaybackNotes(progression: Progression, fromBeat = 0) {
  return progression.notes
    .filter((note) => note.startBeat + note.durationBeats > fromBeat)
    .map((note) => ({
      ...note,
      resumed: note.startBeat < fromBeat,
      startBeat: Math.max(note.startBeat, fromBeat),
      durationBeats: note.startBeat + note.durationBeats - Math.max(note.startBeat, fromBeat)
    }))
}

export function getMetronomeBeats(progression: Progression) {
  const { beatUnit } = getTiming(progression)
  const numerator = progression.timeSignature.numerator

  return Array.from({ length: progression.totalBars * numerator }, (_, index) => ({
    beat: index * beatUnit,
    accent: index % numerator === 0
  }))
}

export function midiFrequency(midi: number) {
  return 440 * 2 ** ((midi - 69) / 12)
}
