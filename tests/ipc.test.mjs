import assert from 'node:assert/strict'
import test from 'node:test'
import { assertLessonId, assertTrustedSender } from '../src/main/ipc.ts'

test('IPC only accepts the application main frame and valid lesson identifiers', () => {
  const pageUrl = 'file:///app/out/renderer/index.html'
  const frame = { url: `${pageUrl}#/lessons/lesson-rhythm-004` }
  const event = { senderFrame: frame, sender: { mainFrame: frame } }
  assert.doesNotThrow(() => assertTrustedSender(event, pageUrl))
  assert.doesNotThrow(() => assertLessonId('lesson-rhythm-004'))

  for (const value of [null, {}, ['lesson-rhythm-004'], '../file', 'lesson-rhythm-004?stage=1']) {
    assert.throws(() => assertLessonId(value), /Invalid lesson ID/)
  }

  assert.throws(
    () => assertTrustedSender({ ...event, senderFrame: { ...frame } }, pageUrl),
    /Untrusted/
  )
  frame.url = 'https://example.com/'
  assert.throws(() => assertTrustedSender(event, pageUrl), /Untrusted/)
})
