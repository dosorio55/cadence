import { Link } from 'react-router-dom'
import { ThemeToggle } from './theme-toggle'

export function AppHeader() {
  return (
    <header className="border-b border-border bg-surface">
      <div className="flex w-full flex-wrap items-center justify-between gap-4 px-4 py-3 sm:px-6">
        <Link to="/" className="flex items-center gap-3" aria-label="Cadence, inicio">
          <span
            className="rounded-control bg-primary px-3 py-2 font-display text-title font-semibold text-primary-foreground"
            aria-hidden="true"
          >
            c.
          </span>
          <span className="font-display text-title font-semibold tracking-tight">
            cadence
            <span className="ml-3 hidden font-mono text-label font-normal uppercase tracking-widest text-muted-foreground sm:inline">
              Piano practice studio
            </span>
          </span>
        </Link>
        <ThemeToggle />
      </div>
    </header>
  )
}
