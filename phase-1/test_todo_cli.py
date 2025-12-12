import unittest
from unittest.mock import patch, call
import sys
from io import StringIO

# Adjust the path to import from the src directory
sys.path.insert(0, './src')

import tasks
import main
from ui import clear_screen, display_main_menu
from colorama import Fore, Style

class TestTodoCLI(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        # Clear tasks list before each test
        tasks.tasks.clear()
        tasks.Task.next_id = 1

    def assert_output_contains(self, mock_stdout, expected_phrase):
        output_str = mock_stdout.getvalue()
        self.assertIn(expected_phrase, output_str, f"Expected phrase '{expected_phrase}' not found in output:\n{output_str}")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['6']) # Exit choice
    def test_main_menu_exit(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")
        self.assert_output_contains(mock_stdout, "\nTODO APPLICATION\n")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['7', '6']) # Invalid choice then exit
    def test_main_menu_invalid_choice(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'Buy milk', '2% fat', '6']) # Add task then exit
    def test_add_task_success(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, Fore.GREEN + "Task 1: 'Buy milk' added successfully!" + Style.RESET_ALL)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")
        self.assertEqual(len(tasks.view_tasks()), 1)
        self.assertEqual(tasks.view_tasks()[0].title, "Buy milk")
        self.assertEqual(tasks.view_tasks()[0].description, "2% fat")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', '', '2% fat', '6']) # Add task with empty title
    def test_add_task_empty_input_title(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, Fore.RED + "Error: Title and description cannot be empty." + Style.RESET_ALL)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")
        self.assertEqual(len(tasks.view_tasks()), 0)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'Buy milk', '', '6']) # Add task with empty description
    def test_add_task_empty_input_description(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, Fore.RED + "Error: Title and description cannot be empty." + Style.RESET_ALL)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")
        self.assertEqual(len(tasks.view_tasks()), 0)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['2', '', '6']) # View empty list then exit
    def test_view_tasks_empty(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, "No tasks found.")
        self.assert_output_contains(mock_stdout, "Total tasks: 0")
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'A very long task title that will wrap.', 'This is a very long task description that should wrap around multiple lines in the display table.', '1', 'Another long title for a task.', 'Another very long description that also needs to wrap to show the functionality correctly.', '2', '', '', '6']) # Add two tasks, view, then exit
    def test_view_tasks_with_items(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, "Task 1: 'A very long task title that will wrap.' added successfully!")
        self.assert_output_contains(mock_stdout, "Task 2: 'Another long title for a task.' added successfully!")

        self.assert_output_contains(mock_stdout, Fore.YELLOW + "ID   Title                     Description                    Status  " + Style.RESET_ALL)
        self.assert_output_contains(mock_stdout, "--------------------------------------------------------------------------------")
        self.assert_output_contains(mock_stdout, "1      A very long task title      This is a very long task         Pending     ")
        self.assert_output_contains(mock_stdout, "       that will wrap.             description that should wrap                 ")
        self.assert_output_contains(mock_stdout, "                                   around multiple lines in the                 ")
        self.assert_output_contains(mock_stdout, "                                   display table.                               ")
        self.assert_output_contains(mock_stdout, "2      Another long title for a    Another very long description    Pending     ")
        self.assert_output_contains(mock_stdout, "       task.                       that also needs to wrap to                   ")
        self.assert_output_contains(mock_stdout, "                                   show the functionality                       ")
        self.assert_output_contains(mock_stdout, "                                   correctly.                                   ")
        self.assert_output_contains(mock_stdout, "--------------------------------------------------------------------------------")
        self.assert_output_contains(mock_stdout, "Total tasks: 2")
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'Task One', 'Desc One', '3', '1', 'Updated Title', 'Updated Desc', '6']) # Update task
    def test_update_task_success(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, "Task 1: 'Task One' added successfully!")
        self.assert_output_contains(mock_stdout, "Task updated successfully!")
        self.assertEqual(tasks.view_tasks()[0].title, "Updated Title")
        self.assertEqual(tasks.view_tasks()[0].description, "Updated Desc")
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['3', '999', 'New Title', 'New Desc', '6']) # Update non-existent task
    def test_update_task_non_existent(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, Fore.RED + "Error: Task with ID 999 not found." + Style.RESET_ALL)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'Task One', 'Desc One', '3', '1', '', '', '6']) # Update with empty title/desc
    def test_update_task_empty_input(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, "Task 1: 'Task One' added successfully!")
        self.assert_output_contains(mock_stdout, Fore.RED + "No changes provided. Task not updated." + Style.RESET_ALL)
        self.assertEqual(tasks.view_tasks()[0].title, "Task One")
        self.assertEqual(tasks.view_tasks()[0].description, "Desc One")
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['3', 'abc', 'Title', 'Desc', '6']) # Update with invalid ID
    def test_update_task_invalid_id(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, Fore.RED + "Error: Task ID must be an integer." + Style.RESET_ALL)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'Task One', 'Desc One', '5', '1', '6']) # Mark complete
    def test_mark_task_complete_success(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, "Task 1: 'Task One' added successfully!")
        self.assert_output_contains(mock_stdout, Fore.GREEN + "Task 1 marked as complete!" + Style.RESET_ALL)
        self.assertTrue(tasks.view_tasks()[0].completed)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'Task One', 'Desc One', '5', '1', '5', '1', '6']) # Mark complete then incomplete
    def test_mark_task_incomplete_success(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, "Task 1: 'Task One' added successfully!")
        self.assert_output_contains(mock_stdout, Fore.GREEN + "Task 1 marked as complete!" + Style.RESET_ALL)
        self.assert_output_contains(mock_stdout, Fore.YELLOW + "Task 1 marked as incomplete!" + Style.RESET_ALL)
        self.assertFalse(tasks.view_tasks()[0].completed)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['5', '999', '6']) # Mark non-existent task
    def test_mark_task_non_existent(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, Fore.RED + "Error: Task with ID 999 not found." + Style.RESET_ALL)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['5', 'abc', '6']) # Mark with invalid ID
    def test_mark_task_invalid_id(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, Fore.RED + "Error: Task ID must be an integer." + Style.RESET_ALL)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'Task One', 'Desc One', '4', '1', 'y', '6']) # Delete task
    def test_delete_task_success(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, "Task 1: 'Task One' added successfully!")
        self.assert_output_contains(mock_stdout, Fore.GREEN + "Task 1: 'Task One' deleted successfully!" + Style.RESET_ALL)
        self.assertEqual(len(tasks.view_tasks()), 0)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'Task One', 'Desc One', '4', '1', 'n', '6']) # Cancel delete
    def test_delete_task_cancelled(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, Fore.YELLOW + "Task deletion cancelled." + Style.RESET_ALL)
        self.assertEqual(len(tasks.view_tasks()), 1)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['4', '999', 'y', '6']) # Delete non-existent
    def test_delete_task_non_existent(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, Fore.RED + "Error: Task with ID 999 not found." + Style.RESET_ALL)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['4', 'abc', 'y', '6']) # Delete with invalid ID
    def test_delete_task_invalid_id(self, mock_input, mock_stdout):
        main.main()
        self.assert_output_contains(mock_stdout, Fore.RED + "Error: Task ID must be an integer." + Style.RESET_ALL)
        self.assert_output_contains(mock_stdout, "Exiting Todo application.")

if __name__ == '__main__':
    unittest.main(exit=False) # Use exit=False to allow other code to run after tests