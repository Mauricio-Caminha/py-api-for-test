import pytest
from unittest.mock import Mock, patch
from src.routes.car_routes import router
from fastapi import FastAPI

@pytest.fixture
def client():
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)

@pytest.fixture
def mock_car_controller(mocker):
    return mocker.patch('src.controllers.car_controller')

@pytest.mark.asyncio
async def test_get_all_cars(client, mock_car_controller):
    # Arrange
    mock_car_controller.get_all_cars.return_value = [{'id': '1', 'name': 'Car A'}, {'id': '2', 'name': 'Car B'}]

    # Act
    response = await client.get("/api/cars")

    # Assert
    assert response.status_code == 200
    assert response.json() == [{'id': '1', 'name': 'Car A'}, {'id': '2', 'name': 'Car B'}]
    mock_car_controller.get_all_cars.assert_called_once()

@pytest.mark.asyncio
async def test_get_car_by_id(client, mock_car_controller):
    # Arrange
    mock_car_controller.get_car_by_id.return_value = {'id': '1', 'name': 'Car A'}

    # Act
    response = await client.get("/api/cars/1")

    # Assert
    assert response.status_code == 200
    assert response.json() == {'id': '1', 'name': 'Car A'}
    mock_car_controller.get_car_by_id.assert_called_once_with('1')

@pytest.mark.asyncio
async def test_create_car(client, mock_car_controller):
    # Arrange
    car_data = {'name': 'Car C'}
    mock_car_controller.create_car.return_value = {'id': '3', 'name': 'Car C'}

    # Act
    response = await client.post("/api/cars/", json=car_data)

    # Assert
    assert response.status_code == 201
    assert response.json() == {'id': '3', 'name': 'Car C'}
    mock_car_controller.create_car.assert_called_once_with(car_data)

@pytest.mark.asyncio
async def test_update_car(client, mock_car_controller):
    # Arrange
    car_data = {'name': 'Updated Car A'}
    mock_car_controller.update_car.return_value = {'id': '1', 'name': 'Updated Car A'}

    # Act
    response = await client.put("/api/cars/1", json=car_data)

    # Assert
    assert response.status_code == 200
    assert response.json() == {'id': '1', 'name': 'Updated Car A'}
    mock_car_controller.update_car.assert_called_once_with('1', car_data)

@pytest.mark.asyncio
async def test_delete_car(client, mock_car_controller):
    # Arrange
    mock_car_controller.delete_car.return_value = None

    # Act
    response = await client.delete("/api/cars/1")

    # Assert
    assert response.status_code == 204
    mock_car_controller.delete_car.assert_called_once_with('1')