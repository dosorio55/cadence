import { app, shell, BrowserWindow, ipcMain, dialog } from 'electron'
import { join } from 'node:path'
import { pathToFileURL } from 'node:url'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'
import { getLesson } from './curriculum'
import { getCurriculumLibrary } from './curriculum-library'
import { openDatabase } from './db'
import { assertLessonId, assertTrustedSender } from './ipc'
import icon from '../../resources/icon.png?asset'

const pageUrl =
  is.dev && process.env['ELECTRON_RENDERER_URL']
    ? process.env['ELECTRON_RENDERER_URL']
    : pathToFileURL(join(__dirname, '../renderer/index.html')).href

let database: ReturnType<typeof openDatabase> | undefined

function createWindow(): void {
  const window = new BrowserWindow({
    width: 1440,
    height: 960,
    show: false,
    autoHideMenuBar: true,
    ...(process.platform === 'linux' ? { icon } : {}),
    webPreferences: {
      preload: join(__dirname, '../preload/index.js'),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true
    }
  })

  window.on('ready-to-show', () => window.show())

  window.webContents.setWindowOpenHandler(({ url }) => {
    if (['https:', 'http:'].includes(new URL(url).protocol)) {
      void shell.openExternal(url)
    }

    return { action: 'deny' }
  })

  window.webContents.on('will-navigate', (event, url) => {
    if (url.split('#')[0] !== pageUrl.split('#')[0]) {
      event.preventDefault()
    }
  })

  void window.loadURL(pageUrl)
}

app
  .whenReady()
  .then(() => {
    electronApp.setAppUserModelId('com.cadence.studio')
    app.setName('Cadence')
    database = openDatabase(join(app.getPath('userData'), 'cadence.sqlite'))

    ipcMain.handle('curriculum:library', (event) => {
      assertTrustedSender(event, pageUrl)
      return getCurriculumLibrary()
    })

    ipcMain.handle('curriculum:lesson', (event, lessonId: unknown) => {
      assertTrustedSender(event, pageUrl)
      assertLessonId(lessonId)
      return getLesson(lessonId)
    })

    app.on('browser-window-created', (_, window) => optimizer.watchWindowShortcuts(window))
    createWindow()

    app.on('activate', () => {
      if (BrowserWindow.getAllWindows().length === 0) {
        createWindow()
      }
    })
  })
  .catch((error: unknown) => {
    dialog.showErrorBox(
      'Cadence no pudo iniciar',
      error instanceof Error ? error.message : String(error)
    )
    app.quit()
  })

app.on('will-quit', () => database?.close())

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
