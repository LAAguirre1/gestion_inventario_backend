from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router.api import api_router
from app.utils.config import settings

app = FastAPI(
    title=settings.project_name, openapi_url=f"{settings.api_v1_str}/openapi.json"
)


# Set all CORS enabled origins
if settings.backend_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.backend_cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.api_v1_str) 