# Backend Error Codes & Format

Standard format:
{
  "detail": "Human readable message",
  "code": "machine_code",
  "meta": { ... optional ... }
}

Common codes:
- validation_error
- unauthorized
- forbidden
- not_found
- conflict
- server_error

Examples:
400 -> { "detail": "Title is required", "code": "validation_error" }
401 -> { "detail": "Invalid token", "code": "unauthorized" }
403 -> { "detail": "Access denied", "code": "forbidden" }
404 -> { "detail": "Task not found", "code": "not_found" }

Mapping to frontend:
- Map code -> friendly message (see integration/error-handling-spec.md)
