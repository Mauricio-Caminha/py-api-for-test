import pytest
from unittest.mock import patch
from src.models.schemas import CreateCarDto, UpdateCarDto, Car
from src.services.car_service import get_all_cars, get_car_by_id, create_car, update_car, delete_car

@pytest.mark.asyncio
async def test_get_all_cars():
    cars = await get_all_cars()
    assert len(cars) == 3
    assert cars[0].brand == "Toyota"
    assert cars[1].brand == "Honda"
    assert cars[2].brand == "Ford"

@pytest.mark.asyncio
async def test_get_car_by_id_existing():
    car = await get_car_by_id("1")
    assert car is not None
    assert car.brand == "Toyota"

@pytest.mark.asyncio
async def test_get_car_by_id_non_existing():
    car = await get_car_by_id("999")
    assert car is None

@pytest.mark.asyncio
async def test_create_car():
    car_data = CreateCarDto(brand="Tesla", model="Model 3", year=2022, color="Blue", price=95000.0)
    new_car = await create_car(car_data)
    assert new_car.id == "4"
    assert new_car.brand == "Tesla"
    assert len(await get_all_cars()) == 4

@pytest.mark.asyncio
async def test_update_car_existing():
    update_data = UpdateCarDto(brand="Toyota", model="Camry", year=2021, color="White", price=87000.0)
    updated_car = await update_car("1", update_data)
    assert updated_car is not None
    assert updated_car.model == "Camry"
    assert updated_car.price == 87000.0

@pytest.mark.asyncio
async def test_update_car_non_existing():
    update_data = UpdateCarDto(brand="Nonexistent", model="Model X", year=2022, color="Black", price=120000.0)
    updated_car = await update_car("999", update_data)
    assert updated_car is None

@pytest.mark.asyncio
async def test_delete_car_existing():
    result = await delete_car("1")
    assert result is True
    assert await get_car_by_id("1") is None
    assert len(await get_all_cars()) == 2

@pytest.mark.asyncio
async def test_delete_car_non_existing():
    result = await delete_car("999")
    assert result is False
    assert len(await get_all_cars()) == 3