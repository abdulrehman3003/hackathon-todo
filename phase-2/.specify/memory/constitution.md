<!--
---
Sync Impact Report
---
- **Version Change**: [CONSTITUTION_VERSION] → v1.0.0
- **Summary**: Initial ratification of the project constitution. Replaced the generic template with project-specific principles for the "Hackathon II – Phase 2 (Full-Stack Todo Application)" project.
- **Added Sections**:
    - Core Principles
    - Judging Criteria
    - Governance
- **Removed Sections**:
    - All placeholder sections from the initial template.
- **Templates Requiring Updates**:
    - ✅ `.specify/templates/plan-template.md` - No immediate changes needed; template is general enough.
    - ✅ `.specify/templates/spec-template.md` - No immediate changes needed; template is general enough.
    - ✅ `.specify/templates/tasks-template.md` - No immediate changes needed; template is general enough.
- **Follow-up TODOs**: None.
-->

# Constitution — Spec-Driven Development (SDD)
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

## Governance

- **Version**: v1.0.0
- **Ratification Date**: 2025-12-10
- **Last Amended Date**: 2025-12-10
- **Amendment Process**: Changes MUST be proposed via a pull request, reviewed by at least one other project member, and merged upon approval. All changes MUST be reflected in an incremented version number.
- **Versioning**: This constitution follows Semantic Versioning 2.0.0.
  - **MAJOR** version for incompatible changes (e.g., removing a core principle).
  - **MINOR** version for adding new, backward-compatible principles or sections.
  - **PATCH** version for clarifications, typo fixes, and non-substantive changes.

If a spec conflicts with the constitution, the constitution prevails.