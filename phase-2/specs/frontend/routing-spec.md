# Frontend Routing (React Router v6)

Routes:
- "/" -> LandingPage (public)
- "/login" -> LoginPage (public)
- "/signup" -> SignupPage (public)
- "/dashboard" -> DashboardPage (protected)
- "*" -> NotFoundPage

Route Guards:
- ProtectedRoute component checks for token in localStorage "todo_token"
- On 401, clear token and redirect to /login

Data fetching:
- fetch wrapper uses VITE_API_URL env var (client-side)
- Authorization header: Bearer <token>
