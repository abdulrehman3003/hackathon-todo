# Backend Logging Specification

Objectives:
- Track request lifecycle and errors
- Avoid leaking secrets

Log entries:
- Request: timestamp, method, path, user_id if present, request_id, latency, status
- Error: timestamp, path, error_code, stack trace (server logs only), correlation id

Do not log:
- Passwords, tokens, or full request bodies with sensitive content

Format:
- JSON structured logs for production; plain text ok for dev
