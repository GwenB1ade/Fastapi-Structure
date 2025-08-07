import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager

from fastapi import status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

from src.config import settings

from . import exceptions
from .routers.users import router as user_router

logger = logging.getLogger("uvicorn.info")


def create_app() -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        logger.info("The application was successfully launched!")
        yield
        logger.info("The app has been stopped")

    app = FastAPI(
        lifespan=lifespan,
        title="API",
        version="0.0.1",
    )

    @app.get("/", include_in_schema=False)
    async def redirect_to_docs():
        return RedirectResponse("/docs")

    # Middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(SessionMiddleware, secret_key=settings.SESSION_SECRET)

    # Exceptions
    app.add_exception_handler(
        status.HTTP_500_INTERNAL_SERVER_ERROR, exceptions.exception_500
    )

    # Routing
    app.include_router(user_router)

    return app
