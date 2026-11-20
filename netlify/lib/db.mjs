import { getDatabase } from '@netlify/database';

export function db() {
  return getDatabase(process.env.NETLIFY_DB_URL ? { connectionString: process.env.NETLIFY_DB_URL } : undefined).sql;
}
