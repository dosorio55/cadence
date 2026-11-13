import { Checkbox } from '@/components/ui/checkbox'
import { Label } from '@/components/ui/label'

export function SelfAssessment({ criteria }: { criteria: string[] }) {
  return (
    <section aria-labelledby="assessment-heading">
      <h2 id="assessment-heading" className="font-display text-title font-semibold">
        ¿Cómo te fue?
      </h2>
      <p className="mt-2 text-caption text-muted-foreground">
        Tu propia evaluación, no una calificación automática. Estas marcas no se guardan.
      </p>
      <div className="mt-4 space-y-4">
        {criteria.map((criterion) => (
          <Label key={criterion} className="flex cursor-pointer items-start gap-3 text-body">
            <Checkbox className="mt-1" />
            <span>{criterion}</span>
          </Label>
        ))}
      </div>
    </section>
  )
}
