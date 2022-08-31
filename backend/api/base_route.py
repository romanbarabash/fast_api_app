from fastapi import APIRouter

from backend.api.version1 import route_users, route_jobs

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/users", tags=["Users"])
api_router.include_router(route_jobs.router, prefix="/job", tags=["Jobs"])
# api_router.include_router(route_login.router, prefix="/login", tags=["login"])
