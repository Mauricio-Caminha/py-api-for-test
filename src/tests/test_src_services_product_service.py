import pytest
import pytest_asyncio
from unittest.mock import patch
from src.services.product_service import get_all_products, get_product_by_id, create_product, update_product, delete_product
from src.models.schemas import Product, CreateProductDto, UpdateProductDto

@pytest.mark.asyncio
class TestProductService:
    
    @pytest_asyncio.fixture(autouse=True)
    async def setup_method(self):
        self.products = [
            Product(id="1", name="Notebook", description="Notebook Dell Inspiron", price=3500.0, stock=10, category="Electronics"),
            Product(id="2", name="Mouse", description="Mouse Logitech Wireless", price=150.0, stock=50, category="Electronics"),
            Product(id="3", name="Teclado", description="Teclado Mecânico RGB", price=450.0, stock=25, category="Electronics"),
        ]
    
    async def test_get_all_products(self):
        result = await get_all_products()
        assert len(result) == 3
        assert result[0].name == "Notebook"
    
    async def test_get_product_by_id_when_exists(self):
        result = await get_product_by_id("1")
        assert result is not None
        assert result.name == "Notebook"
    
    async def test_get_product_by_id_when_not_exists(self):
        result = await get_product_by_id("999")
        assert result is None
    
    async def test_create_product(self):
        new_product_data = CreateProductDto(name="Monitor", description="Monitor 24 inches", price=800.0, stock=20, category="Electronics")
        result = await create_product(new_product_data)
        assert result.id == "4"
        assert result.name == "Monitor"
        assert len(await get_all_products()) == 4
    
    async def test_update_product_when_exists(self):
        update_data = UpdateProductDto(name="Updated Notebook", price=3600.0)
        result = await update_product("1", update_data)
        assert result is not None
        assert result.name == "Updated Notebook"
        assert result.price == 3600.0
    
    async def test_update_product_when_not_exists(self):
        update_data = UpdateProductDto(name="Updated Product")
        result = await update_product("999", update_data)
        assert result is None
    
    async def test_delete_product_when_exists(self):
        result = await delete_product("1")
        assert result is True
        assert len(await get_all_products()) == 2
    
    async def test_delete_product_when_not_exists(self):
        result = await delete_product("999")
        assert result is False