"""Service interfaces using Protocol."""

from typing import Protocol, Optional
from src.models.schemas import (
    User, CreateUserDto, UpdateUserDto,
    Product, CreateProductDto, UpdateProductDto,
    Car, CreateCarDto, UpdateCarDto,
    Order, CreateOrderDto, UpdateOrderDto
)


class IUserService(Protocol):
    """Interface for User Service."""
    
    async def get_all_users(self) -> list[User]:
        """Get all users."""
        ...
    
    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID."""
        ...
    
    async def create_user(self, user_data: CreateUserDto) -> User:
        """Create a new user."""
        ...
    
    async def update_user(self, user_id: str, user_data: UpdateUserDto) -> Optional[User]:
        """Update an existing user."""
        ...
    
    async def delete_user(self, user_id: str) -> bool:
        """Delete a user."""
        ...


class IProductService(Protocol):
    """Interface for Product Service."""
    
    async def get_all_products(self) -> list[Product]:
        """Get all products."""
        ...
    
    async def get_product_by_id(self, product_id: str) -> Optional[Product]:
        """Get product by ID."""
        ...
    
    async def create_product(self, product_data: CreateProductDto) -> Product:
        """Create a new product."""
        ...
    
    async def update_product(self, product_id: str, product_data: UpdateProductDto) -> Optional[Product]:
        """Update an existing product."""
        ...
    
    async def delete_product(self, product_id: str) -> bool:
        """Delete a product."""
        ...


class ICarService(Protocol):
    """Interface for Car Service."""
    
    async def get_all_cars(self) -> list[Car]:
        """Get all cars."""
        ...
    
    async def get_car_by_id(self, car_id: str) -> Optional[Car]:
        """Get car by ID."""
        ...
    
    async def create_car(self, car_data: CreateCarDto) -> Car:
        """Create a new car."""
        ...
    
    async def update_car(self, car_id: str, car_data: UpdateCarDto) -> Optional[Car]:
        """Update an existing car."""
        ...
    
    async def delete_car(self, car_id: str) -> bool:
        """Delete a car."""
        ...


class IOrderService(Protocol):
    """Interface for Order Service."""
    
    async def get_all_orders(self) -> list[Order]:
        """Get all orders."""
        ...
    
    async def get_order_by_id(self, order_id: str) -> Optional[Order]:
        """Get order by ID."""
        ...
    
    async def create_order(self, order_data: CreateOrderDto) -> Order:
        """Create a new order."""
        ...
    
    async def update_order(self, order_id: str, order_data: UpdateOrderDto) -> Optional[Order]:
        """Update an existing order."""
        ...
    
    async def delete_order(self, order_id: str) -> bool:
        """Delete an order."""
        ...
