from enum import StrEnum


class AppUserType(StrEnum):
    ADMIN_USER = "admin_user"
    CUSTOMER = "customer"
    GUEST_USER = "guest_user"
    PRODUCT_OWNER = "product_owner"
