// Runs automatically after every Netlify Forms submission. Saves employer enquiries to the
// database so they show up in /admin/. Never fails the submission: Netlify still emails/stores it.
//
// Written in the modern (Request/Response) function format on purpose: the older "handler"
// format has no access to the Netlify Database connection, so inserts failed there.
import { db } from '../lib/db.mjs';
import { cleanEnquiryFields } from '../lib/validate.mjs';

export default async (req) => {
  try {
    const { payload } = await req.json();
    if (!payload || payload.form_name !== 'employer-enquiry') return new Response('ignored', { status: 200 });
    const e = cleanEnquiryFields(payload.data);
    const sql = db();
    const rows = await sql`
      insert into enquiries (company, contact_name, email, phone, role, province, how_many, urgency, message)
      values (${e.company}, ${e.contact_name}, ${e.email}, ${e.phone}, ${e.role}, ${e.province}, ${e.how_many}, ${e.urgency}, ${e.message})
      returning id`;
    console.log('submission-created: saved enquiry', rows[0]?.id);
    return new Response('saved', { status: 200 });
  } catch (err) {
    console.error('submission-created error', err?.message);
    return new Response('not saved', { status: 200 });
  }
};
