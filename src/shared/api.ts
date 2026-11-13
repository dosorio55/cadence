import type { getLesson } from '../main/curriculum'
import type { getCurriculumLibrary } from '../main/curriculum-library'

export type Lesson = NonNullable<ReturnType<typeof getLesson>>
export type CurriculumLibrary = ReturnType<typeof getCurriculumLibrary>

export interface ChordSegment {
  start_time: number
  end_time: number
  chord: string
}

export interface AudioAnalysis {
  fileName: string
  chords: ChordSegment[]
}

export interface CadenceAPI {
  analyzeAudio(): Promise<AudioAnalysis | null>
  getCurriculumLibrary(): Promise<CurriculumLibrary>
  getLesson(lessonId: string): Promise<Lesson | null>
}
