import type { getLesson } from '../main/curriculum'
import type { getCurriculumLibrary } from '../main/curriculum-library'

export type Lesson = NonNullable<ReturnType<typeof getLesson>>
export type CurriculumLibrary = ReturnType<typeof getCurriculumLibrary>

export interface CadenceAPI {
  getCurriculumLibrary(): Promise<CurriculumLibrary>
  getLesson(lessonId: string): Promise<Lesson | null>
}
