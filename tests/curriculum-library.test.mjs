import assert from 'node:assert/strict'
import test from 'node:test'
import categories from '../lesson-content/approved/categories.json' with { type: 'json' }
import lessons from '../lesson-content/approved/lessons.json' with { type: 'json' }
import skills from '../lesson-content/approved/skills.json' with { type: 'json' }
import { getLesson } from '../src/main/curriculum.ts'
import { getCurriculumLibrary } from '../src/main/curriculum-library.ts'

test('lists all approved lessons in category order with available lesson links', () => {
  const library = getCurriculumLibrary()
  const listedLessons = library.flatMap((category) => category.lessons)

  assert.equal(library.length, 6)
  assert.equal(listedLessons.length, 90)
  assert.deepEqual(
    library.map((category) => category.id),
    [...categories].sort((a, b) => a.order - b.order).map((category) => category.id)
  )
  assert.deepEqual(
    listedLessons.map((lesson) => lesson.id).sort(),
    lessons.map((lesson) => lesson.id).sort()
  )

  for (const category of library) {
    const categorySkills = skills
      .filter((skill) => skill.categoryId === category.id)
      .map((skill) => skill.id)
    const expected = lessons
      .filter((lesson) => categorySkills.includes(lesson.primarySkillId))
      .sort((a, b) => a.orderInCategory - b.orderInCategory)

    assert.equal(category.lessons.length, 15)
    assert.deepEqual(
      category.lessons.map((lesson) => lesson.id),
      expected.map((lesson) => lesson.id)
    )

    for (const [index, lesson] of category.lessons.entries()) {
      const approved = expected[index]

      assert.equal(lesson.title, approved.title)
      assert.equal(lesson.goal, approved.goal)
      assert.equal(lesson.difficulty, approved.difficulty)
      assert.equal(lesson.targetMinutes, approved.targetMinutes)
      assert.deepEqual(
        lesson.skill,
        skills.find((skill) => skill.id === approved.primarySkillId)
      )
      assert.equal(lesson.href, `/lessons/${lesson.id}`)
      assert.equal(getLesson(lesson.href.slice('/lessons/'.length))?.id, lesson.id)
    }
  }
})
