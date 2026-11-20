// Flow Corner admin: sign in, manage jobs, read employer enquiries.
// Bundled by tools/build_admin.mjs into assets/admin.js. All user-supplied text is
// written with textContent, never innerHTML.
import { login, logout, getUser, handleAuthCallback, acceptInvite, updateUser, requestPasswordRecovery } from '@netlify/identity';

const PROVINCES = ['National', 'Gauteng', 'Western Cape', 'KwaZulu-Natal', 'Eastern Cape', 'Free State', 'Limpopo', 'Mpumalanga', 'North West', 'Northern Cape', 'Remote'];
const TYPES = ['Job', 'Learnership', 'Internship', 'Bursary', 'Youth programme', 'Job platform', 'Graduate programme', 'Other'];
const root = document.getElementById('adminApp');

function el(tag, attrs, ...kids) {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (k === 'class') n.className = v;
    else if (k.startsWith('on')) n.addEventListener(k.slice(2), v);
    else if (v !== false && v != null) n.setAttribute(k, v === true ? '' : v);
  }
  for (const kid of kids.flat()) if (kid != null) n.append(kid.nodeType ? kid : document.createTextNode(String(kid)));
  return n;
}
const mount = (...nodes) => { root.replaceChildren(...nodes); };
const msg = (text, kind = 'info') => el('p', { class: 'adm-msg adm-' + kind, role: 'status' }, text);

async function api(path, opts = {}) {
  const res = await fetch(path, {
    credentials: 'same-origin',
    ...opts,
    headers: { 'Content-Type': 'application/json', ...(opts.headers || {}) },
  });
  let data = {};
  try { data = await res.json(); } catch { /* empty body */ }
  if (res.status === 401) { showLogin('Please sign in again.'); throw new Error('signed-out'); }
  if (!res.ok) throw Object.assign(new Error(data.error || 'Request failed'), { data, status: res.status });
  return data;
}

/* ---------- sign-in screens ---------- */
function field(label, input) { return el('label', { class: 'adm-field' }, el('span', {}, label), input); }

function showLogin(note, kind) {
  const email = el('input', { type: 'email', required: true, autocomplete: 'username' });
  const pass = el('input', { type: 'password', required: true, autocomplete: 'current-password' });
  const out = el('div', {}, note ? msg(note, kind) : null);
  const form = el('form', { class: 'adm-card adm-narrow', onsubmit: async (e) => {
    e.preventDefault();
    out.replaceChildren(msg('Signing in…'));
    try { await login(email.value.trim(), pass.value); await showApp(); }
    catch (err) { out.replaceChildren(msg(err?.message || 'Could not sign in.', 'error')); }
  } },
    el('h2', {}, 'Sign in'), field('Email', email), field('Password', pass), out,
    el('button', { class: 'btn-primary', type: 'submit' }, 'Sign in'),
    el('p', { class: 'adm-small' }, el('a', { href: '#', onclick: async (e) => {
      e.preventDefault();
      if (!email.value.trim()) { out.replaceChildren(msg('Type your email above first.', 'error')); return; }
      try { await requestPasswordRecovery(email.value.trim()); out.replaceChildren(msg('If that email has an account, a reset link is on its way.', 'ok')); }
      catch { out.replaceChildren(msg('Could not send a reset link.', 'error')); }
    } }, 'Forgot password?')));
  mount(form);
}

function showSetPassword(title, intro, onSubmit) {
  const p1 = el('input', { type: 'password', required: true, minlength: 8, autocomplete: 'new-password' });
  const p2 = el('input', { type: 'password', required: true, minlength: 8, autocomplete: 'new-password' });
  const out = el('div');
  mount(el('form', { class: 'adm-card adm-narrow', onsubmit: async (e) => {
    e.preventDefault();
    if (p1.value !== p2.value) { out.replaceChildren(msg('The two passwords do not match.', 'error')); return; }
    out.replaceChildren(msg('Saving…'));
    try { await onSubmit(p1.value); await showApp(); }
    catch (err) { out.replaceChildren(msg(err?.message || 'Could not save the password.', 'error')); }
  } }, el('h2', {}, title), el('p', {}, intro), field('New password (8+ characters)', p1), field('Repeat password', p2), out,
    el('button', { class: 'btn-primary', type: 'submit' }, 'Save password')));
}

