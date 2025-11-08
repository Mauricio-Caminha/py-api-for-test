import pytest
from unittest.mock import patch
from src.services.product_service import get_all_products, get_product_by_id, create_product, update_product, delete_product
from src.models.schemas import Product, CreateProductDto, UpdateProductDto

@pytest.mark.asyncio
async def test_get_all_products():
    """Should return all products"""
    result = await get_all_products()
    assert len(result) == 3
    assert result[0].name == "Notebook"

@pytest.mark.asyncio
async def test_get_product_by_id_when_exists():
    """Should return product when id exists"""
    result = await get_product_by_id("1")
    assert result is not None
    assert result.id == "1"

@pytest.mark.asyncio
async def test_get_product_by_id_when_not_exists():
    """Should return None when product id does not exist"""
    result = await get_product_by_id("999")
    assert result is None

@pytest.mark.asyncio
async def test_create_product():
    """Should create a new product"""
    product_data = CreateProductDto(
        name="Headphones",
        description="Wireless Headphones",
        price=300.0,
        stock=20,
        category="Electronics",
    )
    result = await create_product(product_data)
    assert result.id == "4"
    assert result.name == "Headphones"
    assert len(await get_all_products()) == 4

@pytest.mark.asyncio
async def test_update_product_when_exists():
    """Should update product when id exists"""
    update_data = UpdateProductDto(
        name="Updated Notebook",
        description="Updated Description",
        price=3600.0,
        stock=5,
        category="Electronics",
    )
    result = await update_product("1", update_data)
    assert result is not None
    assert result.name == "Updated Notebook"
    assert result.price == 3600.0

@pytest.mark.asyncio
async def test_update_product_when_not_exists():
    """Should return None when product id does not exist"""
    update_data = UpdateProductDto(
        name="Non-existent Product",
        description="This product does not exist",
        price=100.0,
        stock=10,
        category="Electronics",
    )
    result = await update_product("999", update_data)
    assert result is None

@pytest.mark.asyncio
async def test_delete_product_when_exists():
    """Should delete product when id exists"""
    result = await delete_product("1")
    assert result is True
    assert len(await get_all_products()) == 2

@pytest.mark.asyncio
async def test_delete_product_when_not_exists():
    """Should return False when product id does not exist"""
    result = await delete_product("999")
    assert result is False
    assert len(await get_all_products()) == 3