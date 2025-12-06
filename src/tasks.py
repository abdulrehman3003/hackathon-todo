class Task:
    next_id = 1

    def __init__(self, description: str):
        self.id = Task.next_id
        Task.next_id += 1
        self.description = description
        self.completed = False

    def __repr__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}: {self.description}"

tasks = []

def add_task(description: str) -> Task | None:
    """Adds a new task to the list. Returns the task object on success, None on failure."""
    if not description.strip(): # Check for empty or whitespace-only description
        return None # Indicate failure
    task = Task(description)
    tasks.append(task)
    return task

def view_tasks() -> list[Task]:
    """Returns the list of all tasks."""
    return tasks

def find_task_by_id(task_id: int) -> Task | None:
    """Finds a task by its ID."""
    return next((task for task in tasks if task.id == task_id), None)

def update_task(task_id: int, new_description: str) -> Task | None:
    """Updates the description of an existing task. Returns the updated task object on success, None on failure."""
    if not new_description.strip(): # Check for empty or whitespace-only description
        return None # Indicate failure
    task = find_task_by_id(task_id)
    if task:
        task.description = new_description
        return task
    return None # Indicate failure (task not found)

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
