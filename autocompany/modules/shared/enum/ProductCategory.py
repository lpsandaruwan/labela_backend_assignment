from enum import StrEnum


class ProductCategory(StrEnum):
    ENGINE_SYSTEM = "engine_system"
    POWER_TRAIN = "power_train"
    BRAKING_SYSTEM = "braking_system"
    STEERING_SYSTEM = "steering_system"
    SUSPENSION = "suspension"
    TIRES = "tires"
    ELECTRONICS = "electronics"
    EXHAUST_SYSTEM = "exhaust_system"
    OTHER = "other"
