from typing import Optional, Literal
from pydantic import BaseModel, Field
from datetime import datetime
from src.types.enums import OrderStatus, ProductCategory, CarColor


class User(BaseModel):
    id: str
    name: str
    email: str
    age: int


class CreateUserDto(BaseModel):
    name: str
    email: str
    age: int


class UpdateUserDto(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None


class Car(BaseModel):
    id: str
    brand: str
    model: str
    year: int
    color: CarColor
    price: float


class CreateCarDto(BaseModel):
    brand: str
    model: str
    year: int
    color: CarColor
    price: float


class UpdateCarDto(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    color: Optional[CarColor] = None
    price: Optional[float] = None


class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    stock: int
    category: ProductCategory


class CreateProductDto(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    category: ProductCategory


class UpdateProductDto(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category: Optional[ProductCategory] = None


class OrderItem(BaseModel):
    productId: str
    quantity: int
    price: float


class Order(BaseModel):
    id: str
    userId: str
    items: list[OrderItem]
    total: float
    status: OrderStatus
    createdAt: str


class CreateOrderDto(BaseModel):
    userId: str
    items: list[OrderItem]
    total: Optional[float] = None
    status: Optional[OrderStatus] = OrderStatus.PENDING


class UpdateOrderDto(BaseModel):
    userId: Optional[str] = None
    items: Optional[list[OrderItem]] = None
    total: Optional[float] = None
    status: Optional[OrderStatus] = None
    status: Optional[Literal["pending", "processing", "completed", "cancelled"]] = None

