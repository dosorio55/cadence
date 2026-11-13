export function LessonText({ text }: { text: string }) {
  return (
    <p className="whitespace-pre-line text-body leading-relaxed text-muted-foreground">
      {text.split(/(\*\*[^*]+\*\*)/g).map((part) =>
        part.startsWith('**') && part.endsWith('**') ? (
          <strong key={part} className="font-semibold text-foreground">
            {part.slice(2, -2)}
          </strong>
        ) : (
          part
        )
      )}
    </p>
  )
}
