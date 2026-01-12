import pytest
from unittest.mock import Mock, patch
from src.models.schemas import CreateOrderDto, UpdateOrderDto, OrderItem
from src.services.order_service import get_all_orders, get_order_by_id, create_order, update_order, delete_order

@pytest.fixture
def mock_orders():
    return [
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
async def test_get_all_orders(mock_orders):
    global orders
    orders = mock_orders
    result = await get_all_orders()
    assert result == mock_orders

@pytest.mark.asyncio
async def test_get_order_by_id_should_return_order_when_id_exists(mock_orders):
    global orders
    orders = mock_orders
    result = await get_order_by_id("1")
    assert result == mock_orders[0]

@pytest.mark.asyncio
async def test_get_order_by_id_should_return_none_when_id_does_not_exist(mock_orders):
    global orders
    orders = mock_orders
    result = await get_order_by_id("999")
    assert result is None

@pytest.mark.asyncio
async def test_create_order_should_add_order(mock_orders):
    global orders
    orders = mock_orders
    new_order_data = CreateOrderDto(userId="3", items=[OrderItem(productId="4", quantity=1, price=100.0)])
    result = await create_order(new_order_data)
    assert result.userId == "3"
    assert len(orders) == 4  # Check if the order was added

@pytest.mark.asyncio
async def test_update_order_should_return_updated_order_when_id_exists(mock_orders):
    global orders
    orders = mock_orders
    update_data = UpdateOrderDto(status="completed")
    result = await update_order("1", update_data)
    assert result.status == "completed"
    assert result.id == "1"

@pytest.mark.asyncio
async def test_update_order_should_return_none_when_id_does_not_exist(mock_orders):
    global orders
    orders = mock_orders
    update_data = UpdateOrderDto(status="completed")
    result = await update_order("999", update_data)
    assert result is None

@pytest.mark.asyncio
async def test_delete_order_should_return_true_when_id_exists(mock_orders):
    global orders
    orders = mock_orders
    result = await delete_order("1")
    assert result is True
    assert len(orders) == 2  # Check if the order was deleted

@pytest.mark.asyncio
async def test_delete_order_should_return_false_when_id_does_not_exist(mock_orders):
    global orders
    orders = mock_orders
    result = await delete_order("999")
    assert result is False
    assert len(orders) == 3  # Ensure the orders list remains unchanged