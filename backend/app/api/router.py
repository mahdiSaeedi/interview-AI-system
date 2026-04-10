from fastapi import APIRouter

from app.api.routes import analysis, interview, instructions


api_router = APIRouter()
api_router.include_router(instructions.router, prefix="/instructions", tags=["instructions"])
api_router.include_router(interview.router, prefix="/interview", tags=["interview"])
api_router.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
