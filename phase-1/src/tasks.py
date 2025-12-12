class Task:
    next_id = 1

    def __init__(self, title: str, description: str):
        self.id = Task.next_id
        Task.next_id += 1
        self.title = title
        self.description = description
        self.completed = False

    def __repr__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}: {self.title}"

tasks = []

def add_task(title: str, description: str) -> Task | None:
    """Adds a new task to the list. Returns the task object on success, None on failure."""
    if not title.strip() or not description.strip(): # Check for empty or whitespace-only title or description
        return None # Indicate failure
    task = Task(title, description)
    tasks.append(task)
    return task

def view_tasks() -> list[Task]:
    """Returns the list of all tasks."""
    return tasks

def find_task_by_id(task_id: int) -> Task | None:
    """Finds a task by its ID."""
    return next((task for task in tasks if task.id == task_id), None)

def update_task(task_id: int, new_title: str, new_description: str) -> Task | None:
    """Updates the title and/or description of an existing task. Returns the updated task object on success, None if no changes or task not found."""
    task = find_task_by_id(task_id)
    if not task:
        return None # Indicate failure (task not found)

    updated = False
    if new_title.strip():
        task.title = new_title
        updated = True
    if new_description.strip():
        task.description = new_description
        updated = True

    if updated:
        return task
    return None # Indicate no changes were provided

def mark_task(task_id: int, completed: bool) -> Task | None:
    """Marks a task as complete or incomplete. Returns the modified task object on success, None on failure."""
    task = find_task_by_id(task_id)
    if task:
        task.completed = completed
        return task
    return None # Indicate failure (task not found)

def delete_task(task_id: int) -> Task | None:
    """Deletes a task from the list. Returns the deleted task object on success, None on failure."""
    task = find_task_by_id(task_id)
    if task:
        tasks.remove(task)
        return task
    return None # Indicate failure (task not found)
