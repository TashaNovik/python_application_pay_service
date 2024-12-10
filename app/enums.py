from enum import Enum


class PaymentStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"