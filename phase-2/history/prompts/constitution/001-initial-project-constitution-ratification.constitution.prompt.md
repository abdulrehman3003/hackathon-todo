---
id: 001
title: Initial Project Constitution Ratification
stage: constitution
date: 2025-12-10
surface: agent
model: gemini-pro
feature: none
branch: master
user: USER
command: /sp.constitution
labels: [constitution, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

/sp.constitution # Constitution — Spec-Driven Development (SDD)
# Hackathon II – Phase 2 (Full-Stack Todo Application)

This constitution is the single source of governance for all phases of this project.
All code, tests, documentation, and infrastructure MUST conform to the rules below.

## Core Principles
1. SPEC-FIRST: No code is written or modified without a corresponding spec under /specs. Specs are authoritative.
2. AI-GENERATED: Code should be generated from specs using an AI coding agent (Gemini CLI or equivalent). Manual edits are permitted only to fix generation/runtime issues and must be recorded in specs_history (with reason).
3. NO TAILWIND: Frontend uses pure CSS — variables, global stylesheet, component-level CSS files. No Tailwind, Bootstrap, or external CSS frameworks.
4. UV PROJECT: Backend must use `uv` as the project manager (uv venv, uv add, uv run, uv lock).
5. TESTS: Automated tests are required for backend coverage of all API behaviors and critical flows. Frontend tests are recommended.
6. SDD PROCESS: Workflow = constitution → spec → generate code → tests → iterate (update spec) → regenerate.
7. SUBMISSION ARTIFACTS: For hackathon submission include: /specs, /specs_history, constitution.md, backend/, frontend/, README.md (with SDD summary), demo video link, and test run results.
8. SECURITY: Secrets must never be committed. Use .env (with .env.example checked in). JWT_SECRET must be >=32 chars.

## Judging Criteria (mapped to Constitution)
- Correctness (implements spec): 35%
- SDD Compliance & Traceability (specs_history + constitution + process): 20%
- Code Quality & Tests: 15%
- UI/UX & polish (frontend): 15%
- Documentation & Demo readiness: 15%

If a spec conflicts with the constitution, the constitution prevails.

## Response snapshot

Constitution updated to v1.0.0 and saved to `.specify/memory/constitution.md`. A Prompt History Record (PHR) was created.

## Outcome

- ✅ Impact: Established the initial project constitution, setting governance and core principles.
- 🧪 Tests: n/a
- 📁 Files: 
  - `.specify/memory/constitution.md` (overwritten)
  - `history/prompts/constitution/001-initial-project-constitution-ratification.constitution.prompt.md` (created)
- 🔁 Next prompts: n/a
- 🧠 Reflection: The process followed the user request and internal directives correctly, handling file creation, versioning, and record-keeping.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): n/a
