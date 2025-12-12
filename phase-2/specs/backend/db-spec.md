# Database Specification — PostgreSQL

Tables:

users
- id UUID PRIMARY KEY DEFAULT gen_random_uuid() or uuid_generate_v4()
- email VARCHAR(320) UNIQUE NOT NULL
- password_hash TEXT NOT NULL
- created_at TIMESTAMPTZ NOT NULL DEFAULT now()
- updated_at TIMESTAMPTZ NOT NULL DEFAULT now()

tasks
- id SERIAL PRIMARY KEY
- user_id UUID REFERENCES users(id) ON DELETE CASCADE
- title VARCHAR(200) NOT NULL
- description TEXT NULL
- completed BOOLEAN NOT NULL DEFAULT false
- created_at TIMESTAMPTZ NOT NULL DEFAULT now()
- updated_at TIMESTAMPTZ NOT NULL DEFAULT now()

Indexes:
- idx_users_email ON users(email)
- idx_tasks_user_id ON tasks(user_id)
- idx_tasks_created_at ON tasks(created_at)
- idx_tasks_completed ON tasks(completed)

Migrations:
- Use Alembic or SQL migration scripts in backend/src/app/database/migrations/
- Include initial migration creating tables and indexes
- Provide seed script to create one dev user and sample tasks
