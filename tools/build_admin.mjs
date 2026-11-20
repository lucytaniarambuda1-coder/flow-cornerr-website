// Bundles the admin page script (src/admin/main.js) into assets/admin.js.
// Runs as part of `npm run build` on Netlify, before tools/build_dist.py.
import { build } from 'esbuild';

await build({
  entryPoints: ['src/admin/main.js'],
  outfile: 'assets/admin.js',
  bundle: true,
  minify: true,
  format: 'iife',
  target: ['es2020'],
  logLevel: 'info',
});
