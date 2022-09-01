from fastapi import APIRouter

from backend.api.routes import route_users, route_jobs, route_login

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/users", tags=["Users"])
api_router.include_router(route_jobs.router, prefix="/job", tags=["Jobs"])
api_router.include_router(route_login.router, prefix="/login", tags=["Login"])
