from sqlalchemy.ext.asyncio import AsyncSession

from app.exceptions import SqlException
from app.repositories.base_repo import BaseRepo
from app.models.payments_model import Payment
from sqlalchemy import select, update
from sqlalchemy.exc import SQLAlchemyError
from app.models.payments_model import Payment
from app.schemas.payment_schemas import PaymentSchema


class PaymentRepo(BaseRepo):
    async def get_all(self, session: AsyncSession) -> list[PaymentSchema] | list:
        result = await session.execute(select(Payment))
        return [
            PaymentSchema.model_validate(payment) for payment in result.scalars().all()
        ]

    async  def add(self, payment: Payment, session: AsyncSession) -> None:
        try:
            session.add(payment)
            await session.commit()
        except SQLAlchemyError as exc:
            await session.rollback()
            raise SqlException(message=str(exc))

payment_repo = PaymentRepo()
