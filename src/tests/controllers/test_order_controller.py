import pytest
from unittest.mock import patch, AsyncMock
from fastapi import HTTPException
from src.controllers.order_controller import (
    get_all_orders,
    get_order_by_id,
    create_order,
    update_order,
    delete_order
)
from src.models.schemas import Order, CreateOrderDto, UpdateOrderDto, OrderItem

@pytest.mark.asyncio
class TestOrderController:
    
    @patch('src.services.order_service.get_all_orders', new_callable=AsyncMock)
    async def test_get_all_orders(self, mock_get_all_orders):
        """Should return a list of orders"""
        mock_get_all_orders.return_value = [
            Order(
                id="1", 
                userId="1", 
                items=[OrderItem(productId="1", quantity=2, price=100.0)],
                total=200.0,
                status="pending",
                createdAt="2025-11-08T10:00:00Z"
            ),
            Order(
                id="2", 
                userId="2", 
                items=[OrderItem(productId="2", quantity=1, price=50.0)],
                total=50.0,
                status="completed",
                createdAt="2025-11-08T11:00:00Z"
            )
        ]
        
        result = await get_all_orders()
        
        assert len(result) == 2
        assert result[0].userId == "1"
        assert result[0].status == "pending"
    
    @patch('src.services.order_service.get_order_by_id', new_callable=AsyncMock)
    async def test_get_order_by_id_when_exists(self, mock_get_order_by_id):
        """Should return order when id exists"""
        mock_order = Order(
            id="1", 
            userId="1", 
            items=[OrderItem(productId="1", quantity=2, price=100.0)],
            total=200.0,
            status="pending",
            createdAt="2025-11-08T10:00:00Z"
        )
        mock_get_order_by_id.return_value = mock_order
        
        result = await get_order_by_id("1")
        
        assert result.id == "1"
        assert result.userId == "1"
        assert result.total == 200.0
    
    @patch('src.services.order_service.get_order_by_id', new_callable=AsyncMock)
    async def test_get_order_by_id_when_not_exists(self, mock_get_order_by_id):
        """Should raise HTTPException when order not found"""
        mock_get_order_by_id.return_value = None
        
        with pytest.raises(HTTPException) as exc_info:
            await get_order_by_id("999")
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Order not found"
    
    @patch('src.services.order_service.create_order', new_callable=AsyncMock)
    async def test_create_order(self, mock_create_order):
        """Should create a new order"""
        order_data = CreateOrderDto(
            userId="1", 
            items=[OrderItem(productId="1", quantity=2, price=100.0)],
            total=200.0
        )
        mock_order = Order(
            id="1", 
            userId="1", 
            items=[OrderItem(productId="1", quantity=2, price=100.0)],
            total=200.0,
            status="pending",
            createdAt="2025-11-08T10:00:00Z"
        )
        mock_create_order.return_value = mock_order
        
        result = await create_order(order_data)
        
        assert result.id == "1"
        assert result.userId == "1"
        assert result.total == 200.0
    
    @patch('src.services.order_service.update_order', new_callable=AsyncMock)
    async def test_update_order_when_exists(self, mock_update_order):
        """Should update order when id exists"""
        order_data = UpdateOrderDto(status="completed")
        mock_order = Order(
            id="1", 
            userId="1", 
            items=[OrderItem(productId="1", quantity=2, price=100.0)],
            total=200.0,
            status="completed",
            createdAt="2025-11-08T10:00:00Z"
        )
        mock_update_order.return_value = mock_order
        
        result = await update_order("1", order_data)
        
        assert result.id == "1"
        assert result.status == "completed"
    
    @patch('src.services.order_service.update_order', new_callable=AsyncMock)
    async def test_update_order_when_not_exists(self, mock_update_order):
        """Should raise HTTPException when order not found"""
        order_data = UpdateOrderDto(status="completed")
        mock_update_order.return_value = None
        
        with pytest.raises(HTTPException) as exc_info:
            await update_order("999", order_data)
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Order not found"
    
    @patch('src.services.order_service.delete_order', new_callable=AsyncMock)
    async def test_delete_order_when_exists(self, mock_delete_order):
        """Should delete order when id exists"""
        mock_delete_order.return_value = True
        
        result = await delete_order("1")
        
        assert result == {"message": "Order deleted successfully"}
    
    @patch('src.services.order_service.delete_order', new_callable=AsyncMock)
    async def test_delete_order_when_not_exists(self, mock_delete_order):
        """Should raise HTTPException when order not found"""
        mock_delete_order.return_value = False
        
        with pytest.raises(HTTPException) as exc_info:
            await delete_order("999")
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Order not found"
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Order not found"