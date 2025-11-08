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
from src.models.schemas import Order, CreateOrderDto, UpdateOrderDto

@pytest.mark.asyncio
class TestOrderController:
    
    @patch('src.services.order_service.get_all_orders', new_callable=AsyncMock)
    async def test_get_all_orders(self, mock_get_all_orders):
        """Should return a list of orders"""
        mock_get_all_orders.return_value = [Order(id="1", item="Product A"), Order(id="2", item="Product B")]
        
        result = await get_all_orders()
        
        assert len(result) == 2
        assert result[0].item == "Product A"
    
    @patch('src.services.order_service.get_order_by_id', new_callable=AsyncMock)
    async def test_get_order_by_id_when_exists(self, mock_get_order_by_id):
        """Should return order when id exists"""
        mock_order = Order(id="1", item="Product A")
        mock_get_order_by_id.return_value = mock_order
        
        result = await get_order_by_id("1")
        
        assert result.id == "1"
        assert result.item == "Product A"
    
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
        order_data = CreateOrderDto(item="Product A")
        mock_order = Order(id="1", item="Product A")
        mock_create_order.return_value = mock_order
        
        result = await create_order(order_data)
        
        assert result.id == "1"
        assert result.item == "Product A"
    
    @patch('src.services.order_service.update_order', new_callable=AsyncMock)
    async def test_update_order_when_exists(self, mock_update_order):
        """Should update order when id exists"""
        order_data = UpdateOrderDto(item="Updated Product A")
        mock_order = Order(id="1", item="Updated Product A")
        mock_update_order.return_value = mock_order
        
        result = await update_order("1", order_data)
        
        assert result.id == "1"
        assert result.item == "Updated Product A"
    
    @patch('src.services.order_service.update_order', new_callable=AsyncMock)
    async def test_update_order_when_not_exists(self, mock_update_order):
        """Should raise HTTPException when order not found"""
        order_data = UpdateOrderDto(item="Updated Product A")
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