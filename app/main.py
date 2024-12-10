import uvicorn
from fastapi import FastAPI

from app.logger import configure_logger
from app.app import get_app
from app.config import settings



def run_api_app() -> None:
    configure_logger()
    app = FastAPI(docs_url="/docs", openapi_url="/openapi.json", redoc_url="/redoc")
    app.mount(settings.app.app_mount, get_app())
    uvicorn.run(
        app,
        host=settings.app.app_host,
        port=settings.app.app_port,
        log_config=None
    )
