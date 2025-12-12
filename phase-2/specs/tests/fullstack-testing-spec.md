# Fullstack Testing Specification

Backend tests (pytest) are required:
- Auth tests: register, duplicate, login success/fail
- Tasks tests: create, invalid create, list (user only), get (not owner), update, toggle, delete
- Security: missing token -> 401, invalid token -> 401

Frontend tests (recommended):
- Unit tests for components: Button, Input, Modal, TaskItem
- Integration tests for Login flow: render, validation, mock API responses
- Dashboard tests: render list with mocked API, open add modal, submit, list updates

E2E (optional):
- Cypress or Playwright scenario: user registers, logs in, creates task, toggles, deletes

Test environments:
- Backend tests run using TEST_DATABASE_URL; isolate DB per test run
- Frontend tests mock fetch calls with MSW (Mock Service Worker)
