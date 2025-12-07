from tasks import add_task, view_tasks, update_task, mark_task, delete_task, find_task_by_id
from ui import display_main_menu, clear_screen, display_add_task_menu, display_tasks, display_update_task_menu, display_mark_task_menu, display_delete_task_menu
from colorama import Fore, Style
import time

def handle_add_task():
    """Handles the logic for adding a new task."""
    title, description = display_add_task_menu()
    if title:
        # The spec requires a description, but the UI provides a title and description.
        # We will concatenate them for now.
        full_description = f"{title}: {description}"
        task = add_task(full_description) # add_task returns None if description is empty, handle this
        if task:
            print(Fore.GREEN + f"Task {task.id}: '{task.description}' added successfully!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Error: Task description cannot be empty." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Task title cannot be empty." + Style.RESET_ALL)
    time.sleep(2)

def handle_view_tasks():
    """Handles the logic for viewing all tasks."""
    all_tasks = view_tasks()
    display_tasks(all_tasks)

def handle_update_task():
    """Handles the logic for updating a task."""
    try:
        clear_screen()
        print(Fore.CYAN + "==========================================")
        print("UPDATE TASK")
        print("==========================================" + Style.RESET_ALL)
        task_id = int(input("Enter task ID to update: "))
        
        existing_task = find_task_by_id(task_id)
        if not existing_task:
            print(Fore.RED + f"Error: Task with ID {task_id} not found." + Style.RESET_ALL)
            time.sleep(2)
            return

        new_title, new_description = display_update_task_menu(task_id)

        final_description = existing_task.description
        if new_title.strip() or new_description.strip():
            updated_title = new_title if new_title.strip() else existing_task.description.split(': ')[0] if ': ' in existing_task.description else existing_task.description
            updated_description = new_description if new_description.strip() else existing_task.description.split(': ')[1] if ': ' in existing_task.description else ""
            final_description = f"{updated_title}: {updated_description}"
            
            task = update_task(task_id, final_description)
            if task:
                print(Fore.GREEN + "Task updated successfully!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Error: Could not update task." + Style.RESET_ALL)
        else:
            print(Fore.RED + "No changes provided. Task not updated." + Style.RESET_ALL)

    except ValueError:
        print(Fore.RED + "Error: Task ID must be an integer." + Style.RESET_ALL)
    time.sleep(2)

def handle_delete_task():
    """Handles the logic for deleting a task."""
    task_id_str, confirm = display_delete_task_menu()
    if confirm == 'y':
        try:
            task_id = int(task_id_str)
            task = delete_task(task_id)
            if task:
                print(Fore.GREEN + f"Task {task.id}: '{task.description}' deleted successfully!" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Error: Task with ID {task_id} not found." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Error: Task ID must be an integer." + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Task deletion cancelled." + Style.RESET_ALL)
    time.sleep(2)

def handle_mark_task():
    """Handles the logic for marking a task as complete or incomplete."""
    task_id_str = display_mark_task_menu()
    try:
        task_id = int(task_id_str)
        task = find_task_by_id(task_id)
        if task:
            new_status = not task.completed # Toggle the status
            mark_task(task_id, new_status)
            if new_status:
                print(Fore.GREEN + f"Task {task.id} marked as complete!" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + f"Task {task.id} marked as incomplete!" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Error: Task with ID {task_id} not found." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Error: Task ID must be an integer." + Style.RESET_ALL)
    time.sleep(2)

def main():
    """Main function for the Todo CLI application."""
    while True:
        choice = display_main_menu()
        
        if choice == '1':
            handle_add_task()
        elif choice == '2':
            handle_view_tasks()
        elif choice == '3':
            handle_update_task()
        elif choice == '4':
            handle_delete_task()
        elif choice == '5':
            handle_mark_task()
        elif choice == '6':
            print("Exiting Todo application.")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
            time.sleep(2)

if __name__ == "__main__":
    main()
