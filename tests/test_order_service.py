import pytest
from unittest.mock import Mock, patch
from src.services.order_service import get_all_orders, get_order_by_id, create_order, update_order, delete_order
from src.models.schemas import CreateOrderDto, UpdateOrderDto, OrderItem
from src.types.enums import OrderStatus

@pytest.mark.asyncio
async def test_get_all_orders():
    # Act
    result = await get_all_orders()

    # Assert
    assert len(result) == 3

@pytest.mark.asyncio
async def test_get_order_by_id_should_return_order_when_id_exists():
    # Act
    result = await get_order_by_id("1")

    # Assert
    assert result.id == "1"
    assert result.userId == "1"

@pytest.mark.asyncio
async def test_get_order_by_id_should_return_none_when_id_does_not_exist():
    # Act
    result = await get_order_by_id("999")

    # Assert
    assert result is None

@pytest.mark.asyncio
async def test_create_order_should_add_new_order():
    # Arrange
    order_data = CreateOrderDto(userId="3", items=[OrderItem(productId="4", quantity=1, price=100.0)], total=100.0)

    # Act
    result = await create_order(order_data)

    # Assert
    assert result.id == "4"  # Assuming this is the next ID
    assert result.userId == "3"
    assert len(await get_all_orders()) == 4

@pytest.mark.asyncio
async def test_update_order_should_modify_existing_order():
    # Arrange
    update_data = UpdateOrderDto(items=[OrderItem(productId="1", quantity=3, price=3500.0)], status=OrderStatus.COMPLETED)

    # Act
    result = await update_order("1", update_data)

    # Assert
    assert result.id == "1"
    assert result.items[0].quantity == 3
    assert result.status == OrderStatus.COMPLETED

@pytest.mark.asyncio
async def test_update_order_should_return_none_when_order_does_not_exist():
    # Arrange
    update_data = UpdateOrderDto(items=[OrderItem(productId="1", quantity=3, price=3500.0)])

    # Act
    result = await update_order("999", update_data)

    # Assert
    assert result is None

@pytest.mark.asyncio
async def test_delete_order_should_return_true_when_order_deleted():
    # Act
    result = await delete_order("1")

    # Assert
    assert result is True
    assert len(await get_all_orders()) == 2  # One order should be deleted

@pytest.mark.asyncio
async def test_delete_order_should_return_false_when_order_does_not_exist():
    # Act
    result = await delete_order("999")

    # Assert
    assert result is False
    assert len(await get_all_orders()) == 2  # No orders should be deleted