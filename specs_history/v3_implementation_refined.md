# Todo App Spec: v3 - Implementation Refined

## 1. Introduction
This document details the refined requirements for the console-based Todo application, incorporating feedback from initial implementation attempts, enhancing error handling, and clarifying edge cases.

## 2. Key Entities

### Task
- **id**: Unique identifier (integer, auto-incrementing).
- **title**: Concise description of the task (string, cannot be empty).
- **description**: Detailed description of the task (string, cannot be empty).
- **completed**: Status (boolean, default: False).

## 3. Core Features

### 3.1 Add Task
- Users should be able to add a new task with a title and an optional detailed description.
- **User Story**: As a user, I want to add a new task so that I can keep track of what I need to do.
- **Acceptance Criteria**:
    - **Happy Path**: When I add a task with title "Buy groceries" and description "Milk, eggs, bread", it appears in my task list as ID 1, title "Buy groceries", description "Milk, eggs, bread", and status Pending. A success message "Task 1: 'Buy groceries' added." is displayed.
    - **Edge Case - Empty Title**: If I try to add a task with an empty title, an error "Title cannot be empty." is displayed, and no task is added.
    - **Edge Case - Empty Description**: If I try to add a task with an empty description, an error "Description cannot be empty." is displayed, and no task is added.

### 3.2 View Tasks
- Users should be able to see a list of all added tasks.
- The list should show the task ID, truncated title, truncated description and completion status in a formatted table.
- **User Story**: As a user, I want to view all my tasks so I can see what I need to do.
- **Acceptance Criteria**:
    - **Happy Path**: When I view tasks, all my added tasks are displayed in a table format with columns: ID, Title (truncated to 15 chars), Description (truncated to 25 chars), Status.
    - **Edge Case - Empty List**: If there are no tasks, a message "No tasks found." is displayed instead of the table.

### 3.3 Update Task
- Users should be able to update the title and/or description of an existing task using its ID.
- **User Story**: As a user, I want to update a task so I can correct mistakes or change my mind.
- **Acceptance Criteria**:
    - **Happy Path**: When I update task ID 1 with a new title "Buy almond milk" and description "unsweetened", the task's title and description are updated accordingly. A success message "Task updated successfully!" is displayed.
    - **Edge Case - Non-existent ID**: If I try to update a task with ID 999 which does not exist, an error "Error: Task with ID 999 not found." is displayed.
    - **Edge Case - No Changes**: If I provide an existing task ID but leave both new title and new description empty, a message "No changes provided. Task not updated." is displayed, and the task remains unchanged.
    - **Edge Case - Invalid ID Input**: If I provide non-integer input for task ID, an error "Error: Task ID must be an integer." is displayed.

### 3.4 Mark Task as Complete/Incomplete
- Users should be able to toggle the completion status of a task using its ID.
- **User Story**: As a user, I want to mark a task as complete so I can track my progress.
- **Acceptance Criteria**:
    - **Happy Path - Complete**: When I mark task ID 1 as complete, its status changes to 'Completed'. A success message "Task 1 marked as complete!" is displayed.
    - **Happy Path - Incomplete**: When I mark task ID 1 as incomplete (if it was complete), its status changes to 'Pending'. A message "Task 1 marked as incomplete!" is displayed.
    - **Edge Case - Non-existent ID**: If I try to mark a task with ID 999 which does not exist, an error "Error: Task with ID 999 not found." is displayed.
    - **Edge Case - Invalid ID Input**: If I provide non-integer input for task ID, an error "Error: Task ID must be an integer." is displayed.

### 3.5 Delete Task
- Users should be able to remove a task from the list using its ID, with a confirmation step.
- **User Story**: As a user, I want to delete a task so I can remove finished or unwanted items.
- **Acceptance Criteria**:
    - **Happy Path**: When I delete task ID 1 and confirm with 'y', it no longer appears in the task list. A success message "Task 1: 'Task Title' deleted successfully!" is displayed.
    - **Happy Path - Cancel**: When I delete task ID 1 and cancel with 'n', the task remains in the list. A message "Task deletion cancelled." is displayed.
    - **Edge Case - Non-existent ID**: If I try to delete a task with ID 999 which does not exist, an error "Error: Task with ID 999 not found." is displayed.
    - **Edge Case - Invalid ID Input**: If I provide non-integer input for task ID, an error "Error: Task ID must be an integer." is displayed.

## 4. User Interface (CLI)
- **Main Menu**: Options for Add, View, Update, Delete, Mark Complete/Incomplete, Exit.
- **Input Validation**: For menu choices and task IDs.
- **Clear Screen**: After each action.
- **Consistent Formatting**: Headers, rulers, colored messages (green for success, red for error, yellow for warning).
- **Return to Main Menu**: After each operation.
