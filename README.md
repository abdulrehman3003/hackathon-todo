# Todo CLI Application

## Project Summary
A simple command-line interface (CLI) application for managing tasks, built using Python. This application allows users to perform basic CRUD (Create, Read, Update, Delete) operations on tasks, along with marking tasks as complete or incomplete, all through an interactive and user-friendly console interface.

## Spec-Driven Development (SDD)
This project was developed using a Spec-Driven Development (SDD) approach, leveraging a `constitution.md` for core principles, detailed `spec` files for feature requirements, AI-generated code, and comprehensive tests. This methodology ensures strict adherence to defined behaviors, consistent UI/UX, and robust functionality. You can trace the evolution of the project's specifications through `specs_history/`, demonstrating iterative refinement from basic requirements to a comprehensive final spec.

## Phase 1 Features

### Core Task Operations
The application supports the following essential task management functionalities:

*   **Add Task (P1):** Users can add new tasks to their to-do list with a title and description.
*   **View All Tasks (P1):** Displays a list of all current tasks, showing their ID, a truncated title, and completion status, in a formatted table.
*   **Update Task (P2):** Allows users to modify the title and/or description of an existing task by its ID.
*   **Mark Task Complete/Incomplete (P2):** Users can toggle the completion status of a task using its ID.
*   **Delete Task (P3):** Provides functionality to remove a task from the list using its ID, with a confirmation prompt.

### User Interface (CLI)
The application features a clean, modern, and user-friendly command-line interface designed with the following principles:

*   **Clear Layouts:** Dedicated screens for the Main Menu, Add Task, View Tasks, Update Task, Delete Task, and Mark Complete/Incomplete operations.
*   **Formatting:** Consistent use of headers, spacing, borders, and horizontal rulers ("------------------------------------------") for readability.
*   **Color Usage (Optional/Preferred):** Utilizes `colorama` for enhanced visual feedback:
    *   **Cyan:** Titles and Headers
    *   **Green:** Success messages
    *   **Red:** Error messages
    *   **White:** Standard menu text
*   **Numbered Menu Choices:** Easy navigation through the main menu using numerical input.
*   **Input Validation:** Robust handling of invalid menu choices and non-existent task IDs.
*   **Smooth User Experience (UX):**
    *   Automatically clears the screen (`cls` for Windows, `clear` for others) before displaying new pages to maintain a clean interface.
    *   Returns to the main menu after each action, guiding the user seamlessly.

## How to Run the Application

**Demo Video:** [Link to Demo Video - Coming Soon!]

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd hackathon-todo
    ```
2.  **Create and activate a virtual environment using `uv`:**
    ```bash
    uv venv
    .\.venv\Scripts\activate  # On Windows
    # source .venv/bin/activate # On macOS/Linux
    ```
3.  **Install dependencies:**
    ```bash
    uv pip install colorama
    ```
4.  **Run the application:**
    ```bash
    .\.venv\Scripts\python.exe src/main.py
    ```
    (On Windows, ensure you are in the project root directory when running this command.)

    Follow the on-screen menu to interact with the Todo CLI application.

## CLI Visuals
Here are some templates showcasing the CLI's user interface:

### Main Menu Layout
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

## Architecture Overview
The application follows a clear architectural separation of concerns:

*   **`src/main.py`:** Serves as the application's entry point and orchestrator. It manages the main application loop, handles user input for menu navigation, and delegates control to UI functions (`src/ui.py`) for display and task management functions (`src/tasks.py`) for data operations. It also centralizes error handling and success message display.
*   **`src/ui.py`:** Dedicated to all aspects of the User Interface. This module encapsulates functions for displaying menus, task lists, input prompts, and various messages (success, error, warning). It handles screen clearing and ensures consistent formatting and color usage as defined in the UI/UX requirements.
*   **`src/tasks.py`:** Responsible for the core business logic related to task management. It defines the `Task` class and provides CRUD (Create, Read, Update, Delete) operations, along with functions to mark tasks as complete/incomplete and find tasks by their ID. It operates on an in-memory list of `Task` objects.
*   **`test_todo_cli.py`:** Contains comprehensive unit and integration tests to verify the correct functionality of the CLI application, ensuring adherence to the specified behaviors and UI interactions.
