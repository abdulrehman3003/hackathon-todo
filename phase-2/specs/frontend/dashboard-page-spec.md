# Dashboard Page Spec (protected)

Layout:
- Sidebar (left)
- TopNavbar inside main content with user email and logout button
- Content:
  - Stats row (3 cards)
  - Filters row (Today, Upcoming, Completed)
  - TaskList (scrollable)
  - Add Task button (floating bottom-right on mobile, header on desktop)

Functionality:
- Load tasks via GET /tasks on mount
- Filters adjust displayed tasks client-side or server-side via query param
- Add Task opens CSS modal, calls POST /tasks
- Edit opens modal prefilled; calls PUT /tasks/{id}
- Delete opens confirm dialog; calls DELETE /tasks/{id}
- Toggle completion uses PATCH /tasks/{id}/toggle

UX:
- Optimistic UI permitted but rollback on error
- Toasts on success/error
- Loading skeletons while fetching
- Pagination/infinite scroll optional; default limit applied

Security:
- On 401: logout and redirect to /login
