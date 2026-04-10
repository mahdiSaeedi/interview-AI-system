# Interview System

A web-based interview system built with FastAPI and React.

## Goal

This project is structured around three agent-driven phases:

1. Read interview instructions and generate questions.
2. Conduct the interview and preserve answers.
3. Analyze answers and provide qualitative insights.

## Project Layout

```text
backend/
  app/
    agents/
    api/
    core/
    schemas/
    services/
    main.py
frontend/
  src/
    api/
    components/
    features/
    pages/
    types/
docs/
```

## Agent Responsibilities

- `QuestionGenerationAgent`: turns interviewer instructions into a structured question set.
- `InterviewConductorAgent`: sequences questions and captures user responses.
- `AnswerAnalysisAgent`: produces qualitative analysis from completed interview sessions.

## Next Steps

- Implement persistent storage for interview sessions and answers.
- Connect the React UI to the FastAPI endpoints.
- Replace placeholder agent logic with real model and orchestration flows.
