const blackPitchClasses = new Set([1, 3, 6, 8, 10])
const pitchNames = ['C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B']

export const rollHeight = 240
export const visibleBeats = 8

export function pitchName(midi: number): string {
  return `${pitchNames[midi % 12]}${Math.floor(midi / 12) - 1}`
}

export function getKeyboard(pitches: number[]) {
  let first = 21
  let last = 108

  for (const midi of pitches) {
    first = Math.min(first, midi)
    last = Math.max(last, midi)
  }

  if (blackPitchClasses.has(first % 12)) {
    first -= 1
  }

  if (blackPitchClasses.has(last % 12)) {
    last += 1
  }

  const keys: { midi: number; x: number; width: number; black: boolean }[] = []
  let width = 0

  for (let midi = first; midi <= last; midi += 1) {
    const black = blackPitchClasses.has(midi % 12)
    keys.push({ midi, x: black ? width - 7 : width, width: black ? 14 : 24, black })

    if (!black) {
      width += 24
    }
  }

  return { keys, width }
}

export function isNoteActive(
  note: { startBeat: number; durationBeats: number },
  beat: number,
  sounding: boolean
): boolean {
  return sounding && note.startBeat <= beat && beat < note.startBeat + note.durationBeats
}

export function getNoteWindow(note: { startBeat: number; durationBeats: number }, beat: number) {
  const start = Math.max(0, note.startBeat - beat)
  const end = Math.min(visibleBeats, note.startBeat + note.durationBeats - beat)

  if (end <= start) {
    return null
  }

  return {
    y: rollHeight * (1 - end / visibleBeats),
    height: ((end - start) / visibleBeats) * rollHeight
  }
}

export function getBeatGrid(
  beat: number,
  numerator: number,
  denominator: number,
  totalBars: number
) {
  const pulseLength = 4 / denominator
  const first = Math.max(0, Math.ceil(beat / pulseLength))
  const last = Math.min(totalBars * numerator, Math.floor((beat + visibleBeats) / pulseLength))

  return Array.from({ length: Math.max(0, last - first + 1) }, (_, offset) => {
    const pulse = first + offset
    return {
      pulse,
      y: rollHeight * (1 - (pulse * pulseLength - beat) / visibleBeats),
      isBar: pulse % numerator === 0,
      label: `${Math.floor(pulse / numerator) + 1}.${(pulse % numerator) + 1}`
    }
  })
}
