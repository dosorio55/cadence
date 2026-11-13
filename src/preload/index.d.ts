import type { CadenceAPI } from '../shared/api'

declare global {
  interface Window {
    api: CadenceAPI
  }
}
