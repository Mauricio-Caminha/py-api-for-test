import pytest
from unittest.mock import patch, AsyncMock
from src.controllers.car_controller import get_all_cars, get_car_by_id, create_car, update_car, delete_car
from src.models.schemas import Car, CreateCarDto, UpdateCarDto
from fastapi import HTTPException, status

@pytest.mark.asyncio
class TestCarController:
    
    @patch('src.services.car_service.get_all_cars', new_callable=AsyncMock)
    async def test_get_all_cars(self, mock_get_all_cars):
        """Should return a list of cars"""
        mock_get_all_cars.return_value = [
            Car(id="1", brand="Toyota", model="Corolla", year=2023, color="White", price=25000.0),
            Car(id="2", brand="Honda", model="Civic", year=2022, color="Black", price=28000.0)
        ]
        
        result = await get_all_cars()
        
        assert len(result) == 2
        assert result[0].brand == "Toyota"
        assert result[0].model == "Corolla"
    
    @patch('src.services.car_service.get_car_by_id', new_callable=AsyncMock)
    async def test_get_car_by_id_when_exists(self, mock_get_car_by_id):
        """Should return car when id exists"""
        mock_get_car_by_id.return_value = Car(
            id="1", 
            brand="Toyota", 
            model="Corolla", 
            year=2023, 
            color="White", 
            price=25000.0
        )
        
        result = await get_car_by_id("1")
        
        assert result.id == "1"
        assert result.brand == "Toyota"
        assert result.model == "Corolla"
    
    @patch('src.services.car_service.get_car_by_id', new_callable=AsyncMock)
    async def test_get_car_by_id_when_not_exists(self, mock_get_car_by_id):
        """Should raise HTTPException when car not found"""
        mock_get_car_by_id.return_value = None
        
        with pytest.raises(HTTPException) as exc_info:
            await get_car_by_id("999")
        
        assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND
        assert exc_info.value.detail == "Car not found"
    
    @patch('src.services.car_service.create_car', new_callable=AsyncMock)
    async def test_create_car(self, mock_create_car):
        """Should create a new car"""
        car_data = CreateCarDto(
            brand="Toyota", 
            model="Corolla", 
            year=2023, 
            color="White", 
            price=25000.0
        )
        mock_create_car.return_value = Car(
            id="1", 
            brand="Toyota", 
            model="Corolla", 
            year=2023, 
            color="White", 
            price=25000.0
        )
        
        result = await create_car(car_data)
        
        assert result.id == "1"
        assert result.brand == "Toyota"
        assert result.model == "Corolla"
    
    @patch('src.services.car_service.update_car', new_callable=AsyncMock)
    async def test_update_car_when_exists(self, mock_update_car):
        """Should update car when id exists"""
        car_data = UpdateCarDto(brand="Toyota Updated", color="Red")
        mock_update_car.return_value = Car(
            id="1", 
            brand="Toyota Updated", 
            model="Corolla", 
            year=2023, 
            color="Red", 
            price=25000.0
        )
        
        result = await update_car("1", car_data)
        
        assert result.id == "1"
        assert result.brand == "Toyota Updated"
        assert result.color == "Red"
    
    @patch('src.services.car_service.update_car', new_callable=AsyncMock)
    async def test_update_car_when_not_exists(self, mock_update_car):
        """Should raise HTTPException when car not found"""
        mock_update_car.return_value = None
        
        with pytest.raises(HTTPException) as exc_info:
            await update_car("999", UpdateCarDto(brand="Nonexistent"))
        
        assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND
        assert exc_info.value.detail == "Car not found"
    
    @patch('src.services.car_service.delete_car', new_callable=AsyncMock)
    async def test_delete_car_when_exists(self, mock_delete_car):
        """Should delete car when id exists"""
        mock_delete_car.return_value = True
        
        result = await delete_car("1")
        
        assert result == {"message": "Car deleted successfully"}
    
    @patch('src.services.car_service.delete_car', new_callable=AsyncMock)
    async def test_delete_car_when_not_exists(self, mock_delete_car):
        """Should raise HTTPException when car not found"""
        mock_delete_car.return_value = False
        
        with pytest.raises(HTTPException) as exc_info:
            await delete_car("999")
        
        assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND
        assert exc_info.value.detail == "Car not found"