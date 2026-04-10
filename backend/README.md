# Backend

FastAPI service for the interview system.

## App Layers

- `api`: route definitions
- `agents`: phase-specific agent implementations
- `schemas`: typed request and response models
- `services`: persistence and orchestration helpers

## Run Later

This scaffold is intentionally light. Once dependencies are installed, the backend entrypoint will be:

```bash
uvicorn app.main:app --reload
```
