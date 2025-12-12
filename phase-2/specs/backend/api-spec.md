# Backend API Specification — Todo App (Phase 2)

Base:
- Dev base URL: http://localhost:8000
- Returns and accepts JSON only
- All timestamps ISO 8601 UTC (e.g., 2025-12-10T12:00:00Z)
- Auth: Authorization: Bearer <token> for protected endpoints
- Error format: see backend/error-spec.md

AUTH
POST /auth/register
- Request: { "email": "string (email)", "password": "string (min 8)" }
- Response 201:
  { "id": "uuid", "email": "user@example.com", "created_at": "ISO8601" }
- Errors:
  400 validation_error
  409 conflict (email exists)

POST /auth/login
- Request: { "email": "string", "password": "string" }
- Response 200:
  { "access_token": "<jwt>", "token_type": "bearer", "expires_in": 604800 }
- Errors:
  401 invalid_credentials

TASKS (Protected)
GET /tasks
- Query params:
  - status: all|pending|completed (default: all)
  - q: string (search in title/description)
  - limit: int (default 20, max 100)
  - offset: int (default 0)
- Response 200:
  { "data": [ Task, ... ], "meta": { "total": int, "limit": int, "offset": int } }

POST /tasks
- Request: { "title": "string (1..200)", "description": "string (0..2000)" }
- Response 201: Task JSON
- Errors: 400 validation_error, 401 unauthorized

GET /tasks/{id}
- Response 200 Task or 404 not_found or 403 forbidden

PUT /tasks/{id}
- Request: { "title": "string", "description": "string", "completed": bool }
- Response 200 updated Task
- Errors: 400,401,403,404

PATCH /tasks/{id}/toggle
- Toggles completed
- Response 200 updated Task

DELETE /tasks/{id}
- Response 204 No Content
- Errors: 401,403,404

Notes:
- Task JSON:
  {
    "id": 1,
    "user_id": "uuid",
    "title": "string",
    "description": "string",
    "completed": false,
    "created_at": "ISO8601",
    "updated_at": "ISO8601"
  }
