# Auth Flow Spec

- Registration:
  - POST /auth/register -> on 201 redirect to /login with toast
- Login:
  - POST /auth/login -> store token in localStorage key "todo_token"; set user context
  - After login redirect to /dashboard
- Logout:
  - Clear token & user context, redirect to /login
- Token refresh:
  - Out of scope for Phase 2 (stateless JWT)
