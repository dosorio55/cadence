import { Button } from '@/components/ui/button'

export function LoadError({ retry }: { retry: () => void }) {
  return (
    <main className="mx-auto w-full max-w-3xl px-6 py-12">
      <p role="alert" className="text-body text-muted-foreground">
        No pudimos cargar el contenido. Inténtalo de nuevo.
      </p>
      <Button className="mt-4" onClick={retry}>
        Reintentar
      </Button>
    </main>
  )
}
