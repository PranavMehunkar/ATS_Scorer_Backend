import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.config import(
    ALLOWED_ORIGINS, 
    APP_DESCRIPTION, 
    APP_TITLE, 
    APP_VERSION, 
    SPACY_MODEL_PRIMARY, 
    SPACY_MODEL_SECONDARY, SENTENCE_TRANSFORMER_MODEL
)
from backend.api.routes import router

logger=logging.getLogger('ats_resume_scorer')

@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Starting ATS Resume Analyzer API...")

    import spacy

    try:
        logger.info(f"Loading spaCy model: {SPACY_MODEL_PRIMARY}")

        app.state.nlp = spacy.load(SPACY_MODEL_PRIMARY)

        logger.info(f"Loaded {SPACY_MODEL_PRIMARY}")

    except Exception as e:

        logger.warning(
            f"Failed loading {SPACY_MODEL_PRIMARY}: {e}"
        )

        logger.info(
            f"Falling back to {SPACY_MODEL_SECONDARY}"
        )

        app.state.nlp = spacy.load(SPACY_MODEL_SECONDARY)

    # Load sentence transformer safely
    try:

        from sentence_transformers import SentenceTransformer

        logger.info(
            f"Loading SentenceTransformer: "
            f"{SENTENCE_TRANSFORMER_MODEL}"
        )

        app.state.embedder = SentenceTransformer(
            SENTENCE_TRANSFORMER_MODEL
        )

        logger.info("SentenceTransformer loaded successfully")

    except Exception as e:

        logger.error(f"Failed loading embedder: {e}")

        # Prevent crash
        app.state.embedder = None

    logger.info("API startup complete")

    yield

    logger.info("Shutting down API")

@app.get('/')
async def root():
    return {
        'name':      'ATS Resume Analyzer API',
        'version':   '2.0.0',
        'endpoints': {
            'POST   /api/v1/analyze-resume': 'Analyze a resume',
            'GET    /api/v1/history':        'Get user history',
            'DELETE /api/v1/history/:id':    'Delete a history entry',
            'GET    /api/v1/health':         'Health check',
            'POST   /api/v1/generate-pdf':   'Generate PDF report from data',
        },
    }

if __name__=='__main__':
    import uvicorn
    uvicorn.run(
        'backend.main:app',
        host    = '0.0.0.0',
        port    = 8000,
        reload  = True,    # Auto-restart on code changes (dev only)
    )
