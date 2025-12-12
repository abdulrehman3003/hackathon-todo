# TaskList Component Spec

Props:
- tasks: array
- onEdit(id)
- onDelete(id)
- onToggle(id)

Behavior:
- Render tasks sorted newest first
- Empty state "No tasks yet" with CTA Add Task
- Animate task item entries (fade-in + slight upward motion)
