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
    """Displays a list of tasks in a table format with multi-line title and description wrapping."""
    clear_screen()
    print(Fore.CYAN + "================================================================================")
    print("TASK LIST")
    print("================================================================================" + Style.RESET_ALL)
    if not tasks:
        print("No tasks found.")
    else:
        # Adjusted header to exactly 80 chars
        print(Fore.YELLOW + "ID     Title                       Description                      Status  " + Style.RESET_ALL) 
        print("--------------------------------------------------------------------------------") # Ruler updated to 80 chars
        for task in tasks:
            status = "Completed" if task.completed else "Pending"
            
            wrapped_title = textwrap.wrap(task.title, width=25)
            wrapped_description = textwrap.wrap(task.description, width=30)
            
            max_lines = max(len(wrapped_title), len(wrapped_description))
            
            for i in range(max_lines):
                id_part = str(task.id) if i == 0 else ''
                status_part = status if i == 0 else ''

                title_part = wrapped_title[i] if i < len(wrapped_title) else ''
                description_part = wrapped_description[i] if i < len(wrapped_description) else ''
                
                # Format each part to its column width
                # Total line length: 4 (ID) + 3 (space) + 25 (Title) + 3 (space) + 30 (Description) + 3 (space) + 10 (Status) + 2 (trailing space) = 80 chars
                print(f"{id_part:<4}   {title_part:<25}   {description_part:<30}   {status_part:<10}  ")
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
