import { useCallback, useEffect, useRef, useState } from 'react'
import type { Progression } from '../../types'
import { LessonAudioEngine } from './audio-engine'
import { loadPianoSamples } from './piano-samples'
import { getTiming } from './playback-plan'

type PlaybackStatus = 'stopped' | 'loading' | 'playing' | 'paused' | 'error'

export function useLessonPlayback(progression: Progression) {
  const engine = useRef<LessonAudioEngine | null>(null)
  const request = useRef(0)
  const active = useRef(false)
  const [status, setStatus] = useState<PlaybackStatus>('stopped')
  const [beat, setBeat] = useState(0)
  const [sounding, setSounding] = useState(false)
  const [tempo, setTempo] = useState(progression.bpm)
  const [loop, setLoop] = useState(false)
  const [metronome, setMetronome] = useState(false)
  const [clickVolume, setClickVolume] = useState(0.25)
  const [error, setError] = useState('')

  async function play() {
    const currentRequest = ++request.current
    active.current = true
    setStatus('loading')
    setError('')

    try {
      if (!engine.current) {
        const tone = await import('tone')

        if (request.current !== currentRequest) {
          return
        }

        engine.current = new LessonAudioEngine(tone, progression, loadPianoSamples)
        engine.current.setTempo(tempo)
        engine.current.setLoop(loop)
        engine.current.setMetronome(metronome, clickVolume)
      }

      const started = await engine.current.play()

      if (request.current === currentRequest && started) {
        setStatus('playing')
      }
    } catch {
      if (request.current === currentRequest) {
        engine.current?.stop()
        setBeat(0)
        setSounding(false)
        setError('No se pudo iniciar el piano. Comprueba la salida de audio e inténtalo de nuevo.')
        active.current = false
        setStatus('error')
      }
    }
  }

  const cancelRequest = useCallback(() => {
    request.current++
    active.current = false
  }, [])

  const pause = useCallback(() => {
    cancelRequest()
    engine.current?.pause()
    setBeat(engine.current?.getBeat() ?? 0)
    setSounding(false)
    setStatus('paused')
  }, [cancelRequest])

  function stop() {
    cancelRequest()
    engine.current?.stop()
    setBeat(0)
    setSounding(false)
    setStatus('stopped')
    setError('')
  }

  function changeTempo(value: number) {
    if (!Number.isFinite(value) || value < 40 || value > 180) {
      return
    }

    stop()
    engine.current?.setTempo(value)
    setTempo(value)
  }

  function changeLoop(value: boolean) {
    setLoop(value)
    engine.current?.setLoop(value)
  }

  function changeMetronome(value: boolean) {
    setMetronome(value)
    engine.current?.setMetronome(value, clickVolume)
  }

  function changeClickVolume(value: number) {
    setClickVolume(value)
    engine.current?.setMetronome(metronome, value)
  }

  useEffect(() => {
    function onVisibilityChange() {
      if (document.hidden && active.current) {
        pause()
      }
    }

    document.addEventListener('visibilitychange', onVisibilityChange)
    function onPageHide() {
      if (active.current) {
        pause()
      }
    }

    window.addEventListener('pagehide', onPageHide)

    return () => {
      cancelRequest()
      document.removeEventListener('visibilitychange', onVisibilityChange)
      window.removeEventListener('pagehide', onPageHide)
      engine.current?.dispose()
      engine.current = null
    }
  }, [pause, cancelRequest])

  useEffect(() => {
    if (status !== 'playing') {
      return
    }

    let frame = 0

    function update() {
      const audio = engine.current

      if (!audio) {
        return
      }

      if (audio.interrupted) {
        pause()
        return
      }

      const currentBeat = audio.getBeat()
      setBeat(currentBeat)
      setSounding(audio.audible)

      if (!loop && currentBeat >= getTiming(progression).totalBeats) {
        audio.stop(true)
        active.current = false
        setSounding(false)
        setStatus('stopped')
        return
      }

      frame = requestAnimationFrame(update)
    }

    frame = requestAnimationFrame(update)
    return () => cancelAnimationFrame(frame)
  }, [status, progression, loop, pause])

  return {
    status,
    beat,
    sounding,
    tempo,
    loop,
    metronome,
    clickVolume,
    error,
    play,
    pause,
    stop,
    changeTempo,
    changeLoop,
    changeMetronome,
    changeClickVolume
  }
}
