from enum import StrEnum


class TransactionType(StrEnum):
    CHARGE = "charge"
    REFUND = "refund"
