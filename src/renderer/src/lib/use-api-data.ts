import { useEffect, useState } from 'react'

type LoadState<T> = { status: 'loading' } | { status: 'ready'; data: T } | { status: 'error' }

export function useApiData<T>(load: () => Promise<T>) {
  const [state, setState] = useState<LoadState<T>>({ status: 'loading' })
  const [attempt, setAttempt] = useState(0)

  useEffect(() => {
    let active = true

    async function fetchData() {
      try {
        const data = await load()

        if (active) {
          setState({ status: 'ready', data })
        }
      } catch {
        if (active) {
          setState({ status: 'error' })
        }
      }
    }

    void fetchData()

    return () => {
      active = false
    }
  }, [load, attempt])

  function retry() {
    setState({ status: 'loading' })
    setAttempt((value) => value + 1)
  }

  return { state, retry }
}
