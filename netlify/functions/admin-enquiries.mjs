// Admin: read employer enquiries and mark them contacted/closed. Requires the signed-in admin.
import { db } from '../lib/db.mjs';
import { json } from '../lib/http.mjs';
import { requireAdmin } from '../lib/auth.mjs';
import { ENQUIRY_STATUSES, parseId } from '../lib/validate.mjs';

const BASE = '/api/admin/enquiries';

export default async (req) => {
  const gate = await requireAdmin(req);
  if (gate.error) return gate.error;
  const sql = db();
  const id = parseId(new URL(req.url).pathname, BASE);
  if (Number.isNaN(id)) return json({ error: 'Bad id.' }, 400);

  try {
    if (req.method === 'GET') {
      const rows = await sql`select * from enquiries order by (status = 'new') desc, created_at desc limit 500`;
      return json({ items: rows });
    }
    if (req.method === 'PATCH' && id !== null) {
      const body = await req.json().catch(() => ({}));
      if (!ENQUIRY_STATUSES.includes(body.status)) return json({ error: 'Bad status.' }, 422);
      const rows = await sql`update enquiries set status = ${body.status} where id = ${id} returning *`;
      return rows.length ? json({ item: rows[0] }) : json({ error: 'Not found.' }, 404);
    }
    if (req.method === 'DELETE' && id !== null) {
      const rows = await sql`delete from enquiries where id = ${id} returning id`;
      return rows.length ? json({ ok: true }) : json({ error: 'Not found.' }, 404);
    }
    return json({ error: 'Not allowed.' }, 405);
  } catch (err) {
    console.error('admin-enquiries error', err?.message);
    return json({ error: 'Something went wrong. Please try again.' }, 500);
  }
};

export const config = { path: [BASE, BASE + '/*'] };
