from tasks import add_task, view_tasks, update_task, mark_task, delete_task

def print_help():
    """Prints the list of available commands."""
    print("\nTodo CLI Application")
    print("Commands:")
    print("  add <description>         - Add a new task")
    print("  list                      - View all tasks")
    print("  update <id> <description> - Update a task's description")
    print("  complete <id>             - Mark a task as complete")
    print("  incomplete <id>           - Mark a task as incomplete")
    print("  delete <id>               - Delete a task")
    print("  help                      - Show this help message")
    print("  exit                      - Exit the application")

def main():
    """Main function for the Todo CLI application."""
    print_help()
    while True:
        try:
            command_line = input("\nTodo> ").strip().split(maxsplit=2)
            command = command_line[0].lower()
            args = command_line[1:]

            if command == "add":
                if len(args) > 0:
                    task = add_task(" ".join(args))
                    if task:
                        print(f"Success: Added task {task.id}: '{task.description}'")
                    else:
                        print("Error: Task description cannot be empty.")
                else:
                    print("Usage: add <description>")
            elif command == "list":
                all_tasks = view_tasks()
                if not all_tasks:
                    print("Your to-do list is empty.")
                else:
                    print("\nID    Status  Description")
                    print("----  ------  -----------")
                    for task in all_tasks:
                        status = "✓" if task.completed else " "
                        print(f"{task.id:<4}  [{status}]     {task.description}")
            elif command == "update":
                if len(args) == 2:
                    try:
                        task_id = int(args[0])
                        task = update_task(task_id, args[1])
                        if task:
                            print(f"Success: Updated task {task.id}: '{task.description}'")
                        else:
                            # This implies either task not found or empty description
                            if not args[1].strip():
                                print("Error: New task description cannot be empty.")
                            else:
                                print(f"Error: Task with ID {task_id} not found.")
                    except ValueError:
                        print("Error: Task ID must be an integer.")
                else:
                    print("Usage: update <id> <description>")
            elif command == "complete":
                if len(args) == 1:
                    try:
                        task_id = int(args[0])
                        task = mark_task(task_id, True)
                        if task:
                            print(f"Success: Marked task {task.id} as complete.")
                        else:
                            print(f"Error: Task with ID {task_id} not found.")
                    except ValueError:
                        print("Error: Task ID must be an integer.")
                else:
                    print("Usage: complete <id>")
            elif command == "incomplete":
                if len(args) == 1:
                    try:
                        task_id = int(args[0])
                        task = mark_task(task_id, False)
                        if task:
                            print(f"Success: Marked task {task.id} as incomplete.")
                        else:
                            print(f"Error: Task with ID {task_id} not found.")
                    except ValueError:
                        print("Error: Task ID must be an integer.")
                else:
                    print("Usage: incomplete <id>")
            elif command == "delete":
                if len(args) == 1:
                    try:
                        task_id = int(args[0])
                        task = delete_task(task_id)
                        if task:
                            print(f"Success: Deleted task {task.id}: '{task.description}'")
                        else:
                            print(f"Error: Task with ID {task_id} not found.")
                    except ValueError:
                        print("Error: Task ID must be an integer.")
                else:
                    print("Usage: delete <id>")
            elif command == "help":
                print_help()
            elif command == "exit":
                print("Exiting Todo application.")
                break
            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")
        except IndexError:
            print("Error: No command entered. Type 'help' for available commands.")
        except EOFError: # Handle Ctrl+D or Ctrl+Z
            print("\nExiting Todo application.")
            break

if __name__ == "__main__":
    main()