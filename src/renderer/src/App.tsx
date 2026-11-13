import { useCallback } from 'react'
import { HashRouter, Route, Routes, useParams, useSearchParams } from 'react-router-dom'
import Home from './app/page'
import AnalyzePage from './app/analyze/page'
import LessonPage from './app/lessons/[lessonId]/page'
import LessonLoading from './app/lessons/[lessonId]/loading'
import LessonNotFound from './app/lessons/[lessonId]/not-found'
import { AppHeader } from './global/components/app-header'
import { LoadError } from './global/components/load-error'
import { useApiData } from './lib/use-api-data'

const loadLibrary = () => window.api.getCurriculumLibrary()

function HomeRoute() {
  const { state, retry } = useApiData(loadLibrary)

  if (state.status === 'loading') {
    return (
      <main className="w-full flex-1 px-4 py-8 sm:px-6 lg:px-8">
        <p role="status" className="font-mono text-body text-muted-foreground">
          Preparando la biblioteca…
        </p>
      </main>
    )
  }

  if (state.status === 'error') {
    return <LoadError retry={retry} />
  }

  return <Home categories={state.data} />
}

function LessonLoader({ lessonId }: { lessonId: string }) {
  const loadLesson = useCallback(() => window.api.getLesson(lessonId), [lessonId])
  const { state, retry } = useApiData(loadLesson)
  const [searchParams] = useSearchParams()

  if (state.status === 'loading') {
    return <LessonLoading />
  }

  if (state.status === 'error') {
    return <LoadError retry={retry} />
  }

  if (!state.data) {
    return <LessonNotFound />
  }

  const queryValue = (name: string) => {
    const values = searchParams.getAll(name)
    return values.length > 1 ? values : values[0]
  }

  return (
    <LessonPage
      lesson={state.data}
      query={{ stage: queryValue('stage'), example: queryValue('example') }}
    />
  )
}

function LessonRoute() {
  const { lessonId = '' } = useParams()

  if (!/^lesson-[a-z]+-\d{3}$/.test(lessonId)) {
    return <LessonNotFound />
  }

  return <LessonLoader key={lessonId} lessonId={lessonId} />
}

export default function App() {
  return (
    <HashRouter>
      <AppHeader />
      <Routes>
        <Route path="/" element={<HomeRoute />} />
        <Route path="/analyze" element={<AnalyzePage />} />
        <Route path="/lessons/:lessonId" element={<LessonRoute />} />
        <Route path="*" element={<LessonNotFound />} />
      </Routes>
    </HashRouter>
  )
}
