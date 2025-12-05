import pytest
from fastapi.testclient import TestClient
from src.routes.car_routes import router
from unittest.mock import patch
from src.models.schemas import CreateCarDto, UpdateCarDto

client = TestClient(router)

@pytest.fixture
def mock_car_controller():
    with patch('src.controllers.car_controller') as mock:
        yield mock

@pytest.mark.asyncio
async def test_get_all_cars(mock_car_controller):
    mock_car_controller.get_all_cars.return_value = [{'id': '1', 'model': 'Toyota'}, {'id': '2', 'model': 'Honda'}]
    
    response = client.get("/api/cars/")
    
    assert response.status_code == 200
    assert response.json() == [{'id': '1', 'model': 'Toyota'}, {'id': '2', 'model': 'Honda'}]

@pytest.mark.asyncio
async def test_get_car_by_id(mock_car_controller):
    mock_car_controller.get_car_by_id.return_value = {'id': '1', 'model': 'Toyota'}
    
    response = client.get("/api/cars/1")
    
    assert response.status_code == 200
    assert response.json() == {'id': '1', 'model': 'Toyota'}

@pytest.mark.asyncio
async def test_create_car(mock_car_controller):
    car_data = CreateCarDto(model='Toyota')
    mock_car_controller.create_car.return_value = {'id': '1', 'model': 'Toyota'}
    
    response = client.post("/api/cars/", json=car_data.dict())
    
    assert response.status_code == 201
    assert response.json() == {'id': '1', 'model': 'Toyota'}

@pytest.mark.asyncio
async def test_update_car(mock_car_controller):
    car_data = UpdateCarDto(model='Honda')
    mock_car_controller.update_car.return_value = {'id': '1', 'model': 'Honda'}
    
    response = client.put("/api/cars/1", json=car_data.dict())
    
    assert response.status_code == 200
    assert response.json() == {'id': '1', 'model': 'Honda'}

@pytest.mark.asyncio
async def test_delete_car(mock_car_controller):
    mock_car_controller.delete_car.return_value = None
    
    response = client.delete("/api/cars/1")
    
    assert response.status_code == 204
    assert response.content == b''