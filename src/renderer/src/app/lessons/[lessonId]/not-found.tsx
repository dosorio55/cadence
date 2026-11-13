import { Link } from 'react-router-dom'
import { Button } from '@/components/ui/button'

export default function LessonNotFound() {
  return (
    <main className="mx-auto w-full max-w-3xl px-6 py-20">
      <p className="font-mono text-label uppercase tracking-widest text-primary">
        Lección no disponible
      </p>
      <h1 className="mt-4 font-display text-heading font-semibold">Volvamos al piano.</h1>
      <p className="mt-5 text-body text-muted-foreground">
        No encontramos esta lección. Elige una de las lecciones disponibles en la biblioteca.
      </p>
      <Button className="mt-6" render={<Link to="/" />} nativeButton={false}>
        Volver a la biblioteca
      </Button>
    </main>
  )
}
