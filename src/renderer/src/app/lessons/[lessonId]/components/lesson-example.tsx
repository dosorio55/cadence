import { Link } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { Card, CardContent } from '@/components/ui/card'
import type { Progression, Stage } from '../types'

export function LessonExample({
  stage,
  progression,
  stageHref,
  tempo = progression.bpm,
  currentBeat
}: {
  stage: Stage
  progression: Progression
  stageHref: string
  tempo?: number
  currentBeat?: number
}) {
  const currentChord =
    currentBeat === undefined
      ? undefined
      : progression.chords.find(
          (chord) =>
            currentBeat >= chord.startBeat && currentBeat < chord.startBeat + chord.durationBeats
        )

  return (
    <section aria-labelledby="example-heading" className="space-y-4">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h2 id="example-heading" className="text-body font-semibold">
            {progression.title}
          </h2>
          <p className="mt-1 font-mono text-caption text-muted-foreground">
            {progression.keyTonic}{' '}
            {progression.keyMode === 'major'
              ? 'mayor'
              : progression.keyMode === 'minor'
                ? 'menor'
                : progression.keyMode}{' '}
            · ♩ = {tempo} · {progression.timeSignature.numerator}/
            {progression.timeSignature.denominator} · {progression.totalBars} compases
          </p>
        </div>
        {stage.progressions.length > 1 && (
          <nav aria-label="Ejemplos de esta etapa" className="flex flex-wrap gap-2">
            {stage.progressions.map((item) => (
              <Button
                key={item.id}
                variant={item.id === progression.id ? 'default' : 'outline'}
                render={<Link to={`${stageHref}&example=${item.id}`} />}
                nativeButton={false}
                aria-current={item.id === progression.id ? 'true' : undefined}
              >
                {item.kind === 'primary' ? 'Principal' : item.title}
              </Button>
            ))}
          </nav>
        )}
      </div>
      <ol aria-label="Secuencia armónica" className="flex gap-2 overflow-x-auto pb-2">
        {progression.chords.map((chord) => (
          <li
            key={chord.id}
            className="min-w-32 flex-1"
            aria-current={currentChord?.id === chord.id ? 'true' : undefined}
          >
            <Card
              size="sm"
              className={`h-full ${currentChord?.id === chord.id ? 'ring-2 ring-primary' : ''}`}
            >
              <CardContent>
                <div className="flex items-baseline justify-between gap-4">
                  <p className="font-mono text-title font-semibold">{chord.symbol}</p>
                  <p className="text-caption text-primary">{chord.function}</p>
                </div>
                <p className="mt-2 font-mono text-caption text-muted-foreground">
                  Beat {chord.startBeat} · {chord.durationBeats} negras
                </p>
              </CardContent>
            </Card>
          </li>
        ))}
      </ol>
      <p className="text-caption text-muted-foreground">
        Beats contados desde 0, en negras. Acordes del ejemplo seleccionado.
      </p>
    </section>
  )
}
