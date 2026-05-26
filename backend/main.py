import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.config import (
    ALLOWED_ORIGINS,
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
    SPACY_MODEL_PRIMARY,
    SPACY_MODEL_SECONDARY,
)

from backend.api.routes import router

logger = logging.getLogger("ats_resume_scorer")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting ATS Resume Analyzer API...")

    import spacy

    try:
        app.state.nlp = spacy.load(SPACY_MODEL_PRIMARY)
        logger.info(f"Loaded {SPACY_MODEL_PRIMARY}")
    except OSError:
        logger.warning(f"{SPACY_MODEL_PRIMARY} not found — using fallback")
        app.state.nlp = spacy.load(SPACY_MODEL_SECONDARY)

    # Temporary lightweight embedder placeholder
    app.state.embedder = None

    yield

    logger.info("Shutting down API...")


# CREATE APP FIRST
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    lifespan=lifespan,
)

# ADD CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# INCLUDE ROUTES
app.include_router(router)


# ROOT ROUTE
@app.get("/")
async def root():
    return {
        "status": "running",
        "message": "ATS Resume Analyzer API"
    }


# HEALTH ROUTE
@app.get("/api/v1/health")
async def health_check(request: Request):
    return {
        "status": "healthy",
        "nlp_loaded": hasattr(request.app.state, "nlp"),
        "embedder_loaded": hasattr(request.app.state, "embedder"),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
    )
