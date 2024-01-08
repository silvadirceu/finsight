from fastapi import APIRouter

from app.api_v1.v1_endpoints import request

api_router = APIRouter()
api_router.include_router(request.router, prefix="/request", tags=["Request"])
