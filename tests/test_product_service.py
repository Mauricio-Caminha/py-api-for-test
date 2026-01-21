import pytest
from unittest.mock import patch, Mock
from src.services.product_service import get_all_products, get_product_by_id, create_product, update_product, delete_product
from src.models.schemas import Product, CreateProductDto, UpdateProductDto
from src.types.enums import ProductCategory

@pytest.mark.asyncio
class TestProductService:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.products = [
            Product(
                id="1",
                name="Notebook",
                description="Notebook Dell Inspiron",
                price=3500.0,
                stock=10,
                category=ProductCategory.ELECTRONICS,
            ),
            Product(
                id="2",
                name="Mouse",
                description="Mouse Logitech Wireless",
                price=150.0,
                stock=50,
                category=ProductCategory.ELECTRONICS,
            ),
            Product(
                id="3",
                name="Teclado",
                description="Teclado Mecânico RGB",
                price=450.0,
                stock=25,
                category=ProductCategory.ELECTRONICS,
            ),
        ]

    async def test_get_all_products_should_return_all_products(self):
        # Act
        result = await get_all_products()

        # Assert
        assert result == self.products

    async def test_get_product_by_id_should_return_product_when_id_exists(self):
        # Act
        result = await get_product_by_id("1")

        # Assert
        assert result == self.products[0]

    async def test_get_product_by_id_should_return_none_when_id_does_not_exist(self):
        # Act
        result = await get_product_by_id("999")

        # Assert
        assert result is None

    async def test_create_product_should_add_new_product(self):
        # Arrange
        new_product_data = CreateProductDto(
            name="Headphones",
            description="Headphones Bluetooth",
            price=300.0,
            stock=20,
            category=ProductCategory.ELECTRONICS,
        )

        # Act
        result = await create_product(new_product_data)

        # Assert
        assert result.name == new_product_data.name
        assert len(await get_all_products()) == 4  # Ensure product count increased

    async def test_update_product_should_return_updated_product_when_id_exists(self):
        # Arrange
        update_data = UpdateProductDto(
            name="Updated Notebook",
            price=3200.0,
        )

        # Act
        result = await update_product("1", update_data)

        # Assert
        assert result.name == "Updated Notebook"
        assert result.price == 3200.0

    async def test_update_product_should_return_none_when_id_does_not_exist(self):
        # Arrange
        update_data = UpdateProductDto(
            name="Non-existent Product",
            price=100.0,
        )

        # Act
        result = await update_product("999", update_data)

        # Assert
        assert result is None

    async def test_delete_product_should_return_true_when_product_deleted(self):
        # Act
        result = await delete_product("1")

        # Assert
        assert result is True
        assert len(await get_all_products()) == 2  # Ensure product count decreased

    async def test_delete_product_should_return_false_when_id_does_not_exist(self):
        # Act
        result = await delete_product("999")

        # Assert
        assert result is False