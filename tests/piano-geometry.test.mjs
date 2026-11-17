import assert from 'node:assert/strict'
import test from 'node:test'
import {
  getBeatGrid,
  getKeyboard,
  getNoteWindow,
  isNoteActive,
  pitchName,
  rollHeight
} from '../src/renderer/src/app/lessons/[lessonId]/components/player/piano-geometry.ts'

test('full piano geometry aligns accidentals with adjacent natural keys', () => {
  const { keys, width } = getKeyboard([60, 61])
  assert.equal(keys.length, 88)
  assert.equal(keys[0].midi, 21)
  assert.equal(keys.at(-1).midi, 108)
  assert.equal(width, 52 * 24)

  const c = keys.find((key) => key.midi === 60)
  const sharp = keys.find((key) => key.midi === 61)
  const d = keys.find((key) => key.midi === 62)
  assert.equal(sharp.x + sharp.width / 2, c.x + c.width)
  assert.equal(d.x, c.x + c.width)
  assert.equal(pitchName(60), 'C4')
  assert.equal(pitchName(21), 'A0')
})

test('outlying accidentals extend the piano without clipping edge keys', () => {
  const { keys, width } = getKeyboard([18, 109])
  assert.equal(keys[0].midi, 17)
  assert.equal(keys.at(-1).midi, 110)
  assert.ok(keys.some((key) => key.midi === 18))
  assert.ok(keys.every((key) => key.x >= 0 && key.x + key.width <= width))
  assert.equal(getKeyboard([]).keys.length, 88)
})

test('falling notes reach the keyboard at onset and clear exactly at note-off or pause', () => {
  const note = { startBeat: 4, durationBeats: 2 }
  assert.equal(getNoteWindow(note, -5), null)
  assert.deepEqual(getNoteWindow(note, 0), { y: 60, height: 60 })
  assert.deepEqual(getNoteWindow(note, 4), { y: 180, height: 60 })
  assert.equal(getNoteWindow(note, 5).y + getNoteWindow(note, 5).height, rollHeight)
  assert.equal(getNoteWindow(note, 6), null)
  assert.equal(isNoteActive(note, 3.99, true), false)
  assert.equal(isNoteActive(note, 4, true), true)
  assert.equal(isNoteActive(note, 5, false), false)
  assert.equal(isNoteActive(note, 6, true), false)
  assert.deepEqual(getNoteWindow(note, 0), { y: 60, height: 60 })
  assert.deepEqual(getNoteWindow({ startBeat: 0, durationBeats: 20 }, 1), {
    y: 0,
    height: rollHeight
  })
})

test('grid uses denominator pulses and numerator bar boundaries in quarter-note time', () => {
  const grid = getBeatGrid(0, 6, 8, 2)
  assert.equal(grid[0].label, '1.1')
  assert.equal(grid[1].y, rollHeight - 15)
  assert.equal(grid[6].label, '2.1')
  assert.equal(grid[6].isBar, true)
  assert.equal(grid[5].isBar, false)
  assert.equal(grid.at(-1).pulse, 12)
  assert.equal(getBeatGrid(0.25, 3, 4, 2)[0].pulse, 1)
  assert.deepEqual(getBeatGrid(20, 4, 4, 1), [])
})
