import type { Context } from 'tone'

export const pianoSampleFiles = [
  ...Array.from({ length: 8 }, (_, octave) => `A${octave}.mp3`),
  ...Array.from({ length: 8 }, (_, octave) => `C${octave + 1}.mp3`),
  ...Array.from({ length: 7 }, (_, octave) => `Ds${octave + 1}.mp3`),
  ...Array.from({ length: 7 }, (_, octave) => `Fs${octave + 1}.mp3`)
]

let decodedSamples: Record<string, AudioBuffer> | undefined

export async function loadPianoSamples(context: Context, signal: AbortSignal) {
  if (decodedSamples) {
    return decodedSamples
  }

  const entries = await Promise.all(
    pianoSampleFiles.map(async (filename) => {
      const response = await fetch(`${import.meta.env.BASE_URL}audio/salamander/${filename}`, {
        signal
      })

      if (!response.ok) {
        throw new Error('No se pudieron cargar las muestras del piano.')
      }

      const buffer = await context.decodeAudioData(await response.arrayBuffer())
      const pitch = filename.replace('.mp3', '').replace('Ds', 'D#').replace('Fs', 'F#')
      return [pitch, buffer] as const
    })
  )

  signal.throwIfAborted()
  decodedSamples = Object.fromEntries(entries)
  return decodedSamples
}
