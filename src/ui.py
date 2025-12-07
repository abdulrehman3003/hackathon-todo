import os
import platform
from colorama import Fore, Style
import textwrap

def clear_screen():
    """Clears the console screen."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def display_main_menu():
    """Displays the main menu."""
    clear_screen()
    print(Fore.CYAN + "==========================================")
    print("TODO APPLICATION")
    print("==========================================" + Style.RESET_ALL)
    print("Select an option:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete / Incomplete")
    print("6. Exit")
    print("------------------------------------------")
    choice = input("Enter your choice: ")
    return choice

def display_add_task_menu():
    """Displays the UI for adding a new task and gets input."""
    clear_screen()
    print(Fore.CYAN + "==========================================")
    print("ADD NEW TASK")
    print("==========================================" + Style.RESET_ALL)
    title = input("Enter task title: ")
    description = input("Enter description: ")
    return title, description

def display_tasks(tasks):
    """Displays a list of tasks in a table format with multi-line description wrapping."""
    clear_screen()
    print(Fore.CYAN + "================================================================================")
    print("TASK LIST")
    print("================================================================================" + Style.RESET_ALL)
    if not tasks:
        print("No tasks found.")
    else:
        print(Fore.YELLOW + "ID   Title           Description                           Status" + Style.RESET_ALL)
        print("--------------------------------------------------------------------------------")
        for task in tasks:
            status = "Completed" if task.completed else "Pending"
            
            # Truncate title or pad to 15 characters
            title_display = (task.title[:12] + '...') if len(task.title) > 15 else task.title.ljust(15)

            wrapped_description = textwrap.wrap(task.description, width=40)
            
            
            # Print the first line of the task with ID, Title, first part of Description, and Status
            # ID (7) + Title (18) + Description (43) + Status (10) = 78
            # The extra space in the original output seems to come from the default padding of print
            # Let's align to 78 characters for internal content, and rely on external rules for total line length.
            
            first_line_desc = wrapped_description[0].ljust(43) if wrapped_description else ''.ljust(43)
            
            print(f"{task.id:<7}{title_display:<18}{first_line_desc}{status:<10}")

            # Print subsequent lines of the description, indented
            for line in wrapped_description[1:]:
                # Indentation for subsequent description lines: 7 (ID) + 18 (Title) = 25 spaces
                print(f"{'':<25}{line:<43}")
    print("--------------------------------------------------------------------------------")
    print(f"Total tasks: {len(tasks)}")
    input("\nPress Enter to return to the main menu...")

def display_update_task_menu(task_id):
    """Displays the UI for updating a task and gets input."""
    clear_screen()
    print(Fore.CYAN + f"==========================================")
    print(f"UPDATE TASK (ID: {task_id})")
    print(f"==========================================" + Style.RESET_ALL)
    new_title = input("Enter new title (leave empty to keep same): ")
    new_description = input("Enter new description (leave empty to keep same): ")
    return new_title, new_description

def display_mark_task_menu():
    """Displays the UI for marking a task as complete/incomplete and gets the task ID."""
    clear_screen()
    print(Fore.CYAN + "==========================================")
    print("TOGGLE TASK COMPLETION")
    print("==========================================" + Style.RESET_ALL)
    task_id = input("Enter task ID: ")
    return task_id

def display_delete_task_menu():
    """Displays the UI for deleting a task and gets input."""
    clear_screen()
    print(Fore.CYAN + "==========================================")
    print("DELETE TASK")
    print("==========================================" + Style.RESET_ALL)
    task_id = input("Enter task ID to delete: ")
    confirm = input("Confirm deletion (y/n): ").lower()
    return task_id, confirm