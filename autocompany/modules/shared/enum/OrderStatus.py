from enum import StrEnum


class OrderStatus(StrEnum):
    INITIALIZED = "initialized"
    PAYMENT_FAILED = 'payment_failed'
    PAYMENT_REQUIRED = "payment_required"
    TRANSACTION_SUCCESSFUL = "transaction_successful"
    DISPATCHED = "dispatched"
    CANCELLED = "cancelled"
    DELIVERED = "delivered"
