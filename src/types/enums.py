"""Enumerations for the application."""

from enum import Enum


class OrderStatus(str, Enum):
    """Order status enumeration."""
    
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


class ProductCategory(str, Enum):
    """Product category enumeration."""
    
    ELECTRONICS = "Electronics"
    CLOTHING = "Clothing"
    FOOD = "Food"
    BOOKS = "Books"
    TOYS = "Toys"
    HOME = "Home"
    SPORTS = "Sports"
    AUTOMOTIVE = "Automotive"


class CarColor(str, Enum):
    """Car color enumeration."""
    
    WHITE = "White"
    BLACK = "Black"
    RED = "Red"
    BLUE = "Blue"
    SILVER = "Silver"
    GRAY = "Gray"
    GREEN = "Green"
    YELLOW = "Yellow"


class UserRole(str, Enum):
    """User role enumeration."""
    
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"
    MANAGER = "manager"
