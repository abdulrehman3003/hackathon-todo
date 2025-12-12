# Login Page Spec

Layout:
- Centered auth card max-width 420px
- Title "Log in"
- Inputs: email (type=email), password (type=password) with visibility toggle
- Actions: login button, link to signup

Behavior:
- Client-side validate email & password length
- On submit: POST /auth/login
- On 200: store token in localStorage and navigate to /dashboard
- On 401: show toast "Invalid credentials"
- On 400: show inline validation errors

Accessibility:
- Labels associated with inputs
- Enter submits form
- Focus states visible
