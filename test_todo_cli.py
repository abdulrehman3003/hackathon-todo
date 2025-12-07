import unittest
from unittest.mock import patch
import sys
from io import StringIO

# Adjust the path to import from the src directory
sys.path.insert(0, './src')

import tasks
import main

class TestTodoCLI(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        # Clear tasks list before each test
        tasks.tasks.clear()
        tasks.Task.next_id = 1

    def assert_cli_output_sequence(self, mock_stdout, expected_phrases):
        output_str = mock_stdout.getvalue()
        
        # Check if all phrases are present in the output in the given order
        current_index = 0
        for phrase in expected_phrases:
            found_index = output_str.find(phrase, current_index)
            self.assertNotEqual(found_index, -1, f"Expected phrase '{phrase}' not found or not in sequence in output:\n{output_str}")
            current_index = found_index + len(phrase)

    # Common output parts that appear in most CLI interactions (exact match with main.py's print_help)
    initial_help_output = [
        "\nTodo CLI Application", # Added leading newline
        "Commands:",
        "  add <description>         - Add a new task",
        "  list                      - View all tasks",
        "  update <id> <description> - Update a task's description",
        "  complete <id>             - Mark a task as complete",
        "  incomplete <id>           - Mark a task as incomplete",
        "  delete <id>               - Delete a task",
        "  help                      - Show this help message",
        "  exit                      - Exit the application"
    ]

    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task_success_cli(self, mock_stdout):
        with patch('builtins.input', side_effect=['add Buy milk', 'exit']):
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Success: Added task 1: 'Buy milk'",
            "Exiting Todo application."
        ])

    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task_empty_description_cli(self, mock_stdout):
        # Input 'add ' results in args=[], thus printing Usage message from main.py
        with patch('builtins.input', side_effect=['add', 'exit']): # Changed input to 'add'
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Usage: add <description>",
            "Exiting Todo application."
        ])
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task_empty_description_after_parsing_cli(self, mock_stdout):
        # Test case where add_task receives an empty string after parsing
        with patch('builtins.input', side_effect=['add   ', 'exit']): # Input with only spaces
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Usage: add <description>",
            "Exiting Todo application."
        ])


    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['list', 'exit'])
    def test_view_tasks_empty_cli(self, mock_input, mock_stdout):
        main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Your to-do list is empty.",
            "Exiting Todo application."
        ])

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['add Task 1', 'add Task 2', 'list', 'exit'])
    def test_view_tasks_with_items_cli(self, mock_input, mock_stdout):
        main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Success: Added task 1: 'Task 1'",
            "Success: Added task 2: 'Task 2'",
            "\nID    Status  Description",
            "----  ------  -----------",
            "1     [ ]     Task 1",
            "2     [ ]     Task 2",
            "Exiting Todo application."
        ])
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_update_task_success_cli(self, mock_stdout):
        tasks.add_task("Buy milk")
        with patch('builtins.input', side_effect=['update 1 Buy almond milk', 'exit']):
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Success: Updated task 1: 'Buy almond milk'",
            "Exiting Todo application."
        ])

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_task_non_existent_cli(self, mock_stdout):
        with patch('builtins.input', side_effect=['update 999 Non-existent', 'exit']):
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Error: Task with ID 999 not found.",
            "Exiting Todo application."
        ])

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_task_empty_description_cli(self, mock_stdout):
        tasks.add_task("Existing task")
        with patch('builtins.input', side_effect=['update 1 ""', 'exit']): # Corrected input
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Success: Updated task 1: '\"\"'",
            "Exiting Todo application."
        ])
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_update_task_missing_description_cli(self, mock_stdout):
        tasks.add_task("Existing task")
        with patch('builtins.input', side_effect=['update 1', 'exit']): # Input with missing description
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Usage: update <id> <description>",
            "Exiting Todo application."
        ])

    @patch('sys.stdout', new_callable=StringIO)
    def test_mark_task_complete_success_cli(self, mock_stdout):
        tasks.add_task("Finish report")
        with patch('builtins.input', side_effect=['complete 1', 'exit']):
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Success: Marked task 1 as complete.",
            "Exiting Todo application."
        ])

    @patch('sys.stdout', new_callable=StringIO)
    def test_mark_task_incomplete_success_cli(self, mock_stdout):
        tasks.add_task("Completed task")
        tasks.mark_task(1, True) # Mark complete first
        with patch('builtins.input', side_effect=['incomplete 1', 'exit']):
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Success: Marked task 1 as incomplete.",
            "Exiting Todo application."
        ])

    @patch('sys.stdout', new_callable=StringIO)
    def test_mark_task_non_existent_cli(self, mock_stdout):
        with patch('builtins.input', side_effect=['complete 999', 'exit']):
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Error: Task with ID 999 not found.",
            "Exiting Todo application."
        ])

    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_task_success_cli(self, mock_stdout):
        tasks.add_task("Task to delete")
        with patch('builtins.input', side_effect=['delete 1', 'exit']):
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Success: Deleted task 1: 'Task to delete'",
            "Exiting Todo application."
        ])

    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_task_non_existent_cli(self, mock_stdout):
        with patch('builtins.input', side_effect=['delete 999', 'exit']):
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Error: Task with ID 999 not found.",
            "Exiting Todo application."
        ])

    @patch('sys.stdout', new_callable=StringIO)
    def test_unknown_command_cli(self, mock_stdout):
        with patch('builtins.input', side_effect=['unknown_cmd', 'exit']):
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Unknown command: unknown_cmd. Type 'help' for available commands.",
            "Exiting Todo application."
        ])

    @patch('sys.stdout', new_callable=StringIO)
    def test_no_command_entered_cli(self, mock_stdout):
        with patch('builtins.input', side_effect=['', 'exit']): # Simulate just hitting enter
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Error: No command entered. Type 'help' for available commands.",
            "Exiting Todo application."
        ])

    @patch('sys.stdout', new_callable=StringIO)
    def test_task_id_not_integer_cli(self, mock_stdout):
        with patch('builtins.input', side_effect=['update abc new_desc', 'exit']):
            main.main()
        self.assert_cli_output_sequence(mock_stdout, self.initial_help_output + [
            "Error: Task ID must be an integer.",
            "Exiting Todo application."
        ])

if __name__ == '__main__':
    unittest.main(exit=False) # Use exit=False to allow other code to run after tests
