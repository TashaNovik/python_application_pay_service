from typing import Any
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.exceptions import SqlException
from app.models.companies_model import Company
from app.repositories.base_repo import BaseRepo
from app.schemas.company_schemas import CompanySchema



class CompanyRepo(BaseRepo):
    async def get_all(self, session: AsyncSession) -> list[CompanySchema]:
        result = await session.execute(select(Company))
        return [
            CompanySchema.model_validate(company) for company in result.scalars().all()
        ]

    async def add(self, company: Company, session: AsyncSession) -> None:
        try:
            session.add(company)
            await session.commit()
        except SQLAlchemyError as exc:
            await session.rollback()
            raise SqlException(message=str(exc))

    async def get_by_id(self, id_: int, session: AsyncSession) -> None:
        raise NotImplementedError("get_by_id is not implemented for CompanyRepo")


company_repo = CompanyRepo()
