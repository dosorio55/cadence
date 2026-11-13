import type { Lesson } from '../../../../../shared/api'

export type Stage = Lesson['stages'][number]
export type Progression = Stage['progressions'][number]
