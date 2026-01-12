"""Type definitions for the application."""

from typing import TypeVar, Generic, Optional
from pydantic import BaseModel


T = TypeVar('T')


class ServiceResponse(BaseModel, Generic[T]):
    """Generic service response wrapper."""
    
    success: bool
    data: Optional[T] = None
    message: Optional[str] = None
    error: Optional[str] = None


class PaginatedResult(BaseModel, Generic[T]):
    """Generic paginated result wrapper."""
    
    items: list[T]
    total: int
    page: int
    page_size: int
    total_pages: int


class ErrorDetail(BaseModel):
    """Error detail model."""
    
    code: str
    message: str
    field: Optional[str] = None


class ValidationError(BaseModel):
    """Validation error model."""
    
    errors: list[ErrorDetail]
