import pytest
from unittest.mock import patch
from src.services.order_service import get_all_orders, get_order_by_id, create_order, update_order, delete_order
from src.models.schemas import CreateOrderDto, UpdateOrderDto, OrderItem, Order

@pytest.mark.asyncio
class TestOrderService:
    
    @pytest.mark.asyncio
    async def test_get_all_orders(self):
        """Should return all orders"""
        result = await get_all_orders()
        assert len(result) == 3
    
    @pytest.mark.asyncio
    async def test_get_order_by_id_when_exists(self):
        """Should return order when id exists"""
        result = await get_order_by_id("1")
        assert result.id == "1"
        assert result.userId == "1"
    
    @pytest.mark.asyncio
    async def test_get_order_by_id_when_not_found(self):
        """Should return None when order not found"""
        result = await get_order_by_id("999")
        assert result is None
    
    @pytest.mark.asyncio
    async def test_create_order_with_valid_data(self):
        """Should create and return new order"""
        order_data = CreateOrderDto(
            userId="3",
            items=[OrderItem(productId="1", quantity=1, price=100.0)],
            total=None,
            status=None
        )
        result = await create_order(order_data)
        assert result.id == "4"  # New order id
        assert result.userId == "3"
        assert len(result.items) == 1
    
    @pytest.mark.asyncio
    async def test_update_order_when_exists(self):
        """Should update and return order when id exists"""
        update_data = UpdateOrderDto(
            status="completed",
            total=7000.0
        )
        result = await update_order("1", update_data)
        assert result.status == "completed"
        assert result.total == 7000.0
    
    @pytest.mark.asyncio
    async def test_update_order_when_not_found(self):
        """Should return None when order not found"""
        update_data = UpdateOrderDto(status="completed")
        result = await update_order("999", update_data)
        assert result is None
    
    @pytest.mark.asyncio
    async def test_delete_order_when_exists(self):
        """Should return True when order deleted"""
        result = await delete_order("1")
        assert result is True
    
    @pytest.mark.asyncio
    async def test_delete_order_when_not_found(self):
        """Should return False when order not found"""
        result = await delete_order("999")
        assert result is False