import { app, shell, BrowserWindow, ipcMain, dialog } from 'electron'
import { basename, join } from 'node:path'
import { stat } from 'node:fs/promises'
import { pathToFileURL } from 'node:url'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'
import { getLesson } from './curriculum'
import { getCurriculumLibrary } from './curriculum-library'
import { openDatabase } from './db'
import { assertLessonId, assertTrustedSender } from './ipc'
import icon from '../../resources/icon.png?asset'
import { ChordWorker } from './chord-worker'

const pageUrl =
  is.dev && process.env['ELECTRON_RENDERER_URL']
    ? process.env['ELECTRON_RENDERER_URL']
    : pathToFileURL(join(__dirname, '../renderer/index.html')).href

let database: ReturnType<typeof openDatabase> | undefined
let selectingAudio = false

const pythonRoot = join(app.getAppPath(), 'python')
const chordWorker = new ChordWorker(
  app.isPackaged
    ? {
        executable: join(
          process.resourcesPath,
          'chord-worker',
          process.platform === 'win32' ? 'chord-worker.exe' : 'chord-worker'
        )
      }
    : {
        executable: join(
          pythonRoot,
          '.venv',
          process.platform === 'win32' ? 'Scripts/python.exe' : 'bin/python'
        ),
        args: ['-u', join(pythonRoot, 'worker.py')]
      }
)

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

    ipcMain.handle('chords:analyze', async (event) => {
      assertTrustedSender(event, pageUrl)
      if (selectingAudio) throw new Error('Ya hay una selección o un análisis en curso.')

      const window = BrowserWindow.fromWebContents(event.sender)
      if (!window) throw new Error('No se encontró la ventana de Cadence.')

      selectingAudio = true

      try {
        const selection = await dialog.showOpenDialog(window, {
          title: 'Seleccionar audio para analizar acordes',
          properties: ['openFile'],
          filters: [{ name: 'Audio', extensions: ['wav', 'flac', 'ogg'] }]
        })

        if (selection.canceled || !selection.filePaths[0]) return null
        assertTrustedSender(event, pageUrl)

        const path = selection.filePaths[0]
        const file = await stat(path)

        if (!file.isFile() || file.size > 200 * 1024 * 1024) {
          throw new Error('Selecciona un archivo de audio de máximo 200 MB.')
        }

        const chords = await chordWorker.analyze(path)
        return { fileName: basename(path), chords }
      } finally {
        selectingAudio = false
      }
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

app.on('before-quit', () => chordWorker.dispose())
app.on('will-quit', () => database?.close())

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
