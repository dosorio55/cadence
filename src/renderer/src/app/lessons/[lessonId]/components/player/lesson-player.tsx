import { useId } from 'react'
import { Button } from '@/components/ui/button'
import { Checkbox } from '@/components/ui/checkbox'
import { Label } from '@/components/ui/label'
import type { Progression, Stage } from '../../types'
import { LessonExample } from '../lesson-example'
import { PianoVisuals } from './piano-visuals'
import { getTiming } from './playback-plan'
import { useLessonPlayback } from './use-lesson-playback'

export function LessonPlayer({
  stage,
  progression,
  stageHref
}: {
  stage: Stage
  progression: Progression
  stageHref: string
}) {
  const player = useLessonPlayback(progression)
  const id = useId()
  const { beatUnit, beatsPerBar, totalBeats } = getTiming(progression)
  const position = Math.min(player.beat, totalBeats - 0.000001)
  const bar = Math.floor(position / beatsPerBar) + 1
  const pulse = Math.floor((position % beatsPerBar) / beatUnit)
  const loading = player.status === 'loading'
  const playing = player.status === 'playing'

  return (
    <div className="flex flex-1 flex-col gap-4">
      <LessonExample
        stage={stage}
        progression={progression}
        stageHref={stageHref}
        tempo={player.tempo}
        currentBeat={player.sounding ? player.beat : undefined}
      />
      <section
        aria-label="Reproductor del ejemplo"
        className="space-y-4 rounded-panel border border-border bg-surface p-4"
      >
        <div className="flex flex-wrap items-center gap-3">
          <Button onClick={() => void player.play()} disabled={loading || playing}>
            {loading ? 'Cargando piano…' : player.status === 'paused' ? 'Continuar' : 'Reproducir'}
          </Button>
          <Button variant="outline" onClick={player.pause} disabled={!playing}>
            Pausa
          </Button>
          <Button variant="outline" onClick={player.stop}>
            Detener
          </Button>
          <div className="flex items-center gap-2">
            <Checkbox
              id={`${id}-loop`}
              checked={player.loop}
              onCheckedChange={player.changeLoop}
              disabled={loading || !progression.loopable}
            />
            <Label htmlFor={`${id}-loop`}>Repetir ejemplo</Label>
          </div>
        </div>

        <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
          <div className="space-y-2">
            <Label htmlFor={`${id}-tempo`}>Tempo · ♩ = {player.tempo} BPM</Label>
            <input
              id={`${id}-tempo`}
              type="range"
              min="40"
              max="180"
              step="1"
              value={player.tempo}
              disabled={loading}
              onChange={(event) => player.changeTempo(Number(event.target.value))}
              className="w-full accent-primary"
            />
            <p className="text-caption text-muted-foreground">
              BPM en negras. Cambiar tempo reinicia el ejemplo.
            </p>
          </div>
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <Checkbox
                id={`${id}-metronome`}
                checked={player.metronome}
                onCheckedChange={player.changeMetronome}
                disabled={loading}
              />
              <Label htmlFor={`${id}-metronome`}>Metrónomo</Label>
            </div>
            <Label htmlFor={`${id}-click-volume`}>
              Volumen del clic · {Math.round(player.clickVolume * 100)} %
            </Label>
            <input
              id={`${id}-click-volume`}
              type="range"
              min="0"
              max="1"
              step="0.05"
              value={player.clickVolume}
              disabled={loading}
              onChange={(event) => player.changeClickVolume(Number(event.target.value))}
              className="w-full accent-primary"
            />
          </div>
          <div className="space-y-2">
            <p className="font-mono text-caption">
              Compás {bar}/{progression.totalBars} · pulso {pulse + 1}/
              {progression.timeSignature.numerator}
            </p>
            <div aria-hidden="true" className="flex gap-2">
              {Array.from({ length: progression.timeSignature.numerator }, (_, index) => (
                <span
                  key={index}
                  className={`grid size-8 place-items-center rounded-pill border border-border font-mono text-caption ${player.sounding && index === pulse ? 'bg-primary text-primary-foreground' : 'bg-surface-raised text-muted-foreground'}`}
                >
                  {index + 1}
                </span>
              ))}
            </div>
            <p className="text-caption text-muted-foreground">
              Un clic por figura del compás; el primero lleva acento.
            </p>
          </div>
        </div>
        <progress
          aria-label="Posición en el ejemplo"
          value={player.beat}
          max={totalBeats}
          className="h-2 w-full accent-primary"
        />
        {loading && (
          <p role="status" className="text-caption text-muted-foreground">
            Preparando muestras locales. No se necesita conexión a internet.
          </p>
        )}
        {player.error && (
          <p role="alert" className="text-body text-destructive">
            {player.error}
          </p>
        )}
      </section>
      <PianoVisuals progression={progression} beat={player.beat} sounding={player.sounding} />
      <details className="text-caption text-muted-foreground">
        <summary className="cursor-pointer">Sonido del piano y licencia</summary>
        <p className="mt-2">
          Salamander Grand Piano — grabaciones de Alexander Holm, CC BY 3.0. Muestras MP3
          distribuidas por Tone.js; reproducción con cambio de altura. El README original acredita
          una versión reafinada por Markus Fiedler.
        </p>
        <div className="mt-2 flex flex-wrap gap-4">
          <a
            href="https://github.com/Tonejs/audio/tree/869b6f8d9cddb47d966238c012041480b1ce517a/salamander"
            target="_blank"
            rel="noreferrer"
            className="underline"
          >
            Créditos y origen
          </a>
          <a
            href="https://creativecommons.org/licenses/by/3.0/"
            target="_blank"
            rel="noreferrer"
            className="underline"
          >
            Licencia completa
          </a>
        </div>
      </details>
    </div>
  )
}
