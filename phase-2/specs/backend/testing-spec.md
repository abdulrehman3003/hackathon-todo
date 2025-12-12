# Backend Testing Specification (pytest)

Goals:
- Verify auth flows
- Verify CRUD + ownership
- Validate input errors
- Ensure 401/403/404 behavior

Test files:
- tests/conftest.py: test db, client, fixtures
- tests/test_auth.py
  - test_register_success
  - test_register_duplicate_email -> 409
  - test_login_success_returns_jwt
  - test_login_bad_credentials -> 401
- tests/test_tasks.py
  - test_create_task_success -> 201
  - test_create_task_missing_title -> 400
  - test_list_tasks_pagination
  - test_get_task_not_owner -> 403
  - test_update_task_success -> 200
  - test_toggle_task -> 200
  - test_delete_task_success -> 204
- tests/test_security.py
  - test_missing_token -> 401
  - test_invalid_token -> 401

Test DB:
- Use ephemeral Postgres or sqlite (if acceptable) configured via env var TEST_DATABASE_URL
Run:
- uv run pytest -q
