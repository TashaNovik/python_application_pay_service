import uvicorn
from fastapi import FastAPI
from app.app import get_app
from app.config import settings
from app.logger import logger
