-- Jobs and opportunities shown on /opportunities/, managed from /admin/.
create table jobs (
  id          bigserial primary key,
  title       text not null,
  org         text not null,
  type        text not null,
  province    text not null default 'National',
  description text not null,
  url         text not null,
  cta         text,
  tags        text[] not null default '{}',
  closing     date,
  status      text not null default 'draft' check (status in ('draft', 'published', 'archived')),
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);
create index jobs_status_closing_idx on jobs (status, closing);

-- Employer enquiries from /for-business/hire/ (saved by the submission-created function).
create table enquiries (
  id           bigserial primary key,
  company      text,
  contact_name text,
  email        text,
  phone        text,
  role         text,
  province     text,
  how_many     text,
  urgency      text,
  message      text,
  status       text not null default 'new' check (status in ('new', 'contacted', 'closed')),
  created_at   timestamptz not null default now()
);
create index enquiries_status_created_idx on enquiries (status, created_at desc);
