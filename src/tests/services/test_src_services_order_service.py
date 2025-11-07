import pytest
import pytest_asyncio
from src.services.order_service import get_all_orders, get_order_by_id, create_order, update_order, delete_order
from src.models.schemas import CreateOrderDto, UpdateOrderDto, OrderItem

@pytest_asyncio.fixture(autouse=True)
async def reset_orders():
    # Reset the orders list before each test
    global orders
    orders = [
        Order(
            id="1",
            userId="1",
            items=[OrderItem(productId="1", quantity=2, price=3500.0)],
            total=7000.0,
            status="pending",
            createdAt="2025-11-07T18:18:08.792Z",
        ),
        Order(
            id="2",
            userId="2",
            items=[OrderItem(productId="2", quantity=1, price=150.0)],
            total=150.0,
            status="completed",
            createdAt="2025-11-07T18:18:08.792Z",
        ),
        Order(
            id="3",
            userId="1",
            items=[OrderItem(productId="3", quantity=1, price=450.0)],
            total=450.0,
            status="processing",
            createdAt="2025-11-07T18:18:08.792Z",
        ),
    ]

@pytest.mark.asyncio
async def test_get_all_orders():
    orders = await get_all_orders()
    assert len(orders) == 3

@pytest.mark.asyncio
async def test_get_order_by_id_existing():
    order = await get_order_by_id("1")
    assert order.id == "1"

@pytest.mark.asyncio
async def test_get_order_by_id_non_existing():
    order = await get_order_by_id("999")
    assert order is None

@pytest.mark.asyncio
async def test_create_order():
    order_data = CreateOrderDto(userId="1", items=[OrderItem(productId="1", quantity=1, price=100.0)], total=100.0)
    new_order = await create_order(order_data)
    assert new_order.id == "4"
    assert new_order.userId == "1"
    assert len(orders) == 4

@pytest.mark.asyncio
async def test_update_order_existing():
    update_data = UpdateOrderDto(status="completed")
    updated_order = await update_order("1", update_data)
    assert updated_order.status == "completed"

@pytest.mark.asyncio
async def test_update_order_non_existing():
    update_data = UpdateOrderDto(status="completed")
    updated_order = await update_order("999", update_data)
    assert updated_order is None

@pytest.mark.asyncio
async def test_delete_order_existing():
    result = await delete_order("1")
    assert result is True
    assert len(orders) == 2

@pytest.mark.asyncio
async def test_delete_order_non_existing():
    result = await delete_order("999")
    assert result is False
    assert len(orders) == 3