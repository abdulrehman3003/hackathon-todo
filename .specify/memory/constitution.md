<!--
Sync Impact Report:
- Version change: none -> 1.0.0
- Added Principles:
  - System Behavior: Specs as Source of Truth
  - System Behavior: Code Evolution via Specs
  - System Behavior: Dedicated Feature Specs
  - Architecture: Code Organization
  - Architecture: Clean Architecture
  - Architecture: In-Memory Storage
  - Architecture: Python Console Application
- Added Sections:
  - Core Rule
  - Purpose
  - AI Agent Instructions
  - Project Structure (Required)
- Removed Sections: None
- Templates requiring updates:
  - [ ] .specify/templates/plan-template.md
  - [ ] .specify/templates/spec-template.md
  - [ ] .specify/templates/tasks-template.md
  - [ ] .gemini/commands/sp.adr.toml
  - [ ] .gemini/commands/sp.analyze.toml
  - [ ] .gemini/commands/sp.checklist.toml
  - [ ] .gemini/commands/sp.clarify.toml
  - [ ] .gemini/commands/sp.constitution.toml
  - [ ] .gemini/commands/sp.git.commit_pr.toml
  - [ ] .gemini/commands/sp.implement.toml
  - [ ] .gemini/commands/sp.phr.toml
  - [ ] .gemini/commands/sp.plan.toml
  - [ ] .gemini/commands/sp.specify.toml
  - [ ] .gemini/commands/sp.tasks.toml
- Follow-up TODOs:
  - TODO(RATIFICATION_DATE): Set the initial ratification date for this constitution.
-->
# Constitution – Spec-Driven Development (Hackathon II: Evolution of Todo)

This constitution governs how Phase I of the Todo Application must be designed,
implemented, and evolved using Spec-Driven Development principles.

## Core Rule
**No code may be written manually.**
All implementation must be generated through an AI coding agent (Gemini CLI used in this project), strictly following the specifications.
If the generated code is incorrect, **the spec must be refined**, not the code.

## Purpose
To build a clean, maintainable, in-memory Todo Console Application in Python using
Spec-Driven Development and AI-generated code.

## System Behavior Principles
1. The application must fully follow all requirements defined in the specs located in `/specs`.
2. Specs are the single source of truth.
3. Code must evolve only through updating specifications—not touching source files manually.
4. Each feature must have a dedicated specification file.

## Architectural Principles
1. Code must be organized inside a `src/` directory.
2. Code must follow modular, clean-architecture practices.
3. No external database is allowed in Phase I—tasks must exist **in memory only**.
4. The application must run as a Python **console/CLI** app.

## AI Agent Instructions
1. The AI agent must:
   - Read all spec files before generating or modifying code.
   - Generate only what the specifications demand.
   - Produce deterministic, complete, and runnable code.
   - Follow the folder structure defined in the project.

2. The AI agent may refactor or overwrite files **only when the spec requires it**.

3. The AI agent must not:
   - Add features not defined in specs.
   - Generate unnecessary files.
   - Modify code or logic not tied to a spec requirement.

## Project Structure (Required)
*TODO: Define the required project structure here. The user input was not specific enough.*

## Governance
Amendments to this constitution require team consensus and must be documented. All development activities must adhere to these principles.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2025-12-06