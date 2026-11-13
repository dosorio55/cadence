import assert from 'node:assert/strict'
import test from 'node:test'
import {
  getThemeSnapshot,
  initializeTheme,
  setTheme,
  themeStorageKey
} from '../src/renderer/src/lib/theme.ts'

function mockGlobals(t, document, window) {
  for (const [name, value] of Object.entries({ document, window })) {
    const descriptor = Object.getOwnPropertyDescriptor(globalThis, name)
    t.after(() => {
      if (descriptor) {
        Object.defineProperty(globalThis, name, descriptor)
      } else {
        Reflect.deleteProperty(globalThis, name)
      }
    })
    Object.defineProperty(globalThis, name, { configurable: true, value })
  }
}

test('initial theme respects saved choices and safely falls back to the system', (t) => {
  const cases = [
    { saved: 'light', prefersDark: true, expected: 'light' },
    { saved: 'dark', prefersDark: false, expected: 'dark' },
    { saved: null, prefersDark: true, expected: 'dark' },
    { saved: null, prefersDark: false, expected: 'light' },
    { saved: 'invalid', prefersDark: true, expected: 'dark' },
    { saved: 'invalid', prefersDark: false, expected: 'light' },
    { blocked: true, prefersDark: true, expected: 'dark' },
    { blocked: true, prefersDark: false, expected: 'light' }
  ]

  const document = { documentElement: { dataset: {} } }
  let current
  const window = {
    get localStorage() {
      if (current.blocked) {
        throw new Error('Storage blocked')
      }

      return {
        getItem(key) {
          assert.equal(key, themeStorageKey)
          return current.saved
        }
      }
    },
    matchMedia(query) {
      assert.equal(query, '(prefers-color-scheme: dark)')
      return { matches: current.prefersDark }
    }
  }
  mockGlobals(t, document, window)

  for (current of cases) {
    initializeTheme()
    assert.equal(getThemeSnapshot(), current.expected)
  }
})

test('theme switching persists when possible and still works with blocked storage', (t) => {
  const document = { documentElement: { dataset: {} } }
  const stored = new Map()
  const window = {
    localStorage: {
      setItem: (key, value) => stored.set(key, value),
      getItem: (key) => stored.get(key)
    }
  }
  mockGlobals(t, document, window)

  for (const theme of ['dark', 'light']) {
    setTheme(theme)
    assert.equal(getThemeSnapshot(), theme)
    assert.equal(stored.get(themeStorageKey), theme)

    document.documentElement.dataset.theme = undefined
    initializeTheme()
    assert.equal(getThemeSnapshot(), theme)
  }

  Object.defineProperty(window, 'localStorage', {
    get() {
      throw new Error('Storage blocked')
    }
  })

  setTheme('dark')
  assert.equal(getThemeSnapshot(), 'dark')
})
