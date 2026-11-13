import { selectExample } from '../src/renderer/src/lib/curriculum.ts'
import assert from 'node:assert/strict'
import test from 'node:test'
import { getLesson, pilotLessonId } from '../src/main/curriculum.ts'

const lesson = getLesson(pilotLessonId)

test("loads the pilot in order and keeps every example's chord and note events together", () => {
  assert.ok(lesson)
  assert.deepEqual(
    lesson.stages.map((stage) => stage.order),
    [1, 2, 3, 4, 5]
  )
  assert.equal(lesson.category.id, 'cat-rhythm')
  assert.equal(lesson.prerequisites.length, 2)
  assert.equal(lesson.stages.flatMap((stage) => stage.progressions).length, 6)

  for (const stage of lesson.stages) {
    assert.equal(stage.progressions.filter((item) => item.kind === 'primary').length, 1)

    for (const example of stage.progressions) {
      assert.ok(example.chords.length > 0)
      assert.ok(example.notes.length > 0)
      assert.ok(
        [...example.chords, ...example.notes].every((event) => event.progressionId === example.id)
      )
      assert.deepEqual(
        example.notes.map((note) => note.startBeat),
        example.notes.map((note) => note.startBeat).sort((a, b) => a - b)
      )
    }
  }

  const anticipated = lesson.stages[1].progressions[0]
  assert.ok(anticipated.notes.some((note) => note.startBeat === 11.5))
  assert.ok(!anticipated.notes.some((note) => note.startBeat === 12))
  assert.equal(getLesson('does-not-exist'), null)
})

test('selects the primary by default and alternatives only within their own stage', () => {
  const initial = selectExample(lesson, undefined, undefined)
  assert.equal(initial.stage.order, 1)
  assert.equal(initial.progression.kind, 'primary')
  assert.equal(initial.invalidStage, false)
  assert.equal(initial.invalidProgression, false)

  const lastStage = lesson.stages[4]
  const alternative = lastStage.progressions.find((item) => item.kind === 'alternative')
  const selected = selectExample(lesson, lastStage.id, alternative.id)
  assert.equal(selected.progression.id, alternative.id)
  assert.notDeepEqual(
    selected.progression.chords,
    lastStage.progressions.find((item) => item.kind === 'primary').chords
  )

  const foreignExample = selectExample(lesson, lesson.stages[0].id, alternative.id)
  assert.equal(foreignExample.progression.kind, 'primary')
  assert.equal(foreignExample.invalidProgression, true)
})

test('invalid and repeated query values fall back visibly without selecting foreign content', () => {
  for (const stage of ['missing', [lesson.stages[1].id, lesson.stages[2].id]]) {
    const result = selectExample(lesson, stage, ['invalid', 'repeated'])
    assert.equal(result.stage.order, 1)
    assert.equal(result.progression.kind, 'primary')
    assert.equal(result.invalidStage, true)
    assert.equal(result.invalidProgression, true)
  }
})
