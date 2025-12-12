---
id: 1
title: Establish Project Constitution v1.0.0
stage: constitution
date: 2025-12-06
surface: agent
model: Gemini
feature: none
branch: master
user: AbdulRehman3003
command: /sp.constitution
labels: [constitution, sdd, python]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/tasks-template.md
  - .gemini/commands/sp.constitution.toml
tests:
  - none
---

## Prompt

/sp.constitution # Constitution – Spec-Driven Development (Hackathon II: Evolution of Todo)

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

## Response snapshot

I have successfully updated the project constitution to version 1.0.0. I also updated the project templates to align with the new principles.

## Outcome

- ✅ Impact: Established the foundational principles for the project, ensuring all subsequent development will follow a consistent, spec-driven approach.
- 🧪 Tests: none
- 📁 Files: 
  - `.specify/memory/constitution.md`
  - `.specify/templates/plan-template.md`
  - `.specify/templates/tasks-template.md`
  - `.gemini/commands/sp.constitution.toml`
- 🔁 Next prompts: /sp.specify "New feature"
- 🧠 Reflection: The initial constitution was a generic template. By incorporating the user's specific principles, I've tailored the development process to the project's unique requirements (Python, in-memory, CLI-based). This will guide the AI agent more effectively. The inconsistency in the PHR creation script path highlighted the importance of verifying file paths and having fallback mechanisms.

## Evaluation notes (flywheel)

- Failure modes observed: The initial prompt for `sp.constitution` pointed to a non-existent `bash` script for PHR creation.
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): Update the `sp.phr.toml` to point to the correct script or use the agent-native flow by default if the script is not found.
