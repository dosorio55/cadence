import type { Lesson } from '../../../shared/api'

export function selectExample(
  lesson: Lesson,
  stageId: string | string[] | undefined,
  progressionId: string | string[] | undefined
) {
  const requestedStage = lesson.stages.find((item) => item.id === stageId)
  const stage = requestedStage ?? lesson.stages[0]

  if (!stage) {
    throw new Error(`No stages for ${lesson.id}`)
  }

  const requestedProgression = stage.progressions.find((item) => item.id === progressionId)
  const progression =
    requestedProgression ?? stage.progressions.find((item) => item.kind === 'primary')

  if (!progression) {
    throw new Error(`Missing primary progression for ${stage.id}`)
  }

  return {
    stage,
    progression,
    invalidStage: stageId !== undefined && !requestedStage,
    invalidProgression: progressionId !== undefined && !requestedProgression
  }
}
