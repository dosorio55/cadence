import categories from '../../lesson-content/approved/categories.json' with { type: 'json' }
import chords from '../../lesson-content/approved/chord-events.json' with { type: 'json' }
import lessons from '../../lesson-content/approved/lessons.json' with { type: 'json' }
import notes from '../../lesson-content/approved/note-events.json' with { type: 'json' }
import progressions from '../../lesson-content/approved/progressions.json' with { type: 'json' }
import skills from '../../lesson-content/approved/skills.json' with { type: 'json' }
import stages from '../../lesson-content/approved/stages.json' with { type: 'json' }

export const pilotLessonId = 'lesson-rhythm-004'

export function getLesson(lessonId: string) {
  const lesson = lessons.find((item) => item.id === lessonId)

  if (!lesson) {
    return null
  }

  const skill = skills.find((item) => item.id === lesson.primarySkillId)

  if (!skill) {
    throw new Error(`Missing skill for ${lesson.id}`)
  }

  const category = categories.find((item) => item.id === skill.categoryId)

  if (!category) {
    throw new Error(`Missing category for ${skill.id}`)
  }

  const orderedStages = stages
    .filter((item) => item.lessonId === lesson.id)
    .sort((a, b) => a.order - b.order)
    .map((stage) => ({
      ...stage,
      progressions: progressions
        .filter((item) => item.stageId === stage.id)
        .sort((a, b) => a.order - b.order || a.id.localeCompare(b.id))
        .map((progression) => ({
          ...progression,
          chords: chords
            .filter((item) => item.progressionId === progression.id)
            .sort((a, b) => a.startBeat - b.startBeat || a.order - b.order),
          notes: notes
            .filter((item) => item.progressionId === progression.id)
            .sort((a, b) => a.startBeat - b.startBeat || a.midi - b.midi)
        }))
    }))

  return {
    ...lesson,
    skill,
    category,
    stages: orderedStages,
    prerequisites: lesson.prerequisiteLessonIds.map((id) => {
      const prerequisite = lessons.find((item) => item.id === id)

      if (!prerequisite) {
        throw new Error(`Missing prerequisite ${id}`)
      }

      return prerequisite
    })
  }
}
