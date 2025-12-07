# Feature Specification: Task CRUD Operations and CLI User Interface

**Feature Branch**: `001-task-crud`  
**Created**: 2025-12-06
**Status**: Final  
**Input**: Implement the core CRUD operations for tasks with a modern, user-friendly CLI.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add a new task (Priority: P1)

As a user, I want to add a new task to my to-do list so that I can keep track of what I need to do.

**Why this priority**: This is the most fundamental feature.

**Independent Test**: The user can add a task and see it in the list.

**Acceptance Scenarios**:

1. **Given** I have an empty to-do list, **When** I add a new task with the title "Buy milk" and description "2% fat", **Then** my to-do list should contain one task with title "Buy milk" and description "2% fat" and show a success message.
2. **Given** I have a to-do list with one task, **When** I add another task with the title "Study for exam" and description "Chapter 5", **Then** my to-do list should contain two tasks and show a success message.
3. **Given** I am in the "Add Task" menu, **When** I enter an empty title or an empty description, **Then** I should see an error message "Error: Title and description cannot be empty."

---

### User Story 2 - View my to-do list (Priority: P1)

As a user, I want to view all the tasks in my to-do list so that I can see what I need to do.

**Why this priority**: This is essential to see the tasks that have been added.

**Independent Test**: The user can view a list of all their tasks.

**Acceptance Scenarios**:

1. **Given** I have an empty to-do list, **When** I view my to-do list, **Then** I should see a message "No tasks found." within the task list display.
2. **Given** I have a to-do list with two tasks, **When** I view my to-do list, **Then** I should see both tasks with their IDs, truncated titles, and completion status in a formatted table, along with the total tasks count.

---

### User Story 3 - Update a task (Priority: P2)

As a user, I want to update the description of a task in my to-do list so that I can correct mistakes or change my mind.

**Why this priority**: This is an important feature for managing tasks.

**Independent Test**: The user can update a task's description and see the updated description in the list.

**Acceptance Scenarios**:

1. **Given** I have a to-do list with a task (ID: 1, title: "Buy milk", description: "2% fat"), **When** I update the task with ID 1 to new title "Buy almond milk" and new description "unsweetened", **Then** my to-do list should contain the task (ID: 1, title: "Buy almond milk", description: "unsweetened") and show a success message.
2. **Given** I have a to-do list, **When** I try to update a task with a non-existent ID (e.g., 999), **Then** I should see an error message "Error: Task with ID 999 not found.".
3. **Given** I have a to-do list with a task (ID: 1), **When** I enter an empty new title and empty new description, **Then** I should see an error message "No changes provided. Task not updated.".
4. **Given** I am in the "Update Task" menu, **When** I enter an invalid task ID (e.g., "abc"), **Then** I should see an error message "Error: Task ID must be an integer.".

---

### User Story 4 - Mark a task as complete/incomplete (Priority: P2)

As a user, I want to mark a task as complete or incomplete so that I can track my progress.

**Why this priority**: This is a core feature of a to-do list.

**Independent Test**: The user can mark a task as complete and see the updated status in the list.

**Acceptance Scenarios**:

1. **Given** I have a to-do list with an incomplete task (ID: 1), **When** I mark the task with ID 1 as complete, **Then** the task should be marked as complete and show a success message "Task 1 marked as complete!".
2. **Given** I have a to-do list with a complete task (ID: 1), **When** I mark the task with ID 1 as incomplete, **Then** the task should be marked as incomplete and show a success message "Task 1 marked as incomplete!".
3. **Given** I have a to-do list, **When** I try to mark a task with a non-existent ID (e.g., 999), **Then** I should see an error message "Error: Task with ID 999 not found.".
4. **Given** I am in the "Toggle Task Completion" menu, **When** I enter an invalid task ID (e.g., "xyz"), **Then** I should see an error message "Error: Task ID must be an integer.".

---

### User Story 5 - Delete a task (Priority: P3)

As a user, I want to delete a task from my to-do list so that I can remove tasks that are no longer needed.

**Why this priority**: This is a useful feature for keeping the to-do list clean.

**Independent Test**: The user can delete a task and it will no longer appear in the list.

**Acceptance Scenarios**:

1. **Given** I have a to-do list with one task (ID: 1, title: "Buy milk"), **When** I enter ID 1 and confirm deletion ('y'), **Then** my to-do list should be empty and show a success message "Task 1: 'Buy milk' deleted successfully!".
2. **Given** I have a to-do list with one task (ID: 1, "Buy milk"), **When** I enter ID 1 and cancel deletion ('n'), **Then** the task should still be in the list and show a message "Task deletion cancelled.".
3. **Given** I have a to-do list, **When** I try to delete a task with a non-existent ID (e.g., 999), **Then** I should see an error message "Error: Task with ID 999 not found.".
4. **Given** I am in the "Delete Task" menu, **When** I enter an invalid task ID (e.g., "abc"), **Then** I should see an error message "Error: Task ID must be an integer.".

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add a task with a description (derived from title and description).
- **FR-002**: System MUST allow users to view a list of all tasks.
- **FR-003**: System MUST allow users to update the description of a task.
- **FR-004**: System MUST allow users to mark a task as complete or incomplete.
- **FR-005**: System MUST allow users to delete a task.
- **FR-006**: System MUST handle cases where a user tries to operate on a non-existent task.
- **FR-007**: System MUST not allow tasks with an empty title or an empty description.

### Key Entities *(include if feature involves data)*

