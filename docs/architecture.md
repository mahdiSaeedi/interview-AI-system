# Architecture Notes

## Phases

### 1. Question Generation

Input:
- Interview instructions
- Optional audience metadata
- Optional interview goals

Output:
- Ordered list of questions
- Optional rationale and tags

### 2. Interview Conduction

Input:
- Generated interview definition
- User session state
- Prior answers

Output:
- Current question
- Preserved answers
- Session progress

### 3. Answer Analysis

Input:
- Full interview transcript
- Session metadata

Output:
- Qualitative summary
- Themes
- Risks or gaps
- Recommendations

## Backend Modules

- `api/`: HTTP routes
- `agents/`: phase-specific agent classes
- `schemas/`: request and response contracts
- `services/`: storage and orchestration helpers
- `core/`: app configuration

## Frontend Modules

- `pages/`: route-level views
- `features/instructions/`: interview creation
- `features/interview/`: interview experience
- `features/analysis/`: analysis results
- `api/`: HTTP client wrappers

## Suggested Evolution

- Add a workflow manager that coordinates handoff between agents.
- Add a database for interviews, sessions, answers, and analyses.
- Add authentication if interviews must be private.
