# Signup Page Spec

Same layout as login.

Fields:
- email
- password
- confirmPassword

Validation:
- password min 8
- confirmPassword equals password

Behavior:
- POST /auth/register
- On 201: show success toast and redirect to /login
- On 409: show inline "Email already exists" or toast
