from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.payment_repo import payment_repo


class PaymentService:
    def __init__(self):
        self.repo = payment_repo

    async def get_all_payments(self, session: AsyncSession) -> list[PaymentSchema]:
        payments = await self.repo.get_all(session=session)
        return payments

    async def get_payment_by_payment_id(
            self, payment_id: str, session: AsyncSession) -> PaymentSchema | None:
        payment = await self.repo.get_payment_by_payment_id(payment_id=payment_id, session=session)
        return payment
