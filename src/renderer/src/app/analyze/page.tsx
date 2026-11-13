import { useState } from 'react'
import type { AudioAnalysis } from '../../../../shared/api'
import { Button } from '@/components/ui/button'

export default function AnalyzePage() {
  const [analysis, setAnalysis] = useState<AudioAnalysis | null>(null)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')

  async function analyze(): Promise<void> {
    setBusy(true)
    setError('')

    try {
      const result = await window.api.analyzeAudio()
      if (result) setAnalysis(result)
    } catch (cause) {
      setAnalysis(null)
      setError(cause instanceof Error ? cause.message : 'No se pudo analizar el audio.')
    } finally {
      setBusy(false)
    }
  }

  return (
    <main className="w-full flex-1 px-4 py-8 sm:px-6 lg:px-8">
      <h1 className="font-display text-heading font-semibold">Analizar acordes</h1>
      <p className="mt-3 max-w-prose text-body text-muted-foreground">
        Selecciona una grabación WAV, FLAC u OGG de máximo 200 MB. El análisis se realiza en tu
        computador, sin subir el audio a internet. Los acordes son estimaciones, no una evaluación
        de tu interpretación ni una transcripción de las notas del piano.
      </p>
      <Button className="mt-6" disabled={busy} onClick={() => void analyze()}>
        {busy ? 'Preparando motor y analizando…' : 'Seleccionar y analizar audio'}
      </Button>
      <p role="status" className="mt-3 text-caption text-muted-foreground">
        {busy
          ? 'La primera vez se cargan los modelos. El análisis puede tardar varios minutos; permanece en esta pantalla.'
          : 'Los resultados se muestran en segundos y no modifican las lecciones.'}
      </p>
      {error && (
        <p
          role="alert"
          className="mt-6 rounded-panel border border-border bg-surface p-4 text-body"
        >
          {error}
        </p>
      )}
      {analysis && (
        <section className="mt-8" aria-labelledby="analysis-heading" aria-busy={busy}>
          <h2 id="analysis-heading" className="font-display text-title font-semibold">
            {analysis.fileName}
          </h2>
          {analysis.chords.length === 0 ? (
            <p className="mt-3 text-body text-muted-foreground">No se detectaron segmentos.</p>
          ) : (
            <div className="mt-4 overflow-x-auto rounded-panel border border-border">
              <table className="w-full text-left text-body">
                <caption className="sr-only">Acordes estimados y sus tiempos en segundos</caption>
                <thead className="bg-surface">
                  <tr>
                    <th scope="col" className="px-4 py-3">
                      Inicio (s)
                    </th>
                    <th scope="col" className="px-4 py-3">
                      Fin (s)
                    </th>
                    <th scope="col" className="px-4 py-3">
                      Acorde estimado
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {analysis.chords.map((chord, index) => (
                    <tr key={index} className="border-t border-border">
                      <td className="px-4 py-3 font-mono">{chord.start_time.toFixed(2)}</td>
                      <td className="px-4 py-3 font-mono">{chord.end_time.toFixed(2)}</td>
                      <td className="px-4 py-3 font-mono">{chord.chord}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </section>
      )}
    </main>
  )
}
