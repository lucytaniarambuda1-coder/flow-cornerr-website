// Input checks shared by the admin functions. Pure functions, easy to test.

export const PROVINCES = [
  'National', 'Gauteng', 'Western Cape', 'KwaZulu-Natal', 'Eastern Cape',
  'Free State', 'Limpopo', 'Mpumalanga', 'North West', 'Northern Cape', 'Remote',
];
export const JOB_STATUSES = ['draft', 'published', 'archived'];
export const ENQUIRY_STATUSES = ['new', 'contacted', 'closed'];

const str = (v, max) => (typeof v === 'string' ? v.trim().slice(0, max) : '');

export function cleanJob(body) {
  const errors = [];
  const b = body && typeof body === 'object' ? body : {};
  const job = {
    title: str(b.title, 160),
    org: str(b.org, 120),
    type: str(b.type, 60),
    province: str(b.province, 40) || 'National',
    description: str(b.description, 2000),
    url: str(b.url, 500),
    cta: str(b.cta, 80) || null,
    tags: (Array.isArray(b.tags) ? b.tags : String(b.tags || '').split(','))
      .map((t) => str(t, 40).toLowerCase()).filter(Boolean).slice(0, 12),
    closing: str(b.closing, 10) || null,
    status: str(b.status, 20) || 'draft',
  };
  if (!job.title) errors.push('Title is required.');
  if (!job.org) errors.push('Organisation is required.');
  if (!job.type) errors.push('Type is required.');
  if (!job.description) errors.push('Description is required.');
  if (!/^https?:\/\/[^\s]+$/i.test(job.url)) errors.push('Link must start with http:// or https://');
  if (!PROVINCES.includes(job.province)) errors.push('Choose a province from the list.');
  if (!JOB_STATUSES.includes(job.status)) errors.push('Status must be draft, published or archived.');
  if (job.closing !== null) {
    const ok = /^\d{4}-\d{2}-\d{2}$/.test(job.closing) && !Number.isNaN(Date.parse(job.closing + 'T00:00:00Z'));
    if (!ok) errors.push('Closing date must look like 2026-12-31.');
  }
  return errors.length ? { ok: false, errors } : { ok: true, value: job };
}

export function cleanEnquiryFields(data) {
  const d = data && typeof data === 'object' ? data : {};
  return {
    company: str(d.company, 160),
    contact_name: str(d.contact_name, 120),
    email: str(d.email, 200),
    phone: str(d.phone, 60),
    role: str(d.role, 160),
    province: str(d.province, 40),
    how_many: str(d.how_many, 60),
    urgency: str(d.urgency, 60),
    message: str(d.message, 3000),
  };
}

export function parseId(pathname, base) {
  const rest = pathname.slice(pathname.indexOf(base) + base.length).replace(/^\/+|\/+$/g, '');
  if (!rest) return null;
  return /^\d{1,12}$/.test(rest) ? Number(rest) : NaN;
}
