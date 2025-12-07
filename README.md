# Todo CLI Application

**Table of Contents**
- [Project Summary](#project-summary)
- [Spec-Driven Development (SDD)](#spec-driven-development-sdd)
- [Phase 1 Features](#phase-1-features)
  - [Core Task Operations](#core-task-operations)
  - [User Interface (CLI)](#user-interface-cli)
- [How to Run the Application](#how-to-run-the-application)
- [Usage Examples](#usage-examples)
- [CLI Visuals](#cli-visuals)
  - [Main Menu Layout](#main-menu-layout)
- [Architecture Overview](#architecture-overview)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact/Support](#contactsupport)

## Project Summary
A simple command-line interface (CLI) application for managing tasks, built using Python. This application allows users to perform basic CRUD (Create, Read, Update, Delete) operations on tasks, along with marking tasks as complete or incomplete, all through an interactive and user-friendly console interface.

## Spec-Driven Development (SDD)
This project was developed using a Spec-Driven Development (SDD) approach, leveraging a `constitution.md` for core principles, detailed `spec` files for feature requirements, AI-generated code, and comprehensive tests. This methodology ensures strict adherence to defined behaviors, consistent UI/UX, and robust functionality. You can trace the evolution of the project's specifications through `specs_history/`, demonstrating iterative refinement from basic requirements to a comprehensive final spec.

## Phase 1 Features

### Core Task Operations
The application supports the following essential task management functionalities:

*   **Add Task (P1 - High Priority):** Allows users to create a new task by providing a title and a detailed description. Tasks are assigned a unique ID automatically. The system ensures that neither the title nor the description can be empty.
*   **View All Tasks (P1 - High Priority):** Presents a clear, formatted table of all active tasks. Each task is displayed with its unique ID, a potentially truncated title, and its current completion status (Pending/Completed). Detailed descriptions are displayed with multi-line wrapping for better readability.
*   **Update Task (P2 - Medium Priority):** Enables users to modify an existing task's title and/or description using its unique ID. Users can choose to update one or both fields, or leave them unchanged. The system handles cases where the task ID is invalid or no changes are provided.
*   **Mark Task Complete/Incomplete (P2 - Medium Priority):** Provides the ability to toggle the completion status of any task by its ID. This helps users track their progress and manage their workload effectively.
*   **Delete Task (P3 - Low Priority):** Offers functionality to permanently remove a task from the list using its ID. A confirmation prompt is included to prevent accidental deletions. The system validates the task ID before proceeding.
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

## Usage Examples

Here are some common interactions with the Todo CLI application:

### 1. Add a New Task
- Select `1` from the main menu.
- Enter a task title (e.g., "Buy Groceries").
- Enter a task description (e.g., "Milk, Eggs, Bread, and Cheese").
- You will see a success message: `Task 1: 'Buy Groceries' added successfully!`

### 2. View All Tasks
- Select `2` from the main menu.
- The application will display a formatted table of all your tasks, including their ID, Title, Description, and Status.
- If there are no tasks, it will display "No tasks found."

### 3. Update a Task
- Select `3` from the main menu.
- Enter the ID of the task you want to update (e.g., `1`).
- Enter a new title (e.g., "Grocery Shopping") or leave it empty to keep the current title.
- Enter a new description (e.g., "Milk, Eggs, Bread, Cheese, and Apples") or leave it empty to keep the current description.
- You will see a success message: `Task updated successfully!`

### 4. Mark Task Complete / Incomplete
- Select `5` from the main menu.
- Enter the ID of the task you want to mark (e.g., `1`).
- The task's status will toggle between "Pending" and "Completed".
- You will see a success message: `Task 1 marked as complete!` or `Task 1 marked as incomplete!`

### 5. Delete a Task
- Select `4` from the main menu.
- Enter the ID of the task you want to delete (e.g., `1`).
- Confirm deletion by typing `y` and pressing Enter. Type `n` to cancel.
- You will see a success message: `Task 1: 'Grocery Shopping' deleted successfully!`

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

## Testing
The project includes a suite of unit and integration tests to ensure the reliability and correctness of the application.

### How to Run Tests
1.  **Ensure you have activated your virtual environment** (see [How to Run the Application](#how-to-run-the-application)).
2.  **Navigate to the project root directory.**
3.  **Run the tests using `unittest`:**
    ```bash
    python -m unittest test_todo_cli.py
    ```
### Testing Strategy
Tests are designed to cover:
-   **Core functionality**: Verifying that each CRUD operation works as expected.
-   **User interface interactions**: Ensuring correct menu display, input prompts, and output messages (including colors and formatting).
-   **Edge cases**: Handling scenarios like empty task lists, non-existent task IDs, and invalid user inputs.
-   **Regression prevention**: Ensuring that new features or bug fixes do not inadvertently break existing functionality.

## Contributing
We welcome contributions to this project! If you'd like to contribute, please follow these steps:
1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and ensure they adhere to the project's coding standards.
4.  Write or update tests to cover your changes.
5.  Submit a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact/Support
For any questions, issues, or support, please open an issue on the [GitHub repository](https://github.com/your-username/your-repository/issues) or contact [your-email@example.com](mailto:your-email@example.com).
