import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: 'sqlite',
  schema: './src/main/db/schema.ts',
  out: './drizzle',
  dbCredentials: {
    url: process.env.CADENCE_DB_PATH ?? './cadence.dev.sqlite'
  }
})
