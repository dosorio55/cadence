import type { IpcMainInvokeEvent } from 'electron'

export function assertTrustedSender(event: IpcMainInvokeEvent, pageUrl: string): void {
  const senderUrl = new URL(event.senderFrame?.url ?? 'about:blank')
  const expectedUrl = new URL(pageUrl)
  senderUrl.hash = ''
  expectedUrl.hash = ''

  if (event.senderFrame !== event.sender.mainFrame || senderUrl.href !== expectedUrl.href) {
    throw new Error('Untrusted IPC sender')
  }
}

export function assertLessonId(value: unknown): asserts value is string {
  if (typeof value !== 'string' || !/^lesson-[a-z]+-\d{3}$/.test(value)) {
    throw new Error('Invalid lesson ID')
  }
}
