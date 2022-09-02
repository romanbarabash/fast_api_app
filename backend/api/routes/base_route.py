from fastapi import APIRouter

from backend.api.routes import users, jobs, login

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(jobs.router, prefix="/job", tags=["Jobs"])
api_router.include_router(login.router, prefix="/login", tags=["Login"])
