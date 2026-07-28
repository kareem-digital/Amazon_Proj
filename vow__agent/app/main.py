"""FastAPI application entrypoint.

Run locally:   uvicorn app.main:app --reload
Docs:          http://localhost:8000/docs
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import api_router
from app.config import get_settings
from app.core.logging import configure_logging

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown.

    Connection pools, the checkpointer and the registry client will be
    initialised here as they land.
    """
    settings = get_settings()
    configure_logging(level=settings.log_level, json_output=not settings.debug)
    logger.info("starting %s in %s environment", settings.app_name, settings.environment)

    # TODO(PLT-03): initialise the Postgres checkpointer
    # TODO(PLT-04): initialise the shared httpx client for VOW API calls

    yield

    logger.info("shutting down %s", settings.app_name)
    # TODO: close pools and clients


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title="Agentic VOW",
        description="Conversational planning agent for CTV campaigns on Amazon DSP.",
        version=__import__("app").__version__,
        lifespan=lifespan,
        docs_url="/docs" if not settings.is_production else None,
        redoc_url=None,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=settings.api_prefix)

    return app


app = create_app()