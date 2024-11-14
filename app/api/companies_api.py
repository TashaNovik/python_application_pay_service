from fastapi import APIRouter
from app.logger import logger

companies_router = APIRouter(tags=["companies"])


@companies_router.get("/")
async def get_all_companies():
    logger.info("MY ENDPOINT")
    return {"message": "get all companies"}


@companies_router.post("/")
async def create_new_company(body: BodySchema):
    return "OK"
