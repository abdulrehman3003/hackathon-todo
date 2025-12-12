# Backend Behavior & Business Logic

Ownership:
- Use user_id from JWT to filter tasks
- Accessing others' tasks => 403

Validation:
- title: required, 1..200 chars
- description: optional, max 2000 chars
- id path params: integer -> 400 if invalid

Responses:
- Follow HTTP semantics (200, 201, 204, 400, 401, 403, 404, 409, 500)

Transactions:
- Writes should be transactional to avoid partial updates
- Use optimistic concurrency with updated_at for potential conflicts

Pagination & Search:
- GET /tasks supports limit/offset and q parameter for text search on title/description
- Return meta with total count

Logging:
- Minimal logging in responses; full logs for server-side only
