import categories from '../../lesson-content/approved/categories.json' with { type: 'json' }
import lessons from '../../lesson-content/approved/lessons.json' with { type: 'json' }
import skills from '../../lesson-content/approved/skills.json' with { type: 'json' }

export function getCurriculumLibrary() {
  const libraryLessons = lessons.map((lesson) => {
    const skill = skills.find((item) => item.id === lesson.primarySkillId)

    if (!skill) {
      throw new Error(`Missing skill for ${lesson.id}`)
    }

    if (!categories.some((category) => category.id === skill.categoryId)) {
      throw new Error(`Missing category for ${skill.id}`)
    }

    return {
      ...lesson,
      skill,
      href: `/lessons/${lesson.id}`
    }
  })

  return [...categories]
    .sort((a, b) => a.order - b.order)
    .map((category) => ({
      ...category,
      lessons: libraryLessons
        .filter((lesson) => lesson.skill.categoryId === category.id)
        .sort((a, b) => a.orderInCategory - b.orderInCategory)
    }))
}
