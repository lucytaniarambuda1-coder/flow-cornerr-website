import { getUser, verifyRequestOrigin } from '@netlify/identity';
import { json } from './http.mjs';

// Only Lucy can reach the admin API. Registration is invite-only in Netlify Identity;
// ADMIN_EMAILS (comma-separated, set in Netlify's environment variables) is a second lock.
export async function requireAdmin(req) {
  if (req.method !== 'GET' && req.method !== 'HEAD') {
    try { verifyRequestOrigin(req); } catch { return { error: json({ error: 'Bad origin.' }, 403) }; }
  }
  let user = null;
  try { user = await getUser(); } catch { user = null; }
  if (!user) return { error: json({ error: 'Please sign in.' }, 401) };
  const allow = (process.env.ADMIN_EMAILS || '').split(',').map((s) => s.trim().toLowerCase()).filter(Boolean);
  if (allow.length && !allow.includes((user.email || '').toLowerCase())) {
    return { error: json({ error: 'This account is not allowed.' }, 403) };
  }
  return { user };
}
