// Public: published, not-yet-closed jobs for /opportunities/.
import { db } from '../lib/db.mjs';
import { json } from '../lib/http.mjs';

export default async () => {
  try {
    const sql = db();
    const rows = await sql`
      select id, title, org, type, province, description, url, cta, tags, closing
      from jobs
      where status = 'published' and (closing is null or closing >= current_date)
      order by closing asc nulls last, id desc`;
    const items = rows.map((r) => ({
      id: r.id, title: r.title, org: r.org, type: r.type, province: r.province,
      desc: r.description, url: r.url, cta: r.cta || '', tags: r.tags || [],
      closing: r.closing ? new Date(r.closing).toISOString().slice(0, 10) : '',
    }));
    return json({ items }, 200, { 'Cache-Control': 'public, max-age=60, stale-while-revalidate=300' });
  } catch (err) {
    console.error('jobs: database error', err?.message);
    return json({ items: [], error: 'unavailable' }, 503);
  }
};

export const config = { path: '/api/jobs' };
