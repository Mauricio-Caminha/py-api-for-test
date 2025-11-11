import pytest
from src.models.schemas import Product, CreateProductDto, UpdateProductDto
from src.services.product_service import get_all_products, get_product_by_id, create_product, update_product, delete_product

@pytest.mark.asyncio
class TestProductService:
    async def test_get_all_products(self):
        # Act
        result = await get_all_products()

        # Assert
        assert len(result) == 3

    async def test_get_product_by_id_should_return_product_when_id_exists(self):
        # Act
        result = await get_product_by_id("1")

        # Assert
        assert result is not None
        assert result.id == "1"
        assert result.name == "Notebook"

    async def test_get_product_by_id_should_return_none_when_id_does_not_exist(self):
        # Act
        result = await get_product_by_id("999")

        # Assert
        assert result is None

    async def test_create_product_should_add_new_product(self):
        # Arrange
        new_product_data = CreateProductDto(
            name="Headphones",
            description="Wireless Headphones",
            price=300.0,
            stock=20,
            category="Electronics"
        )

        # Act
        result = await create_product(new_product_data)

        # Assert
        assert result.id == "4"  # Assuming this is the next ID
        assert result.name == "Headphones"
        assert len(await get_all_products()) == 4

    async def test_update_product_should_modify_existing_product(self):
        # Arrange
        update_data = UpdateProductDto(
            name="Updated Notebook",
            price=3600.0
        )

        # Act
        result = await update_product("1", update_data)

        # Assert
        assert result is not None
        assert result.name == "Updated Notebook"
        assert result.price == 3600.0

    async def test_update_product_should_return_none_when_product_not_found(self):
        # Arrange
        update_data = UpdateProductDto(name="Non-existent Product")

        # Act
        result = await update_product("999", update_data)

        # Assert
        assert result is None

    async def test_delete_product_should_return_true_when_product_deleted(self):
        # Act
        result = await delete_product("1")

        # Assert
        assert result is True
        assert len(await get_all_products()) == 2  # One less product

    async def test_delete_product_should_return_false_when_product_not_found(self):
        # Act
        result = await delete_product("999")

        # Assert
        assert result is False
        assert len(await get_all_products()) == 3  # No change in product count