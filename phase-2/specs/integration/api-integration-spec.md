# API Integration Spec (Frontend-Backend)

- Base URL: VITE_API_URL
- Fetch wrapper: /frontend/src/lib/api.js
- Wrapper handles:
  - Setting Authorization header with token if exists
  - JSON response parsing
  - Throwing structured error object: { code, detail, status }
  - Auto logout & redirect on 401
- All calls must map backend error codes to UI messages (see error-handling-spec.md)
