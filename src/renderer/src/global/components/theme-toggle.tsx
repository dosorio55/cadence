'use client'

import { useSyncExternalStore } from 'react'
import { ToggleGroup, ToggleGroupItem } from '@/components/ui/toggle-group'
import { getThemeSnapshot, setTheme } from '@/lib/theme'

function subscribe(onChange: () => void) {
  const observer = new MutationObserver(onChange)
  observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['data-theme']
  })

  return () => observer.disconnect()
}

function getServerSnapshot() {
  return 'light' as const
}

export function ThemeToggle() {
  const theme = useSyncExternalStore(subscribe, getThemeSnapshot, getServerSnapshot)

  return (
    <ToggleGroup
      aria-label="Tema de la interfaz"
      variant="outline"
      spacing={0}
      value={[theme]}
      onValueChange={(values) => {
        const value = values[0]

        if (value === 'light' || value === 'dark') {
          setTheme(value)
        }
      }}
    >
      {(
        [
          ['light', 'Claro'],
          ['dark', 'Oscuro']
        ] as const
      ).map(([value, label]) => (
        <ToggleGroupItem key={value} value={value} aria-label={label}>
          {label}
        </ToggleGroupItem>
      ))}
    </ToggleGroup>
  )
}
