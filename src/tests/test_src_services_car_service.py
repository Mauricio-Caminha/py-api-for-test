import pytest
import pytest_asyncio
from unittest.mock import patch
from src.services.car_service import get_all_cars, get_car_by_id, create_car, update_car, delete_car
from src.models.schemas import Car, CreateCarDto, UpdateCarDto

@pytest.mark.asyncio
class TestCarService:
    
    @pytest_asyncio.fixture(autouse=True)
    async def setup_method(self):
        # Reset the in-memory database before each test
        global cars
        cars = [
            Car(id="1", brand="Toyota", model="Corolla", year=2020, color="White", price=85000.0),
            Car(id="2", brand="Honda", model="Civic", year=2021, color="Black", price=92000.0),
            Car(id="3", brand="Ford", model="Focus", year=2019, color="Red", price=75000.0),
        ]
    
    async def test_get_all_cars(self):
        """Should return all cars"""
        result = await get_all_cars()
        assert len(result) == 3
        assert result[0].brand == "Toyota"
    
    async def test_get_car_by_id_when_exists(self):
        """Should return car when id exists"""
        result = await get_car_by_id("1")
        assert result is not None
        assert result.brand == "Toyota"
    
    async def test_get_car_by_id_when_not_found(self):
        """Should return None when car not found"""
        result = await get_car_by_id("999")
        assert result is None
    
    async def test_create_car_with_valid_data(self):
        """Should create and return new car"""
        car_data = CreateCarDto(brand="Nissan", model="Altima", year=2022, color="Blue", price=95000.0)
        result = await create_car(car_data)
        assert result.id == "4"
        assert result.brand == "Nissan"
        assert len(cars) == 4
    
    async def test_update_car_when_exists(self):
        """Should update and return the car when it exists"""
        update_data = UpdateCarDto(brand="Toyota", model="Camry", year=2021, color="White", price=88000.0)
        result = await update_car("1", update_data)
        assert result is not None
        assert result.model == "Camry"
    
    async def test_update_car_when_not_found(self):
        """Should return None when car not found"""
        update_data = UpdateCarDto(brand="Toyota", model="Camry", year=2021, color="White", price=88000.0)
        result = await update_car("999", update_data)
        assert result is None
    
    async def test_delete_car_when_exists(self):
        """Should return True when car deleted"""
        result = await delete_car("1")
        assert result is True
        assert len(cars) == 2
    
    async def test_delete_car_when_not_found(self):
        """Should return False when car not found"""
        result = await delete_car("999")
        assert result is False
        assert len(cars) == 3