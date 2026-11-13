'use client'

import {
  PanelLeftCloseIcon,
  PanelLeftOpenIcon,
  PanelRightCloseIcon,
  PanelRightOpenIcon
} from '@hugeicons/core-free-icons'
import { HugeiconsIcon } from '@hugeicons/react'
import { type ReactNode, useState } from 'react'
import { Button } from '@/components/ui/button'
import { Collapsible, CollapsibleContent } from '@/components/ui/collapsible'

export function PracticeWorkspace({
  stages,
  guidance,
  children
}: {
  stages: ReactNode
  guidance: ReactNode
  children: ReactNode
}) {
  const [showStages, setShowStages] = useState(true)
  const [showGuidance, setShowGuidance] = useState(false)

  return (
    <div className="flex flex-1 flex-col lg:flex-row">
      <Collapsible
        open={showStages}
        onOpenChange={setShowStages}
        className="order-1 shrink-0 lg:flex lg:flex-col"
      >
        <CollapsibleContent
          id="lesson-stages"
          keepMounted
          className="border-b border-border bg-surface lg:flex-1 lg:border-r lg:border-b-0"
        >
          <aside className="p-4 lg:w-60">
            <div className="mb-4 flex items-center justify-between gap-3">
              <h2 className="font-mono text-label uppercase tracking-widest text-muted-foreground">
                El recorrido
              </h2>
              <Button
                variant="ghost"
                size="icon"
                aria-label="Ocultar etapas"
                title="Ocultar etapas"
                aria-expanded={showStages}
                aria-controls="lesson-stages"
                onClick={() => setShowStages(false)}
              >
                <HugeiconsIcon icon={PanelLeftCloseIcon} strokeWidth={2} aria-hidden="true" />
              </Button>
            </div>
            {stages}
          </aside>
        </CollapsibleContent>
      </Collapsible>
      <div className="relative order-3 flex min-w-0 flex-1 flex-col lg:order-2">
        {!showStages && (
          <Button
            variant="outline"
            size="icon"
            className="absolute top-3 left-3 z-10 bg-surface shadow-sm"
            aria-label="Mostrar etapas"
            title="Mostrar etapas"
            aria-expanded={showStages}
            aria-controls="lesson-stages"
            onClick={() => setShowStages(true)}
          >
            <HugeiconsIcon icon={PanelLeftOpenIcon} strokeWidth={2} aria-hidden="true" />
          </Button>
        )}
        {!showGuidance && (
          <Button
            variant="outline"
            size="icon"
            className="absolute top-3 right-3 z-10 bg-surface shadow-sm"
            aria-label="Abrir guía de práctica"
            title="Abrir guía de práctica"
            aria-expanded={showGuidance}
            aria-controls="lesson-guidance"
            onClick={() => setShowGuidance(true)}
          >
            <HugeiconsIcon icon={PanelRightOpenIcon} strokeWidth={2} aria-hidden="true" />
          </Button>
        )}
        {children}
      </div>
      <Collapsible
        open={showGuidance}
        onOpenChange={setShowGuidance}
        className="order-2 shrink-0 lg:order-3 lg:flex lg:flex-col"
      >
        <CollapsibleContent
          id="lesson-guidance"
          keepMounted
          className="border-b border-border bg-surface lg:flex-1 lg:border-b-0 lg:border-l"
        >
          <aside className="space-y-6 p-5 lg:w-80">
            <div className="flex items-center justify-between gap-3">
              <h2 className="font-mono text-label uppercase tracking-widest text-primary">
                Guía de práctica
              </h2>
              <Button
                variant="ghost"
                size="icon"
                aria-label="Ocultar guía"
                title="Ocultar guía"
                aria-expanded={showGuidance}
                aria-controls="lesson-guidance"
                onClick={() => setShowGuidance(false)}
              >
                <HugeiconsIcon icon={PanelRightCloseIcon} strokeWidth={2} aria-hidden="true" />
              </Button>
            </div>
            {guidance}
          </aside>
        </CollapsibleContent>
      </Collapsible>
    </div>
  )
}
