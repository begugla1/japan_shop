# japan_shop

Little internet-shop with authentication, cart and favorites.

## Quick start (portable setup)

This project uses PostgreSQL with fixed defaults from settings:
- DB name: `japanshop`
- DB user: `japanshop_user`

1. Install system dependencies:
   - Python 3.10+
   - PostgreSQL (server + `psql` client)
2. Run:
   - `make bootstrap`
3. Start app:
   - `make run`

The first bootstrap run will:
- create `.venv`
- install Python requirements
- create `.env` from `.env.example` (if missing)
- create/update PostgreSQL role and database
- run migrations

## Useful commands

- `make run-https` - run HTTPS server for social auth callbacks
- `make superuser` - create admin user
- `make shell` - open Django shell
- `make clean` - remove virtual environment

## Environment variables

Edit `.env` and fill required values:
- `SECRET_KEY`
- `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
- OAuth keys (`SOCIAL_AUTH_*`)
- Stripe keys (`STRIPE_*`)

Gmail App Password docs: https://support.google.com/accounts/answer/185833?hl=ru

## Docker (one command)

Run everything (PostgreSQL + Django) with:
- `docker compose up --build`

Then open:
- http://localhost:8000
- https://localhost:8000 (for Google/GitHub OAuth)

Notes:
- This keeps Django project code untouched.
- Compose uses development defaults for env vars, so no mandatory pre-configuration is needed.
- On Linux, compose uses `host` network mode to avoid bridge/veth errors on restricted systems.
- Web container installs dependencies at startup (no Docker build step), so first launch can take several minutes.

### Admin panel and products

1. Create superuser (one-time):
   - `docker compose exec web python manage.py createsuperuser`
2. Open admin:
   - https://localhost:8000/admin/
3. Add products:
   - In admin UI open the model for products/items and create entries there.

Optional auto-create admin on startup:
- Set in `.env`:
  - `CREATE_SUPERUSER=1`
  - `DJANGO_SUPERUSER_USERNAME=admin`
  - `DJANGO_SUPERUSER_EMAIL=admin@example.com`
  - `DJANGO_SUPERUSER_PASSWORD=admin`

### OAuth (Google/GitHub) setup

Set OAuth keys in `.env`:
- `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=...`
- `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=...`
- `SOCIAL_AUTH_GITHUB_KEY=...`
- `SOCIAL_AUTH_GITHUB_SECRET=...`

Use these callback URLs in providers:
- Google: `https://localhost:8000/social-auth/complete/google-oauth2/`
- GitHub: `https://localhost:8000/social-auth/complete/github/`

Why it failed before:
- OAuth vars were empty in compose.
- App setting `ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'` requires HTTPS callback flow.
