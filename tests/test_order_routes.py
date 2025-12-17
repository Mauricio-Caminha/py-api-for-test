import pytest
from unittest.mock import Mock, patch
from src.routes.order_routes import router
from fastapi import FastAPI

@pytest.fixture
def mock_order_controller():
    with patch('src.controllers.order_controller') as mock:
        yield mock

@pytest.fixture
def app(mock_order_controller):
    app = FastAPI()
    app.include_router(router)
    return app

@pytest.mark.asyncio
async def test_get_all_orders(app, mock_order_controller):
    # Arrange
    mock_orders = [{'id': '1', 'item': 'Product A'}, {'id': '2', 'item': 'Product B'}]
    mock_order_controller.get_all_orders.return_value = mock_orders

    # Act
    response = await app.get('/api/orders')

    # Assert
    assert response.status_code == 200
    assert response.json() == mock_orders
    mock_order_controller.get_all_orders.assert_called_once()

@pytest.mark.asyncio
async def test_get_order_by_id(app, mock_order_controller):
    # Arrange
    mock_order = {'id': '1', 'item': 'Product A'}
    mock_order_controller.get_order_by_id.return_value = mock_order

    # Act
    response = await app.get('/api/orders/1')

    # Assert
    assert response.status_code == 200
    assert response.json() == mock_order
    mock_order_controller.get_order_by_id.assert_called_once_with('1')

@pytest.mark.asyncio
async def test_create_order(app, mock_order_controller):
    # Arrange
    order_data = {'item': 'Product A'}
    mock_order = {'id': '1', 'item': 'Product A'}
    mock_order_controller.create_order.return_value = mock_order

    # Act
    response = await app.post('/api/orders', json=order_data)

    # Assert
    assert response.status_code == 201
    assert response.json() == mock_order
    mock_order_controller.create_order.assert_called_once_with(order_data)

@pytest.mark.asyncio
async def test_update_order(app, mock_order_controller):
    # Arrange
    order_data = {'item': 'Updated Product A'}
    mock_order = {'id': '1', 'item': 'Updated Product A'}
    mock_order_controller.update_order.return_value = mock_order

    # Act
    response = await app.put('/api/orders/1', json=order_data)

    # Assert
    assert response.status_code == 200
    assert response.json() == mock_order
    mock_order_controller.update_order.assert_called_once_with('1', order_data)

@pytest.mark.asyncio
async def test_delete_order(app, mock_order_controller):
    # Arrange
    mock_order_controller.delete_order.return_value = None

    # Act
    response = await app.delete('/api/orders/1')

    # Assert
    assert response.status_code == 204
    mock_order_controller.delete_order.assert_called_once_with('1')