/* ---------- main app ---------- */
let tab = 'jobs';
async function showApp() {
  const user = await getUser();
  if (!user) return showLogin();
  const body = el('div', { class: 'adm-body' });
  const tabs = ['jobs', 'enquiries'].map((t) => el('button', {
    type: 'button', class: 'adm-tab' + (t === tab ? ' active' : ''),
    onclick: () => { tab = t; showApp(); },
  }, t === 'jobs' ? 'Jobs & opportunities' : 'Employer enquiries'));
  mount(
    el('div', { class: 'adm-top' },
      el('div', { class: 'adm-tabs' }, tabs),
      el('div', { class: 'adm-who' }, user.email || '', ' ',
        el('button', { class: 'adm-link', type: 'button', onclick: async () => { await logout(); showLogin('You are signed out.', 'ok'); } }, 'Sign out'))),
    body);
  if (tab === 'jobs') await renderJobs(body); else await renderEnquiries(body);
}

/* ---------- jobs ---------- */
async function renderJobs(body) {
  body.replaceChildren(msg('Loading jobs…'));
  let items;
  try { items = (await api('/api/admin/jobs')).items; }
  catch (e) { if (e.message !== 'signed-out') body.replaceChildren(msg('Could not load jobs. ' + e.message, 'error')); return; }

  const list = el('div', { class: 'adm-list' });
  const head = el('div', { class: 'adm-row-head' },
    el('h2', {}, `Jobs & opportunities (${items.length})`),
    el('button', { class: 'btn-primary', type: 'button', onclick: () => jobForm(body, null) }, 'Add a job'));
  if (!items.length) list.append(msg('No jobs yet. Click "Add a job".'));
  for (const j of items) {
    const expired = j.closing && j.closing < new Date().toISOString().slice(0, 10);
    list.append(el('div', { class: 'adm-item' },
      el('div', { class: 'adm-item-main' },
        el('strong', {}, j.title), ' ', el('span', { class: 'adm-pill adm-' + j.status }, j.status),
        expired ? el('span', { class: 'adm-pill adm-expired' }, 'closed') : null,
        el('div', { class: 'adm-small' }, `${j.org} · ${j.type} · ${j.province} · ${j.closing ? 'closes ' + j.closing : 'always open'}`)),
      el('div', { class: 'adm-actions' },
        el('button', { type: 'button', class: 'adm-btn', onclick: () => jobForm(body, j) }, 'Edit'),
        el('button', { type: 'button', class: 'adm-btn', onclick: () => setJobStatus(body, j, j.status === 'published' ? 'draft' : 'published') }, j.status === 'published' ? 'Unpublish' : 'Publish'),
        el('button', { type: 'button', class: 'adm-btn adm-danger', onclick: async () => {
          if (!confirm(`Delete "${j.title}" for good?`)) return;
          try { await api('/api/admin/jobs/' + j.id, { method: 'DELETE' }); renderJobs(body); } catch (e) { alert(e.message); }
        } }, 'Delete'))));
  }
  body.replaceChildren(head, list);
}

async function setJobStatus(body, j, status) {
  try { await api('/api/admin/jobs/' + j.id, { method: 'PUT', body: JSON.stringify({ ...j, status }) }); renderJobs(body); }
  catch (e) { if (e.message !== 'signed-out') alert((e.data?.errors || [e.message]).join('\n')); }
}

function jobForm(body, j) {
  const v = j || { title: '', org: '', type: 'Job', province: 'National', description: '', url: '', cta: '', tags: [], closing: '', status: 'draft' };
  const f = {
    title: el('input', { type: 'text', required: true, maxlength: 160, value: v.title }),
    org: el('input', { type: 'text', required: true, maxlength: 120, value: v.org }),
    type: el('select', {}, ...[...new Set([...TYPES, v.type])].map((t) => el('option', { value: t, selected: t === v.type }, t))),
    province: el('select', {}, ...PROVINCES.map((p) => el('option', { value: p, selected: p === v.province }, p))),
    description: el('textarea', { rows: 4, required: true, maxlength: 2000 }, v.description),
    url: el('input', { type: 'url', required: true, placeholder: 'https://…', value: v.url }),
    cta: el('input', { type: 'text', maxlength: 80, placeholder: 'Visit the official page', value: v.cta }),
    tags: el('input', { type: 'text', placeholder: 'youth, learnership, free', value: (v.tags || []).join(', ') }),
    closing: el('input', { type: 'date', value: v.closing }),
    status: el('select', {}, ...['draft', 'published', 'archived'].map((s) => el('option', { value: s, selected: s === v.status }, s))),
  };
  const out = el('div');
  body.replaceChildren(el('form', { class: 'adm-card', onsubmit: async (e) => {
    e.preventDefault();
    const payload = Object.fromEntries(Object.entries(f).map(([k, n]) => [k, n.value]));
    out.replaceChildren(msg('Saving…'));
    try {
      await api(j ? '/api/admin/jobs/' + j.id : '/api/admin/jobs', { method: j ? 'PUT' : 'POST', body: JSON.stringify(payload) });
      renderJobs(body);
    } catch (err) {
      if (err.message === 'signed-out') return;
      out.replaceChildren(msg((err.data?.errors || [err.message]).join(' '), 'error'));
    }
  } },
    el('h2', {}, j ? 'Edit job' : 'Add a job'),
    field('Title', f.title), field('Organisation', f.org),
    el('div', { class: 'adm-two' }, field('Type', f.type), field('Province', f.province)),
    field('Description', f.description), field('Link people apply or read more at', f.url),
    field('Button text (optional)', f.cta), field('Tags (comma separated)', f.tags),
    el('div', { class: 'adm-two' }, field('Closing date (leave empty if always open)', f.closing), field('Status (only "published" shows on the site)', f.status)),
    out,
    el('div', { class: 'adm-actions' },
      el('button', { class: 'btn-primary', type: 'submit' }, 'Save'),
      el('button', { class: 'adm-btn', type: 'button', onclick: () => renderJobs(body) }, 'Cancel'))));
}

