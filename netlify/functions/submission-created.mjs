// Runs automatically after every Netlify Forms submission. Saves employer enquiries to the
// database so they show up in /admin/. Never fails the submission: Netlify still emails/stores it.
import { db } from '../lib/db.mjs';
import { cleanEnquiryFields } from '../lib/validate.mjs';

export const handler = async (event) => {
  try {
    const { payload } = JSON.parse(event.body || '{}');
    if (!payload || payload.form_name !== 'employer-enquiry') return { statusCode: 200, body: 'ignored' };
    const e = cleanEnquiryFields(payload.data);
    const sql = db();
    await sql`
      insert into enquiries (company, contact_name, email, phone, role, province, how_many, urgency, message)
      values (${e.company}, ${e.contact_name}, ${e.email}, ${e.phone}, ${e.role}, ${e.province}, ${e.how_many}, ${e.urgency}, ${e.message})`;
    return { statusCode: 200, body: 'saved' };
  } catch (err) {
    console.error('submission-created error', err?.message);
    return { statusCode: 200, body: 'not saved' };
  }
};
