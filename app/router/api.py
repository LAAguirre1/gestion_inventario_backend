from fastapi import APIRouter

import app.router.endpoints.users as users
import app.router.endpoints.login as login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])