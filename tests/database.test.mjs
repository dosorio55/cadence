import assert from 'node:assert/strict'
import { mkdtempSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import test from 'node:test'
import { sql } from 'drizzle-orm'
import { openDatabase } from '../src/main/db/index.ts'

test('local SQLite persists across reopen and enables integrity settings', () => {
  const directory = mkdtempSync(join(tmpdir(), 'cadence-db-'))
  let connection

  try {
    const filename = join(directory, 'cadence.sqlite')
    connection = openDatabase(filename)
    assert.equal(connection.db.get(sql`PRAGMA foreign_keys`).foreign_keys, 1)
    assert.equal(connection.db.get(sql`PRAGMA journal_mode`).journal_mode, 'wal')
    connection.db.run(sql`CREATE TABLE persistence_check (value TEXT NOT NULL)`)
    connection.db.run(sql`INSERT INTO persistence_check VALUES ('retained')`)
    connection.close()
    connection = openDatabase(filename)
    assert.deepEqual(connection.db.all(sql`SELECT value FROM persistence_check`), [
      { value: 'retained' }
    ])
    assert.equal(connection.db.get(sql`PRAGMA integrity_check`).integrity_check, 'ok')
  } finally {
    connection?.close()
    rmSync(directory, { recursive: true, force: true })
  }
})
