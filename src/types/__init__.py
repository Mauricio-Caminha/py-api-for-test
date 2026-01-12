"""Types, Interfaces and Enums for the application."""

from .enums import OrderStatus, ProductCategory, CarColor, UserRole
from .interfaces import IUserService, IProductService, ICarService, IOrderService
from .types import ServiceResponse, PaginatedResult

__all__ = [
    "OrderStatus",
    "ProductCategory",
    "CarColor",
    "UserRole",
    "IUserService",
    "IProductService",
    "ICarService",
    "IOrderService",
    "ServiceResponse",
    "PaginatedResult",
]
