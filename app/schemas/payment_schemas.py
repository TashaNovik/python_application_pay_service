from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from app.enums import PaymentStatus


class PaymentSchema(BaseModel):
    user_id: str
    payment_id: str
    amount: Decimal
    email: str | None
    type: str | None
    company_id: int
    model_config = ConfigDict(from_attributes=True)

class PaymentResultSchema(BaseModel):
    payment_status: PaymentStatus
    payment_id: str