- **Task**:
    - `id`: A unique identifier for the task (integer, auto-incrementing).
    - `title`: A concise title for the task (string).
    - `description`: A detailed description of the task (string).
    - `completed`: A boolean indicating whether the task is complete or not (default: `False`).

## UI/UX Requirements *(mandatory)*

### UI-001: General UI Principles
- The CLI interface must be clean, modern, and user-friendly.
- Clear headers, consistent spacing, and borders (`=`, `-`) must be used.
- Consistent formatting across all menus.
- No confusing prints or raw output; guide the user smoothly.
- **Smooth UX:**
    - All actions must return to the main menu after completion.
    - The screen must be cleared (`os.system("cls")` for Windows, `os.system("clear")` for others) before displaying new pages.
    - Consistent horizontal rulers using "------------------------------------------".

### UI-002: Color Usage
- Simple ANSI colors MUST be used via `colorama`.
- Colors MUST reset (`Style.RESET_ALL`) after printing.
- **Color Scheme:**
    - **Cyan (`Fore.CYAN`):** Titles/Headers of menus and sections.
    - **Green (`Fore.GREEN`):** Success messages.
    - **Red (`Fore.RED`):** Error messages.
    - **Yellow (`Fore.YELLOW`):** Warning or cancellation messages (e.g., "Task deletion cancelled.").
    - **White (Default):** Menu text and general input prompts.

### UI-003: Main Menu Layout
When the program starts and after completing any action, the Main Menu MUST be displayed as follows:

```
==========================================
TODO APPLICATION
==========================================
Select an option:
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Complete / Incomplete
6. Exit
------------------------------------------
Enter your choice: _
```
- **Invalid Choice:** If user enters invalid input (e.g., "7", "abc"), an error message "Invalid choice. Please try again." (Red) should be displayed, and the menu redisplayed after a short pause.
- **Empty Command:** If user enters an empty line, an error message "Error: No command entered. Type 'help' for available commands." (Red) should be displayed (though this is now handled by the main menu logic).

### UI-004: View Tasks Layout
When listing tasks (Menu Option 2), the display MUST be a table-like structure:

```
==================================================================
TASK LIST
==================================================================
ID   Title           Description               Status
------------------------------------------------------------------
1    Buy groceries   Get milk and bread        Pending
2    Study for exam  Chapter 5 on Python       Completed
3    Call Ahmed      Call about the project    Pending
------------------------------------------------------------------
Total tasks: X

Press Enter to return to the main menu..._
```
- **Headers:** "ID", "Title", "Description", "Status" MUST be `Yellow`.
- **Title Truncation:** Task titles longer than 15 characters MUST be truncated to 12 characters followed by "..." (e.g., "Buy groceri...").
- **Description Truncation:** Task descriptions longer than 25 characters MUST be truncated to 22 characters followed by "..." (e.g., "Get milk and brea...").
- **Empty State:** If no tasks exist, "No tasks found." should be displayed where the task list would be.

### UI-005: Add Task Layout
When adding a task (Menu Option 1), the display MUST be:

```
==========================================
ADD NEW TASK
==========================================
Enter task title: ________
Enter description: ________
```
- **Success Message:** "Task [ID]: '[Title]' added successfully!" (Green).
- **Empty Input Error:** "Error: Title and description cannot be empty." (Red).

### UI-006: Update Task Layout
When updating a task (Menu Option 3), the display MUST be:

```
==========================================
UPDATE TASK
==========================================
Enter task ID to update: ____
```
Followed by the update prompt (implemented via `display_update_task_menu(task_id)`):
```
==========================================
UPDATE TASK (ID: X)
==========================================
Enter new title (leave empty to keep same): ________
Enter new description (leave empty to keep same): ________
```
- **Success Message:** "Task updated successfully!" (Green).
- **Non-existent Task Error:** "Error: Task with ID X not found." (Red).
- **Empty Update Input Error:** "No changes provided. Task not updated." (Red).
- **Invalid ID Type Error:** "Error: Task ID must be an integer." (Red).

### UI-007: Delete Task Layout
When deleting a task (Menu Option 4), the display MUST be:

```
==========================================
DELETE TASK
==========================================
Enter task ID to delete: ____
Confirm deletion (y/n): _
```
- **Success Message:** "Task [ID]: '[Title]' deleted successfully!" (Green).
- **Cancellation Message:** "Task deletion cancelled." (Yellow).
- **Non-existent Task Error:** "Error: Task with ID X not found." (Red).
- **Invalid ID Type Error:** "Error: Task ID must be an integer." (Red).

### UI-008: Mark Complete / Incomplete Menu Layout
When toggling task completion (Menu Option 5), the display MUST be:

```
==========================================
TOGGLE TASK COMPLETION
==========================================
Enter task ID: ____
```
- **Success Message (Complete):** "Task X marked as complete!" (Green).
- **Success Message (Incomplete):** "Task X marked as incomplete!" (Yellow).
- **Non-existent Task Error:** "Error: Task with ID X not found." (Red).
- **Invalid ID Type Error:** "Error: Task ID must be an integer.".

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A user can perform all CRUD operations on tasks via the CLI without errors, with a clear and consistent UI.
- **SC-002**: The task list accurately reflects all changes made by the user, displayed in the specified table format.
- **SC-003**: All UI elements, including headers, menus, messages, and colors, strictly adhere to the UI/UX Requirements.
- **SC-004**: Input validation and error handling messages are displayed correctly for all specified scenarios.