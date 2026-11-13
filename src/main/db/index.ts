import Database from 'better-sqlite3'
import { drizzle } from 'drizzle-orm/better-sqlite3'
import * as schema from './schema.ts'

export function openDatabase(filename: string) {
  const client = new Database(filename)

  try {
    client.pragma('journal_mode = WAL')
    client.pragma('foreign_keys = ON')

    return { db: drizzle(client, { schema }), close: () => client.close() }
  } catch (error) {
    client.close()
    throw error
  }
}
