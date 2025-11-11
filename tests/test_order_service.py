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
    order_data = CreateOrderDto(userId="3", items=[OrderItem(productId="1", quantity=1, price=100.0)], total=100.0, status="pending")
    new_order = await create_order(order_data)
    assert new_order.id == "4"  # Assuming 3 existing orders
    assert new_order.userId == "3"
    assert len(await get_all_orders()) == 4

@pytest.mark.asyncio
async def test_update_order_existing():
    update_data = UpdateOrderDto(items=[OrderItem(productId="1", quantity=3, price=100.0)], total=300.0)
    updated_order = await update_order("1", update_data)
    assert updated_order.id == "1"
    assert updated_order.items[0].quantity == 3
    assert updated_order.total == 300.0

@pytest.mark.asyncio
async def test_update_order_non_existing():
    update_data = UpdateOrderDto(items=[OrderItem(productId="1", quantity=3, price=100.0)], total=300.0)
    updated_order = await update_order("999", update_data)
    assert updated_order is None

@pytest.mark.asyncio
async def test_delete_order_existing():
    result = await delete_order("1")
    assert result is True
    assert await get_order_by_id("1") is None
    assert len(await get_all_orders()) == 2  # One less order

@pytest.mark.asyncio
async def test_delete_order_non_existing():
    result = await delete_order("999")
    assert result is False
    assert len(await get_all_orders()) == 3  # No change in order count