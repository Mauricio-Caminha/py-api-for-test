import pytest
from unittest.mock import patch, MagicMock
from src.services.order_service import get_all_orders, get_order_by_id, create_order, update_order, delete_order
from src.models.schemas import CreateOrderDto, UpdateOrderDto, OrderItem
from src.types.enums import OrderStatus

@pytest.mark.asyncio
class TestOrderService:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.orders_backup = [
            {
                "id": "1",
                "userId": "1",
                "items": [OrderItem(productId="1", quantity=2, price=3500.0)],
                "total": 7000.0,
                "status": OrderStatus.PENDING,
                "createdAt": "2025-11-07T18:18:08.792Z",
            },
            {
                "id": "2",
                "userId": "2",
                "items": [OrderItem(productId="2", quantity=1, price=150.0)],
                "total": 150.0,
                "status": OrderStatus.COMPLETED,
                "createdAt": "2025-11-07T18:18:08.792Z",
            },
            {
                "id": "3",
                "userId": "1",
                "items": [OrderItem(productId="3", quantity=1, price=450.0)],
                "total": 450.0,
                "status": OrderStatus.PROCESSING,
                "createdAt": "2025-11-07T18:18:08.792Z",
            },
        ]

    async def test_get_all_orders_should_return_all_orders(self):
        # Act
        result = await get_all_orders()

        # Assert
        assert len(result) == len(self.orders_backup)

    async def test_get_order_by_id_should_return_order_when_id_exists(self):
        # Act
        result = await get_order_by_id("1")

        # Assert
        assert result.id == "1"

    async def test_get_order_by_id_should_return_none_when_id_does_not_exist(self):
        # Act
        result = await get_order_by_id("999")

        # Assert
        assert result is None

    async def test_create_order_should_add_order_and_return_it(self):
        # Arrange
        new_order_data = CreateOrderDto(
            userId="3",
            items=[OrderItem(productId="4", quantity=1, price=100.0)],
            total=None,
            status=None,
        )

        # Act
        result = await create_order(new_order_data)

        # Assert
        assert result.userId == "3"
        assert len(await get_all_orders()) == len(self.orders_backup) + 1

    async def test_update_order_should_modify_order_when_id_exists(self):
        # Arrange
        update_data = UpdateOrderDto(
            items=[OrderItem(productId="1", quantity=3, price=3500.0)],
            total=10500.0,
            status=OrderStatus.COMPLETED,
        )

        # Act
        result = await update_order("1", update_data)

        # Assert
        assert result.total == 10500.0
        assert result.status == OrderStatus.COMPLETED

    async def test_update_order_should_return_none_when_id_does_not_exist(self):
        # Arrange
        update_data = UpdateOrderDto()

        # Act
        result = await update_order("999", update_data)

        # Assert
        assert result is None

    async def test_delete_order_should_return_true_when_order_deleted(self):
        # Act
        result = await delete_order("1")

        # Assert
        assert result is True
        assert await get_order_by_id("1") is None

    async def test_delete_order_should_return_false_when_id_does_not_exist(self):
        # Act
        result = await delete_order("999")

        # Assert
        assert result is False