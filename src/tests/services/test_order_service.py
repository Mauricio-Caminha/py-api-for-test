import pytest
from unittest.mock import patch
from src.services.order_service import get_all_orders, get_order_by_id, create_order, update_order, delete_order
from src.models.schemas import CreateOrderDto, UpdateOrderDto, OrderItem, Order

@pytest.mark.asyncio
async def test_get_all_orders():
    """Should return all orders"""
    result = await get_all_orders()
    assert len(result) == 3

@pytest.mark.asyncio
async def test_get_order_by_id_when_exists():
    """Should return order when id exists"""
    result = await get_order_by_id("1")
    assert result is not None
    assert result.id == "1"

@pytest.mark.asyncio
async def test_get_order_by_id_when_not_exists():
    """Should return None when order id does not exist"""
    result = await get_order_by_id("999")
    assert result is None

@pytest.mark.asyncio
async def test_create_order():
    """Should create a new order"""
    order_data = CreateOrderDto(userId="1", items=[OrderItem(productId="1", quantity=2, price=3500.0)], total=7000.0, status=None)
    result = await create_order(order_data)
    assert result.id == "4"
    assert result.userId == "1"
    assert len(result.items) == 1
    assert result.total == 7000.0
    assert result.status == "pending"

@pytest.mark.asyncio
async def test_update_order_when_exists():
    """Should update order when id exists"""
    order_data = UpdateOrderDto(status="completed")
    result = await update_order("1", order_data)
    assert result is not None
    assert result.status == "completed"

@pytest.mark.asyncio
async def test_update_order_when_not_exists():
    """Should return None when order id does not exist"""
    order_data = UpdateOrderDto(status="completed")
    result = await update_order("999", order_data)
    assert result is None

@pytest.mark.asyncio
async def test_delete_order_when_exists():
    """Should delete order when id exists"""
    result = await delete_order("1")
    assert result is True

@pytest.mark.asyncio
async def test_delete_order_when_not_exists():
    """Should return False when order id does not exist"""
    result = await delete_order("999")
    assert result is False