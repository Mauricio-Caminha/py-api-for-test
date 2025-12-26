import pytest
from unittest.mock import patch, MagicMock
from src.models.schemas import Product, CreateProductDto, UpdateProductDto
from src.services.product_service import get_all_products, get_product_by_id, create_product, update_product, delete_product

@pytest.mark.asyncio
async def test_get_all_products():
    # Arrange
    expected_products = [
        Product(id="1", name="Notebook", description="Notebook Dell Inspiron", price=3500.0, stock=10, category="Electronics"),
        Product(id="2", name="Mouse", description="Mouse Logitech Wireless", price=150.0, stock=50, category="Electronics"),
        Product(id="3", name="Teclado", description="Teclado Mecânico RGB", price=450.0, stock=25, category="Electronics"),
    ]

    # Act
    result = await get_all_products()

    # Assert
    assert result == expected_products

@pytest.mark.asyncio
async def test_get_product_by_id_should_return_product_when_id_exists():
    # Act
    result = await get_product_by_id("1")

    # Assert
    assert result == Product(id="1", name="Notebook", description="Notebook Dell Inspiron", price=3500.0, stock=10, category="Electronics")

@pytest.mark.asyncio
async def test_get_product_by_id_should_return_none_when_id_does_not_exist():
    # Act
    result = await get_product_by_id("999")

    # Assert
    assert result is None

@pytest.mark.asyncio
async def test_create_product():
    # Arrange
    product_data = CreateProductDto(name="Headphones", description="Wireless Headphones", price=300.0, stock=20, category="Electronics")

    # Act
    result = await create_product(product_data)

    # Assert
    assert result.name == "Headphones"
    assert result.description == "Wireless Headphones"
    assert result.price == 300.0
    assert result.stock == 20
    assert result.category == "Electronics"
    assert len(products) == 4  # Ensure the product list has increased

@pytest.mark.asyncio
async def test_update_product_should_return_updated_product_when_id_exists():
    # Arrange
    update_data = UpdateProductDto(name="Updated Notebook", price=3200.0)

    # Act
    result = await update_product("1", update_data)

    # Assert
    assert result.name == "Updated Notebook"
    assert result.price == 3200.0

@pytest.mark.asyncio
async def test_update_product_should_return_none_when_id_does_not_exist():
    # Arrange
    update_data = UpdateProductDto(name="Non-existent Product", price=1000.0)

    # Act
    result = await update_product("999", update_data)

    # Assert
    assert result is None

@pytest.mark.asyncio
async def test_delete_product_should_return_true_when_id_exists():
    # Act
    result = await delete_product("1")

    # Assert
    assert result is True
    assert len(products) == 2  # Ensure the product list has decreased

@pytest.mark.asyncio
async def test_delete_product_should_return_false_when_id_does_not_exist():
    # Act
    result = await delete_product("999")

    # Assert
    assert result is False