import pytest
from unittest.mock import patch, MagicMock
from src.services.car_service import get_all_cars, get_car_by_id, create_car, update_car, delete_car
from src.models.schemas import Car, CreateCarDto, UpdateCarDto
from src.types.enums import CarColor

@pytest.mark.asyncio
async def test_get_all_cars_should_return_all_cars():
    # Act
    result = await get_all_cars()

    # Assert
    assert len(result) == 3
    assert result[0].brand == "Toyota"
    assert result[1].brand == "Honda"
    assert result[2].brand == "Ford"

@pytest.mark.asyncio
async def test_get_car_by_id_should_return_car_when_id_exists():
    # Act
    result = await get_car_by_id("1")

    # Assert
    assert result is not None
    assert result.brand == "Toyota"

@pytest.mark.asyncio
async def test_get_car_by_id_should_return_none_when_id_does_not_exist():
    # Act
    result = await get_car_by_id("999")

    # Assert
    assert result is None

@pytest.mark.asyncio
async def test_create_car_should_add_new_car():
    # Arrange
    car_data = CreateCarDto(brand="Nissan", model="Altima", year=2022, color=CarColor.BLUE, price=95000.0)

    # Act
    result = await create_car(car_data)

    # Assert
    assert result.id == "4"
    assert result.brand == "Nissan"
    assert len(await get_all_cars()) == 4

@pytest.mark.asyncio
async def test_update_car_should_modify_existing_car():
    # Arrange
    update_data = UpdateCarDto(brand="Toyota", model="Camry", year=2021, color=CarColor.BLACK, price=88000.0)

    # Act
    result = await update_car("1", update_data)

    # Assert
    assert result is not None
    assert result.model == "Camry"
    assert result.price == 88000.0

@pytest.mark.asyncio
async def test_update_car_should_return_none_when_id_does_not_exist():
    # Arrange
    update_data = UpdateCarDto(brand="Toyota", model="Camry", year=2021, color=CarColor.BLACK, price=88000.0)

    # Act
    result = await update_car("999", update_data)

    # Assert
    assert result is None

@pytest.mark.asyncio
async def test_delete_car_should_return_true_when_car_deleted():
    # Act
    result = await delete_car("1")

    # Assert
    assert result is True
    assert len(await get_all_cars()) == 2

@pytest.mark.asyncio
async def test_delete_car_should_return_false_when_id_does_not_exist():
    # Act
    result = await delete_car("999")

    # Assert
    assert result is False
    assert len(await get_all_cars()) == 3