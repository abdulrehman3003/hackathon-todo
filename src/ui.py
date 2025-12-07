import os
import platform
from colorama import Fore, Style

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
    """Displays a list of tasks in a table format."""
    clear_screen()
    print(Fore.CYAN + "==========================================")
    print("TASK LIST")
    print("==========================================" + Style.RESET_ALL)
    if not tasks:
        print("No tasks found.")
    else:
        print(Fore.YELLOW + f"{{'ID':<4}} {{'Title':<20}} {{'Status':<10}}" + Style.RESET_ALL)
        print("------------------------------------------")
        for task in tasks:
            status = "Completed" if task.completed else "Pending"
            title = (task.description[:17] + '...') if len(task.description) > 20 else task.description
            print(f"{task.id:<4} {title:<20} {status:<10}")
    print("------------------------------------------")
    print(f"Total tasks: {len(tasks)}")
    input("\nPress Enter to return to the main menu...")

def display_update_task_menu(task_id):
    """Displays the UI for updating a task and gets input."""
    clear_screen()
    print(Fore.CYAN + f"==========================================")
    print(Fore.CYAN + f"UPDATE TASK (ID: {task_id})" + Style.RESET_ALL)
    print(Fore.CYAN + f"==========================================" + Style.RESET_ALL)
    new_title = input("Enter new title (leave empty to keep same): ")
    new_description = input("Enter new description (leave empty to keep same): ")
    return new_title, new_description

def display_mark_task_menu():
    """Displays the UI for marking a task as complete/incomplete and gets the task ID."""
    clear_screen()
    print(Fore.CYAN + "==========================================")
    print(Fore.CYAN + "TOGGLE TASK COMPLETION" + Style.RESET_ALL)
    print(Fore.CYAN + "==========================================" + Style.RESET_ALL)
    task_id = input("Enter task ID: ")
    return task_id

def display_delete_task_menu():
    """Displays the UI for deleting a task and gets input."""
    clear_screen()
    print(Fore.CYAN + "==========================================")
    print(Fore.CYAN + "DELETE TASK" + Style.RESET_ALL)
    print(Fore.CYAN + "==========================================" + Style.RESET_ALL)
    task_id = input("Enter task ID to delete: ")
    confirm = input("Confirm deletion (y/n): ").lower()
    return task_id, confirm