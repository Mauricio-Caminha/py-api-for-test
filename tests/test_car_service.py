import pytest
from unittest.mock import patch, MagicMock
from src.models.schemas import Car, CreateCarDto, UpdateCarDto
from src.services.car_service import get_all_cars, get_car_by_id, create_car, update_car, delete_car

class TestCarService:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.car_data = CreateCarDto(brand="Tesla", model="Model S", year=2022, color="Blue", price=100000.0)
        self.update_data = UpdateCarDto(brand="Tesla", model="Model X", year=2023, color="Red", price=120000.0)

    @pytest.mark.asyncio
    async def test_get_all_cars_should_return_all_cars(self):
        # Act
        result = await get_all_cars()

        # Assert
        assert len(result) == 3

    @pytest.mark.asyncio
    async def test_get_car_by_id_should_return_car_when_id_exists(self):
        # Act
        result = await get_car_by_id("1")

        # Assert
        assert result.id == "1"
        assert result.brand == "Toyota"

    @pytest.mark.asyncio
    async def test_get_car_by_id_should_return_none_when_id_does_not_exist(self):
        # Act
        result = await get_car_by_id("999")

        # Assert
        assert result is None

    @pytest.mark.asyncio
    async def test_create_car_should_add_new_car(self):
        # Act
        result = await create_car(self.car_data)

        # Assert
        assert result.id == "4"
        assert result.brand == "Tesla"
        assert len(await get_all_cars()) == 4

    @pytest.mark.asyncio
    async def test_update_car_should_return_updated_car_when_id_exists(self):
        # Act
        result = await update_car("1", self.update_data)

        # Assert
        assert result.id == "1"
        assert result.model == "Model X"
        assert result.year == 2023

    @pytest.mark.asyncio
    async def test_update_car_should_return_none_when_id_does_not_exist(self):
        # Act
        result = await update_car("999", self.update_data)

        # Assert
        assert result is None

    @pytest.mark.asyncio
    async def test_delete_car_should_return_true_when_car_deleted(self):
        # Act
        result = await delete_car("1")

        # Assert
        assert result is True
        assert len(await get_all_cars()) == 2

    @pytest.mark.asyncio
    async def test_delete_car_should_return_false_when_id_does_not_exist(self):
        # Act
        result = await delete_car("999")

        # Assert
        assert result is False
        assert len(await get_all_cars()) == 3