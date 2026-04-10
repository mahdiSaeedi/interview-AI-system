from fastapi import FastAPI

from app.api.router import api_router


app = FastAPI(
    title="Interview System API",
    version="0.1.0",
    description="Agent-driven interview system backend.",
)

app.include_router(api_router, prefix="/api")


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
