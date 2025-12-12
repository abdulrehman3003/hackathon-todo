# Authentication Specification (Backend)

Mechanism:
- JWT (HS256) signed with JWT_SECRET from env
- Token payload (claims): { "sub": "<user_id>", "email": "<email>", "iat": <ts>, "exp": <ts> }

Signup (POST /auth/register):
- Validate email format, check uniqueness
- Validate password >= 8 characters
- Hash using bcrypt (passlib)
- Return id, email, created_at

Login (POST /auth/login):
- Validate credentials against password hash
- On success return access_token and expiry
- Token expiry default: 7 days (JWT_EXPIRES_IN env)

Token usage:
- Frontend stores token in localStorage key "todo_token"
- Backend must reject missing/invalid/expired tokens with 401 (code: unauthorized)

Security:
- Do not include password hash in responses
- Use HTTPS in production (CORS origins via env)
- Consider rotating JWT secret in deployment notes (optional)
