import { Badge } from '@/components/ui/badge'

export function MusicPlaceholders() {
  return (
    <div className="flex flex-1 flex-col gap-3">
      <section
        aria-labelledby="piano-roll-heading"
        className="flex min-h-72 flex-1 flex-col items-center justify-center rounded-panel border border-dashed border-border bg-surface-raised px-6 py-12 sm:min-h-96"
      >
        <p className="font-mono text-label uppercase tracking-widest text-muted-foreground">
          Espacio de visualización
        </p>
        <h2 id="piano-roll-heading" className="mt-3 font-display text-title font-semibold">
          Piano roll
        </h2>
        <p className="mt-2 max-w-sm text-center text-body text-muted-foreground">
          Aquí verás las notas, sus duraciones y el recorrido de ambas manos durante el ejemplo.
        </p>
        <Badge variant="outline" className="mt-5">
          Pendiente de implementación
        </Badge>
      </section>
      <section
        aria-label="Espacio reservado para reproducción"
        className="flex flex-wrap items-center justify-between gap-3 rounded-control border border-dashed border-border bg-surface px-5 py-4"
      >
        <h2 className="text-body font-semibold">Reproducción de audio</h2>
        <p className="text-caption text-muted-foreground">
          Play / pausa · bucle · tempo · metrónomo — próximamente
        </p>
      </section>
      <section
        aria-labelledby="keyboard-heading"
        className="flex min-h-28 flex-wrap items-center justify-between gap-3 rounded-panel border border-dashed border-border bg-surface-raised px-5 py-5"
      >
        <div>
          <h2 id="keyboard-heading" className="text-body font-semibold">
            Teclado de piano
          </h2>
          <p className="mt-1 text-caption text-muted-foreground">
            Espacio reservado para las teclas y las notas activas.
          </p>
        </div>
        <span className="font-mono text-label uppercase tracking-widest text-muted-foreground">
          Próximamente
        </span>
      </section>
    </div>
  )
}
