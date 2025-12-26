import pytest
from unittest.mock import patch, Mock
from src.models.schemas import Car, CreateCarDto, UpdateCarDto
from src.services.car_service import get_all_cars, get_car_by_id, create_car, update_car, delete_car

class TestCarService:
    @pytest.fixture
    def setup_cars(self):
        # Reset the in-memory database for each test
        from src.services.car_service import cars
        cars.clear()
        cars.extend([
            Car(id="1", brand="Toyota", model="Corolla", year=2020, color="White", price=85000.0),
            Car(id="2", brand="Honda", model="Civic", year=2021, color="Black", price=92000.0),
            Car(id="3", brand="Ford", model="Focus", year=2019, color="Red", price=75000.0),
        ])

    @pytest.mark.asyncio
    async def test_get_all_cars_should_return_all_cars(self, setup_cars):
        # Act
        result = await get_all_cars()

        # Assert
        assert len(result) == 3
        assert result[0].brand == "Toyota"

    @pytest.mark.asyncio
    async def test_get_car_by_id_should_return_car_when_id_exists(self, setup_cars):
        # Act
        result = await get_car_by_id("1")

        # Assert
        assert result is not None
        assert result.brand == "Toyota"

    @pytest.mark.asyncio
    async def test_get_car_by_id_should_return_none_when_id_does_not_exist(self, setup_cars):
        # Act
        result = await get_car_by_id("999")

        # Assert
        assert result is None

    @pytest.mark.asyncio
    async def test_create_car_should_add_new_car(self, setup_cars):
        # Arrange
        car_data = CreateCarDto(brand="Nissan", model="Altima", year=2022, color="Blue", price=88000.0)

        # Act
        result = await create_car(car_data)

        # Assert
        assert result.id == "4"
        assert len(await get_all_cars()) == 4

    @pytest.mark.asyncio
    async def test_update_car_should_modify_existing_car(self, setup_cars):
        # Arrange
        update_data = UpdateCarDto(brand="Toyota", model="Camry", year=2021, color="White", price=90000.0)

        # Act
        result = await update_car("1", update_data)

        # Assert
        assert result is not None
        assert result.model == "Camry"
        assert result.year == 2021

    @pytest.mark.asyncio
    async def test_update_car_should_return_none_when_id_does_not_exist(self, setup_cars):
        # Arrange
        update_data = UpdateCarDto(brand="Toyota", model="Camry", year=2021, color="White", price=90000.0)

        # Act
        result = await update_car("999", update_data)

        # Assert
        assert result is None

    @pytest.mark.asyncio
    async def test_delete_car_should_return_true_when_car_deleted(self, setup_cars):
        # Act
        result = await delete_car("1")

        # Assert
        assert result is True
        assert len(await get_all_cars()) == 2

    @pytest.mark.asyncio
    async def test_delete_car_should_return_false_when_id_does_not_exist(self, setup_cars):
        # Act
        result = await delete_car("999")

        # Assert
        assert result is False
        assert len(await get_all_cars()) == 3