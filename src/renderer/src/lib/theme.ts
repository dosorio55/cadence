export type Theme = 'light' | 'dark'

export const themeStorageKey = 'cadence:theme'

export function initializeTheme() {
  let saved

  try {
    saved = window.localStorage.getItem(themeStorageKey)
  } catch {
    // Blocked storage must not prevent applying the system theme.
  }

  document.documentElement.dataset.theme =
    saved === 'light' || saved === 'dark'
      ? saved
      : window.matchMedia('(prefers-color-scheme: dark)').matches
        ? 'dark'
        : 'light'
}

export function getThemeSnapshot(): Theme {
  return document.documentElement.dataset.theme === 'dark' ? 'dark' : 'light'
}

export function setTheme(theme: Theme) {
  document.documentElement.dataset.theme = theme

  try {
    window.localStorage.setItem(themeStorageKey, theme)
  } catch {
    // The choice still applies for this session when storage is blocked.
  }
}
