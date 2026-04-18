import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import fetch

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

app = FastAPI(
    title="Session Summary Fetch API",
    description="Public API to fetch saved session summaries from the database.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(fetch.router, prefix="/api/v1")


@app.get("/", tags=["Root"], summary="API info")
def root():
    return {
        "name": "Session Summary Fetch API",
        "version": "1.0.0",
        "status": "running",
        "author": "Chouhdry Rizwan",
        "docs": "/docs",
        "endpoints": {
            "fetch_summary": "/api/v1/records/fetch?semester=...&book_name=...&session_number=...",
        },
    }