'use client'

import { Link } from 'react-router-dom'
import { useState } from 'react'
import { Button } from '@/components/ui/button'

export function StageNavigation({
  previousHref,
  nextHref,
  stageOrder,
  totalStages
}: {
  previousHref?: string
  nextHref?: string
  stageOrder: number
  totalStages: number
}) {
  const [finished, setFinished] = useState(false)

  return (
    <footer className="sticky bottom-0 z-10 border-t border-border bg-surface px-4 py-3 sm:px-6">
      {finished && (
        <div role="status" className="mb-4 border-b border-border pb-4">
          <p className="text-body font-semibold">Llegaste al final del recorrido.</p>
          <p className="mt-1 text-caption text-muted-foreground">
            Puedes repetir cualquier etapa. Este repaso no acredita dominio ni guarda progreso.
          </p>
          <Button variant="link" className="mt-2" render={<Link to="/" />} nativeButton={false}>
            Volver a la biblioteca
          </Button>
        </div>
      )}
      <div className="flex flex-wrap items-center justify-between gap-3">
        {previousHref ? (
          <Button variant="outline" render={<Link to={previousHref} />} nativeButton={false}>
            ← Anterior
          </Button>
        ) : (
          <Button variant="outline" render={<Link to="/" />} nativeButton={false}>
            Biblioteca
          </Button>
        )}
        <p className="font-mono text-caption text-muted-foreground">
          Etapa {stageOrder} / {totalStages}
        </p>
        {nextHref ? (
          <Button render={<Link to={nextHref} />} nativeButton={false}>
            Siguiente etapa →
          </Button>
        ) : (
          <Button onClick={() => setFinished(true)}>Terminar repaso</Button>
        )}
      </div>
    </footer>
  )
}
