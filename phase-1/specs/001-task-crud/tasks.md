# Tasks: 001-task-crud

## Phase 1: Setup
- [x] T001 Install colorama for colored console output
- [x] T002 [P] Create `src/ui.py` for UI-related functions

## Phase 2: Foundational
- [x] T003 Implement a screen clearing function in `src/ui.py` that works for both Windows and other OSes
- [x] T004 Implement the main menu layout in `src/ui.py` as specified in the UI requirements
- [x] T005 [P] Create a function in `src/main.py` to display the main menu and get user input

## Phase 3: User Story 1 - Add a new task (Priority: P1)
- [x] T006 [US1] Implement the "Add Task" UI layout in `src/ui.py`
- [x] T007 [US1] Create a function in `src/main.py` to handle the "Add Task" logic

## Phase 4: User Story 2 - View my to-do list (Priority: P1)
- [x] T008 [US2] Implement the "View Tasks" table layout in `src/ui.py`
- [x] T009 [US2] Create a function in `src/main.py` to handle the "View Tasks" logic

## Phase 5: User Story 3 - Update a task (Priority: P2)
- [x] T010 [US3] Implement the "Update Task" UI layout in `src/ui.py`
- [x] T011 [US3] Create a function in `src/main.py` to handle the "Update Task" logic

## Phase 6: User Story 4 - Mark a task as complete/incomplete (Priority: P2)
- [x] T012 [US4] Implement the "Toggle Task Completion" UI layout in `src/ui.py`
- [x] T013 [US4] Create a function in `src/main.py` to handle the "Mark Complete/Incomplete" logic

## Phase 7: User Story 5 - Delete a task (Priority: P3)
- [x] T014 [US5] Implement the "Delete Task" UI layout in `src/ui.py`
- [x] T015 [US5] Create a function in `src/main.py` to handle the "Delete Task" logic

## Phase 8: Polish & Cross-Cutting Concerns
- [x] T016 Implement input validation for all menu choices in `src/main.py`
- [x] T017 Implement error handling for non-existent task IDs in `src/main.py`
- [x] T018 Ensure all actions return to the main menu after completion
- [x] T019 [P] Add color to all UI elements as specified in the UI requirements in `src/ui.py`
- [x] T020 Review and refactor `src/main.py` and `src/ui.py` for clarity and efficiency

## Dependencies & Execution Order
- **Phase 1** must be completed before **Phase 2**.
- **Phase 2** must be completed before any user story phases.
- All user story phases can be completed independently after **Phase 2**.
- **Phase 8** should be completed after all user stories are implemented.

## Parallel Opportunities
- Tasks marked with [P] can be worked on in parallel.
- Each user story phase can be worked on in parallel by different developers.
