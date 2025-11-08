import pytest
from unittest.mock import patch
from src.services.car_service import get_all_cars, get_car_by_id, create_car, update_car, delete_car
from src.models.schemas import CreateCarDto, UpdateCarDto, Car

@pytest.mark.asyncio
async def test_get_all_cars():
    """Should return all cars"""
    result = await get_all_cars()
    assert len(result) == 3
    assert result[0].brand == "Toyota"

@pytest.mark.asyncio
async def test_get_car_by_id_when_exists():
    """Should return car when id exists"""
    result = await get_car_by_id("1")
    assert result is not None
    assert result.id == "1"

@pytest.mark.asyncio
async def test_get_car_by_id_when_not_exists():
    """Should return None when car id does not exist"""
    result = await get_car_by_id("999")
    assert result is None

@pytest.mark.asyncio
async def test_create_car():
    """Should create a new car"""
    car_data = CreateCarDto(brand="Nissan", model="Altima", year=2022, color="Blue", price=95000.0)
    result = await create_car(car_data)
    assert result.id == "4"
    assert result.brand == "Nissan"
    assert len(await get_all_cars()) == 4

@pytest.mark.asyncio
async def test_update_car_when_exists():
    """Should update car when id exists"""
    update_data = UpdateCarDto(brand="Toyota", model="Camry", year=2021, color="White", price=90000.0)
    result = await update_car("1", update_data)
    assert result is not None
    assert result.model == "Camry"

@pytest.mark.asyncio
async def test_update_car_when_not_exists():
    """Should return None when car id does not exist"""
    update_data = UpdateCarDto(brand="Toyota", model="Camry", year=2021, color="White", price=90000.0)
    result = await update_car("999", update_data)
    assert result is None

@pytest.mark.asyncio
async def test_delete_car_when_exists():
    """Should delete car when id exists"""
    result = await delete_car("1")
    assert result is True
    assert len(await get_all_cars()) == 2

@pytest.mark.asyncio
async def test_delete_car_when_not_exists():
    """Should return False when car id does not exist"""
    result = await delete_car("999")
    assert result is False