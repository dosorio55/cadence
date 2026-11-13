import { Link } from 'react-router-dom'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'
import type { CurriculumLibrary } from '../../../shared/api'

export default function Home({ categories }: { categories: CurriculumLibrary }) {
  const lessonCount = categories.reduce((count, category) => count + category.lessons.length, 0)

  return (
    <main className="w-full flex-1 px-4 py-8 sm:px-6 lg:px-8">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <h1 className="font-display text-title font-semibold">Biblioteca de lecciones</h1>
        <p className="text-caption text-muted-foreground">
          {categories.length} categorías · {lessonCount} lecciones
        </p>
      </div>

      <nav aria-label="Categorías" className="mt-5 flex flex-wrap gap-2">
        {categories.map((category) => (
          <Button
            key={category.id}
            variant="outline"
            onClick={() => document.getElementById(category.slug)?.scrollIntoView()}
          >
            {category.name}
          </Button>
        ))}
      </nav>

      <div className="mt-8 space-y-10">
        {categories.map((category) => (
          <section
            key={category.id}
            id={category.slug}
            aria-labelledby={`${category.id}-heading`}
            className="scroll-mt-24"
          >
            <div className="mb-4 flex flex-wrap items-end justify-between gap-2">
              <div>
                <h2 id={`${category.id}-heading`} className="font-display text-title font-semibold">
                  {category.name}
                </h2>
                <p className="mt-1 text-body text-muted-foreground">{category.description}</p>
              </div>
              <p className="text-caption text-muted-foreground">
                {category.lessons.length} lecciones
              </p>
            </div>

            <ol className="grid gap-4 md:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-4">
              {category.lessons.map((lesson) => (
                <li key={lesson.id} className="min-w-0">
                  <Link to={lesson.href} className="block h-full">
                    <Card className="h-full hover:ring-primary">
                      <CardHeader>
                        <div className="flex flex-wrap items-center justify-between gap-2 text-caption text-muted-foreground">
                          <span className="font-mono">Lección {lesson.orderInCategory}</span>
                          <span>{lesson.targetMinutes} min</span>
                        </div>
                        <CardTitle>
                          <h3 className="font-display text-title font-semibold">{lesson.title}</h3>
                        </CardTitle>
                      </CardHeader>
                      <CardContent>
                        <p className="text-body text-muted-foreground">{lesson.goal}</p>
                      </CardContent>
                      <CardFooter className="mt-auto block">
                        <p className="text-caption text-muted-foreground">
                          Habilidad: {lesson.skill.name}
                        </p>
                        <div className="mt-3 flex flex-wrap items-center justify-between gap-2 text-caption">
                          <Badge variant="outline">Dificultad {lesson.difficulty}/5</Badge>
                          <span className="font-semibold text-primary">
                            Abrir lección <span aria-hidden="true">→</span>
                          </span>
                        </div>
                      </CardFooter>
                    </Card>
                  </Link>
                </li>
              ))}
            </ol>
          </section>
        ))}
      </div>
    </main>
  )
}
