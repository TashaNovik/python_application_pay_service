import uvicorn
from fastapi import FastAPI

from app import logger
from app.app import get_app
from app.config import settings



def run_api_app() -> None:
    #configure_logger()
    logger.info("Run API app")
    app = FastAPI(docs_url=None)
    app.mount(settings.app.app_mount, get_app())
    uvicorn.run(
        app,
        host=settings.app.app_host,
        port=settings.app.app_port,
        log_config=None
    )