/* ---------- enquiries ---------- */
async function renderEnquiries(body) {
  body.replaceChildren(msg('Loading enquiries…'));
  let items;
  try { items = (await api('/api/admin/enquiries')).items; }
  catch (e) { if (e.message !== 'signed-out') body.replaceChildren(msg('Could not load enquiries. ' + e.message, 'error')); return; }
  const list = el('div', { class: 'adm-list' });
  if (!items.length) list.append(msg('No enquiries yet. Employer enquiries from the For Business form will appear here.'));
  for (const q of items) {
    const sel = el('select', { onchange: async () => {
      try { await api('/api/admin/enquiries/' + q.id, { method: 'PATCH', body: JSON.stringify({ status: sel.value }) }); renderEnquiries(body); }
      catch (e) { if (e.message !== 'signed-out') alert(e.message); }
    } }, ...['new', 'contacted', 'closed'].map((s) => el('option', { value: s, selected: s === q.status }, s)));
    const contact = [q.contact_name, q.email, q.phone].filter(Boolean).join(' · ');
    list.append(el('div', { class: 'adm-item adm-enq' },
      el('div', { class: 'adm-item-main' },
        el('strong', {}, q.company || '(no company)'), ' ', el('span', { class: 'adm-pill adm-' + q.status }, q.status),
        el('div', { class: 'adm-small' }, `${new Date(q.created_at).toLocaleString('en-ZA')} · ${q.role || 'role not given'} · ${q.province || '—'} · ${q.how_many || '?'} people · ${q.urgency || '—'}`),
        el('div', {}, contact),
        q.message ? el('p', { class: 'adm-small' }, q.message) : null),
      el('div', { class: 'adm-actions' }, sel,
        q.email ? el('a', { class: 'adm-btn', href: 'mailto:' + q.email }, 'Email') : null,
        q.phone ? el('a', { class: 'adm-btn', href: 'https://wa.me/' + q.phone.replace(/\D/g, '').replace(/^0/, '27') }, 'WhatsApp') : null,
        el('button', { type: 'button', class: 'adm-btn adm-danger', onclick: async () => {
          if (!confirm('Delete this enquiry for good?')) return;
          try { await api('/api/admin/enquiries/' + q.id, { method: 'DELETE' }); renderEnquiries(body); } catch (e) { alert(e.message); }
        } }, 'Delete'))));
  }
  body.replaceChildren(el('div', { class: 'adm-row-head' }, el('h2', {}, `Employer enquiries (${items.length})`)), list);
}

/* ---------- start ---------- */
(async function start() {
  try {
    const cb = await handleAuthCallback();
    history.replaceState(null, '', location.pathname);
    if (cb?.type === 'invite') {
      return showSetPassword('Welcome to Flow Corner admin', 'Choose a password to finish setting up your account.', (pw) => acceptInvite(cb.token, pw));
    }
    if (cb?.type === 'recovery') {
      return showSetPassword('Choose a new password', 'Enter a new password for your account.', (pw) => updateUser({ password: pw }));
    }
  } catch (err) {
    return showLogin('That link did not work or has expired. ' + (err?.message || ''), 'error');
  }
  await showApp();
})();
