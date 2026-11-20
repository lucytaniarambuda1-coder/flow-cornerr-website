// Admin: list, create, update and delete jobs. Requires the signed-in admin.
import { db } from '../lib/db.mjs';
import { json } from '../lib/http.mjs';
import { requireAdmin } from '../lib/auth.mjs';
import { cleanJob, parseId } from '../lib/validate.mjs';

const BASE = '/api/admin/jobs';
const shape = (r) => ({
  id: r.id, title: r.title, org: r.org, type: r.type, province: r.province,
  description: r.description, url: r.url, cta: r.cta || '', tags: r.tags || [],
  closing: r.closing ? new Date(r.closing).toISOString().slice(0, 10) : '',
  status: r.status, created_at: r.created_at, updated_at: r.updated_at,
});

export default async (req) => {
  const gate = await requireAdmin(req);
  if (gate.error) return gate.error;
  const sql = db();
  const id = parseId(new URL(req.url).pathname, BASE);
  if (Number.isNaN(id)) return json({ error: 'Bad id.' }, 400);

  try {
    if (req.method === 'GET') {
      const rows = await sql`select * from jobs order by (status = 'published') desc, closing asc nulls last, id desc`;
      return json({ items: rows.map(shape) });
    }
    if (req.method === 'POST' && id === null) {
      const r = cleanJob(await req.json().catch(() => null));
      if (!r.ok) return json({ errors: r.errors }, 422);
      const j = r.value;
      const rows = await sql`
        insert into jobs (title, org, type, province, description, url, cta, tags, closing, status)
        values (${j.title}, ${j.org}, ${j.type}, ${j.province}, ${j.description}, ${j.url}, ${j.cta}, ${j.tags}, ${j.closing}, ${j.status})
        returning *`;
      return json({ item: shape(rows[0]) }, 201);
    }
    if (req.method === 'PUT' && id !== null) {
      const r = cleanJob(await req.json().catch(() => null));
      if (!r.ok) return json({ errors: r.errors }, 422);
      const j = r.value;
      const rows = await sql`
        update jobs set title = ${j.title}, org = ${j.org}, type = ${j.type}, province = ${j.province},
          description = ${j.description}, url = ${j.url}, cta = ${j.cta}, tags = ${j.tags},
          closing = ${j.closing}, status = ${j.status}, updated_at = now()
        where id = ${id} returning *`;
      return rows.length ? json({ item: shape(rows[0]) }) : json({ error: 'Not found.' }, 404);
    }
    if (req.method === 'DELETE' && id !== null) {
      const rows = await sql`delete from jobs where id = ${id} returning id`;
      return rows.length ? json({ ok: true }) : json({ error: 'Not found.' }, 404);
    }
    return json({ error: 'Not allowed.' }, 405);
  } catch (err) {
    console.error('admin-jobs error', err?.message);
    return json({ error: 'Something went wrong. Please try again.' }, 500);
  }
};

export const config = { path: [BASE, BASE + '/*'] };
