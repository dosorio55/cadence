import { Link } from 'react-router-dom'
import type { Lesson } from '../../../../../shared/api'
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger
} from '@/components/ui/accordion'
import { selectExample } from '@/lib/curriculum'
import { LessonPlayer } from './components/player/lesson-player'
import { LessonText } from './components/lesson-text'
import { PracticeWorkspace } from './components/practice-workspace'
import { SelfAssessment } from './components/self-assessment'
import { StageInstructions } from './components/stage-instructions'
import { StageNavigation } from './components/stage-navigation'

export default function LessonPage({
  lesson,
  query
}: {
  lesson: Lesson
  query: Record<string, string | string[] | undefined>
}) {
  const { stage, progression, invalidStage, invalidProgression } = selectExample(
    lesson,
    query.stage,
    query.example
  )
  const stageIndex = lesson.stages.findIndex((item) => item.id === stage.id)
  const previous = lesson.stages[stageIndex - 1]
  const next = lesson.stages[stageIndex + 1]
  const stageHref = (id: string) => `/lessons/${lesson.id}?stage=${id}`

  return (
    <main className="flex w-full flex-1 flex-col">
      <header className="flex flex-wrap items-center justify-between gap-4 border-b border-border px-4 py-4 sm:px-6">
        <div>
          <Link to="/" className="text-caption text-muted-foreground hover:text-foreground">
            ← Biblioteca / {lesson.category.name}
          </Link>
          <h1 className="mt-1 font-display text-title font-semibold">{lesson.title}</h1>
        </div>
        <p className="font-mono text-caption text-muted-foreground">
          Dificultad {lesson.difficulty}/5 · {lesson.targetMinutes} min ·{' '}
          {lesson.styleTags.join(' / ')}
        </p>
      </header>
      {(invalidStage || invalidProgression) && (
        <p role="status" className="border-b border-border bg-muted px-6 py-3 text-body">
          {invalidStage ? 'La etapa solicitada no existe. Se muestra la primera etapa. ' : ''}
          {invalidProgression
            ? 'El ejemplo solicitado no pertenece a esta etapa. Se muestra el principal.'
            : ''}
        </p>
      )}
      <PracticeWorkspace
        stages={
          <nav aria-label="Etapas de la lección">
            <ol className="grid gap-2 sm:grid-cols-2 lg:grid-cols-1">
              {lesson.stages.map((item) => (
                <li key={item.id}>
                  <Link
                    to={stageHref(item.id)}
                    aria-current={item.id === stage.id ? 'step' : undefined}
                    className="flex gap-3 rounded-control border border-transparent px-3 py-3 text-body text-muted-foreground hover:bg-surface-raised aria-current:border-border aria-current:bg-surface-raised aria-current:text-foreground"
                  >
                    <span className="font-mono text-primary">
                      {String(item.order).padStart(2, '0')}
                    </span>
                    <span>{item.title}</span>
                  </Link>
                </li>
              ))}
            </ol>
            <p className="mt-6 text-caption text-muted-foreground">
              Puedes volver a cualquier etapa. No hay progreso guardado.
            </p>
          </nav>
        }
        guidance={
          <>
            <section aria-labelledby="guidance-heading">
              <h2 id="guidance-heading" className="mt-2 font-display text-title font-semibold">
                Entiende el cambio
              </h2>
              <div className="mt-3">
                <LessonText text={stage.explanationMd} />
              </div>
            </section>
            <SelfAssessment
              key={`${stage.id}:${progression.id}`}
              criteria={stage.successCriteria}
            />
            <Accordion multiple>
              {[
                ['simplify', 'Si necesitas simplificar', stage.simplifyHint],
                ['extend', 'Para ir más allá', stage.extendHint]
              ].map(
                ([value, title, hint]) =>
                  hint && (
                    <AccordionItem key={value} value={value}>
                      <AccordionTrigger>{title}</AccordionTrigger>
                      <AccordionContent>
                        <LessonText text={hint} />
                      </AccordionContent>
                    </AccordionItem>
                  )
              )}
              <AccordionItem value="lesson">
                <AccordionTrigger>Sobre esta lección</AccordionTrigger>
                <AccordionContent>
                  <div className="space-y-3">
                    <LessonText text={lesson.goal} />
                    <LessonText text={lesson.introMd} />
                    <p className="text-caption text-muted-foreground">
                      Habilidad: {lesson.skill.name}
                    </p>
                    <p className="text-caption text-muted-foreground">
                      Prerrequisitos sugeridos:{' '}
                      {lesson.prerequisites.length
                        ? lesson.prerequisites.map((item) => item.title).join('; ')
                        : 'ninguno'}
                      . No bloquean la lección.
                    </p>
                  </div>
                </AccordionContent>
              </AccordionItem>
              <AccordionItem value="example">
                <AccordionTrigger>Sobre el ejemplo</AccordionTrigger>
                <AccordionContent>
                  <LessonText text={progression.description} />
                </AccordionContent>
              </AccordionItem>
            </Accordion>
          </>
        }
      >
        <StageInstructions stage={stage} totalStages={lesson.stages.length} />
        <div className="flex flex-1 flex-col gap-4 p-4 sm:p-6">
          <LessonPlayer
            key={progression.id}
            stage={stage}
            progression={progression}
            stageHref={stageHref(stage.id)}
          />
        </div>
      </PracticeWorkspace>
      <StageNavigation
        key={stage.id}
        previousHref={previous ? stageHref(previous.id) : undefined}
        nextHref={next ? stageHref(next.id) : undefined}
        stageOrder={stage.order}
        totalStages={lesson.stages.length}
      />
    </main>
  )
}
