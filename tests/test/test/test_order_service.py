import pytest
from unittest.mock import patch, MagicMock
from src.models.schemas import CreateOrderDto, UpdateOrderDto, OrderItem
from src.services.order_service import get_all_orders, get_order_by_id, create_order, update_order, delete_order

@pytest.mark.asyncio
class TestOrderService:
    @pytest.fixture
    def setup_orders(self):
        # Reset the orders list before each test
        from src.services.order_service import orders
        orders.clear()
        orders.extend([
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
        ])

    @pytest.mark.asyncio
    async def test_get_all_orders_should_return_all_orders(self, setup_orders):
        # Act
        result = await get_all_orders()

        # Assert
        assert len(result) == 2

    @pytest.mark.asyncio
    async def test_get_order_by_id_should_return_order_when_id_exists(self, setup_orders):
        # Act
        result = await get_order_by_id("1")

        # Assert
        assert result.id == "1"

    @pytest.mark.asyncio
    async def test_get_order_by_id_should_return_none_when_id_does_not_exist(self, setup_orders):
        # Act
        result = await get_order_by_id("3")

        # Assert
        assert result is None

    @pytest.mark.asyncio
    async def test_create_order_should_add_new_order(self, setup_orders):
        # Arrange
        order_data = CreateOrderDto(userId="1", items=[OrderItem(productId="1", quantity=2, price=3500.0)], total=None)

        # Act
        result = await create_order(order_data)

        # Assert
        assert result.id == "3"
        assert len(setup_orders) == 3

    @pytest.mark.asyncio
    async def test_update_order_should_modify_existing_order(self, setup_orders):
        # Arrange
        order_data = UpdateOrderDto(status="completed")

        # Act
        result = await update_order("1", order_data)

        # Assert
        assert result.status == "completed"

    @pytest.mark.asyncio
    async def test_update_order_should_return_none_when_id_does_not_exist(self, setup_orders):
        # Arrange
        order_data = UpdateOrderDto(status="completed")

        # Act
        result = await update_order("3", order_data)

        # Assert
        assert result is None

    @pytest.mark.asyncio
    async def test_delete_order_should_return_true_when_order_deleted(self, setup_orders):
        # Act
        result = await delete_order("1")

        # Assert
        assert result is True
        assert len(setup_orders) == 1

    @pytest.mark.asyncio
    async def test_delete_order_should_return_false_when_order_does_not_exist(self, setup_orders):
        # Act
        result = await delete_order("3")

        # Assert
        assert result is False
        assert len(setup_orders) == 2