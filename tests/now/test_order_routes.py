import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from src.routes.order_routes import router

client = TestClient(router)

@pytest.fixture
def mock_order_controller():
    with patch("src.controllers.order_controller") as mock:
        yield mock

@pytest.mark.asyncio
async def test_get_all_orders(mock_order_controller):
    mock_order_controller.get_all_orders.return_value = [{"id": "1", "item": "Test Order"}]
    
    response = client.get("/api/orders/")
    
    assert response.status_code == 200
    assert response.json() == [{"id": "1", "item": "Test Order"}]

@pytest.mark.asyncio
async def test_get_order_by_id(mock_order_controller):
    mock_order_controller.get_order_by_id.return_value = {"id": "1", "item": "Test Order"}
    
    response = client.get("/api/orders/1")
    
    assert response.status_code == 200
    assert response.json() == {"id": "1", "item": "Test Order"}

@pytest.mark.asyncio
async def test_create_order(mock_order_controller):
    mock_order_controller.create_order.return_value = {"id": "1", "item": "Test Order"}
    order_data = {"item": "Test Order"}
    
    response = client.post("/api/orders/", json=order_data)
    
    assert response.status_code == 201
    assert response.json() == {"id": "1", "item": "Test Order"}

@pytest.mark.asyncio
async def test_update_order(mock_order_controller):
    mock_order_controller.update_order.return_value = {"id": "1", "item": "Updated Order"}
    order_data = {"item": "Updated Order"}
    
    response = client.put("/api/orders/1", json=order_data)
    
    assert response.status_code == 200
    assert response.json() == {"id": "1", "item": "Updated Order"}

@pytest.mark.asyncio
async def test_delete_order(mock_order_controller):
    mock_order_controller.delete_order.return_value = None
    
    response = client.delete("/api/orders/1")
    
    assert response.status_code == 204
    assert response.content == b""