import { useId, useMemo } from 'react'
import type { Progression } from '../../types'
import {
  getBeatGrid,
  getKeyboard,
  getNoteWindow,
  isNoteActive,
  pitchName,
  rollHeight,
  visibleBeats
} from './piano-geometry'

const handRoles = {
  right: {
    fill: 'var(--primary)',
    foreground: 'var(--primary-foreground)',
    label: 'Mano derecha'
  },
  left: {
    fill: 'var(--secondary)',
    foreground: 'var(--secondary-foreground)',
    label: 'Mano izquierda'
  },
  either: {
    fill: 'var(--muted)',
    foreground: 'var(--muted-foreground)',
    label: 'Cualquier mano'
  }
}

function handRole(hand: string) {
  return handRoles[hand as keyof typeof handRoles] ?? handRoles.either
}

export function PianoVisuals({
  progression,
  beat,
  sounding
}: {
  progression: Progression
  beat: number
  sounding: boolean
}) {
  const id = useId()
  const { keys, width } = useMemo(
    () => getKeyboard(progression.notes.map((note) => note.midi)),
    [progression.notes]
  )
  const keysByPitch = useMemo(() => new Map(keys.map((key) => [key.midi, key])), [keys])
  const activeNotes = progression.notes.filter((note) => isNoteActive(note, beat, sounding))
  const activePitches = [...new Set(activeNotes.map((note) => note.midi))].sort((a, b) => a - b)
  const grid = getBeatGrid(
    beat,
    progression.timeSignature.numerator,
    progression.timeSignature.denominator,
    progression.totalBars
  )

  return (
    <section aria-label="Piano roll y teclado" className="space-y-3">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <h2 className="text-body font-semibold">Piano roll</h2>
        <ul aria-label="Leyenda de manos" className="flex flex-wrap gap-4 text-caption">
          {Object.entries(handRoles).map(([hand, role]) => (
            <li key={hand} className="flex items-center gap-2">
              <span
                aria-hidden="true"
                className="size-3 rounded-control border border-border"
                style={{ background: role.fill }}
              />
              {role.label}
            </li>
          ))}
        </ul>
      </div>
      <div
        className="overflow-x-auto rounded-panel border border-border bg-surface focus-visible:outline-ring"
        role="region"
        aria-label="Teclado completo; desplázate horizontalmente para ver los extremos"
        tabIndex={0}
      >
        <svg
          role="img"
          aria-labelledby={`${id}-title ${id}-description`}
          viewBox={`0 0 ${width} ${rollHeight + 100}`}
          className="block w-full"
          style={{ minWidth: width }}
        >
          <title id={`${id}-title`}>Piano roll: {progression.title}</title>
          <desc id={`${id}-description`}>
            Las notas descienden hacia el teclado. Su altura representa la duración en negras. La
            línea inferior marca el instante de reproducción. Ventana de {visibleBeats} negras;
            cuadrícula de compases y pulsos en {progression.timeSignature.numerator}/
            {progression.timeSignature.denominator}. Derecha: color primario; izquierda: secundario;
            cualquier mano: neutro. El teclado solo se ilumina mientras suena el ejemplo.
          </desc>
          <rect width={width} height={rollHeight} fill="var(--surface)" />
          {keys.map((key) => (
            <line
              key={key.midi}
              x1={key.x + key.width / 2}
              x2={key.x + key.width / 2}
              y1={0}
              y2={rollHeight}
              stroke="var(--border)"
              strokeOpacity={key.black ? 0.3 : 0.6}
            />
          ))}
          {grid.map((line) => (
            <g key={line.pulse}>
              <line
                x1={0}
                x2={width}
                y1={line.y}
                y2={line.y}
                stroke={line.isBar ? 'var(--muted-foreground)' : 'var(--border)'}
                strokeDasharray={line.isBar ? undefined : '3 5'}
              />
              {line.y >= 15 && (
                <text
                  x={5}
                  y={line.y - 4}
                  fill="var(--muted-foreground)"
                  className="font-mono text-label"
                >
                  {line.label}
                </text>
              )}
            </g>
          ))}
          {progression.notes.map((note) => {
            const window = getNoteWindow(note, beat)
            const key = keysByPitch.get(note.midi)

            if (!window || !key) {
              return null
            }

            return (
              <rect
                key={note.id}
                x={key.x + 2}
                y={window.y}
                width={key.width - 4}
                height={window.height}
                fill={handRole(note.hand).fill}
                stroke="var(--muted-foreground)"
                strokeWidth={isNoteActive(note, beat, sounding) ? 2 : 0.5}
                style={{ rx: 'var(--radius-control)' }}
              />
            )
          })}
          {[...keys.filter((key) => !key.black), ...keys.filter((key) => key.black)].map((key) => {
            const active = activeNotes.find((note) => note.midi === key.midi)

            return (
              <g key={key.midi}>
                <rect
                  x={key.x}
                  y={rollHeight}
                  width={key.width}
                  height={key.black ? 62 : 98}
                  fill={
                    active
                      ? handRole(active.hand).fill
                      : key.black
                        ? 'var(--piano-black)'
                        : 'var(--piano-white)'
                  }
                  stroke="var(--border)"
                  style={{ rx: 'var(--radius-control)' }}
                />
                {key.midi % 12 === 0 && (
                  <text
                    x={key.x + key.width / 2}
                    y={rollHeight + 86}
                    textAnchor="middle"
                    fill={active ? handRole(active.hand).foreground : 'var(--piano-key-label)'}
                    className="font-mono text-label"
                  >
                    {pitchName(key.midi)}
                  </text>
                )}
              </g>
            )
          })}
          <line
            x1={0}
            x2={width}
            y1={rollHeight}
            y2={rollHeight}
            stroke="var(--primary)"
            strokeWidth={2}
          />
        </svg>
      </div>
      <p className="font-mono text-caption text-muted-foreground" aria-live="off">
        Notas activas: {activePitches.length ? activePitches.map(pitchName).join(' · ') : 'ninguna'}
      </p>
    </section>
  )
}
