import pytest
from src.services.order_service import get_all_orders, get_order_by_id, create_order, update_order, delete_order
from src.models.schemas import CreateOrderDto, UpdateOrderDto, OrderItem, Order

@pytest.mark.asyncio
async def test_get_all_orders():
    orders = await get_all_orders()
    assert len(orders) == 3

@pytest.mark.asyncio
async def test_get_order_by_id_existing():
    order = await get_order_by_id("1")
    assert order.id == "1"
    assert order.userId == "1"

@pytest.mark.asyncio
async def test_get_order_by_id_non_existing():
    order = await get_order_by_id("999")
    assert order is None

@pytest.mark.asyncio
async def test_create_order():
    order_data = CreateOrderDto(
        userId="3",
        items=[OrderItem(productId="1", quantity=2, price=3500.0)],
        total=None,
        status=None
    )
    new_order = await create_order(order_data)
    assert new_order.id == "4"
    assert new_order.userId == "3"
    assert new_order.total == 7000.0
    assert new_order.status == "pending"

@pytest.mark.asyncio
async def test_update_order_existing():
    update_data = UpdateOrderDto(
        items=[OrderItem(productId="1", quantity=3, price=3500.0)],
        total=10500.0,
        status="completed"
    )
    updated_order = await update_order("1", update_data)
    assert updated_order.id == "1"
    assert updated_order.total == 10500.0
    assert updated_order.status == "completed"

@pytest.mark.asyncio
async def test_update_order_non_existing():
    update_data = UpdateOrderDto(
        items=[OrderItem(productId="1", quantity=3, price=3500.0)],
        total=10500.0,
        status="completed"
    )
    updated_order = await update_order("999", update_data)
    assert updated_order is None

@pytest.mark.asyncio
async def test_delete_order_existing():
    result = await delete_order("1")
    assert result is True
    assert await get_order_by_id("1") is None

@pytest.mark.asyncio
async def test_delete_order_non_existing():
    result = await delete_order("999")
    assert result is False