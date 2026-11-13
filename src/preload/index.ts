import { contextBridge, ipcRenderer } from 'electron'
import type { CadenceAPI } from '../shared/api'

const api: CadenceAPI = {
  analyzeAudio: () => ipcRenderer.invoke('chords:analyze'),
  getCurriculumLibrary: () => ipcRenderer.invoke('curriculum:library'),
  getLesson: (lessonId) => ipcRenderer.invoke('curriculum:lesson', lessonId)
}

contextBridge.exposeInMainWorld('api', api)
