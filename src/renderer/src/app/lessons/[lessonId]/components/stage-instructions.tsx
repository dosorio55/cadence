import type { Stage } from '../types'
import { LessonText } from './lesson-text'

export function StageInstructions({ stage, totalStages }: { stage: Stage; totalStages: number }) {
  return (
    <section aria-labelledby="stage-heading" className="border-b border-border px-4 py-5 sm:px-6">
      <p className="px-8 font-mono text-label uppercase tracking-widest text-primary">
        Etapa {stage.order} de {totalStages}
      </p>
      <h2 id="stage-heading" className="mt-2 font-display text-title font-semibold">
        {stage.title}
      </h2>
      <div className="mt-4 grid gap-4 xl:grid-cols-2">
        <div className="max-w-prose">
          <h3 className="mb-1 text-label font-semibold uppercase tracking-widest text-primary">
            Qué cambia
          </h3>
          <LessonText text={stage.changeFromPrevious} />
        </div>
        <div className="max-w-prose">
          <h3 className="mb-1 text-label font-semibold uppercase tracking-widest text-primary">
            Tu tarea al piano
          </h3>
          <LessonText text={stage.task} />
        </div>
      </div>
    </section>
  )
}
