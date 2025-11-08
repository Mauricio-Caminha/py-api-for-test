import pytest
import pytest_asyncio
from unittest.mock import patch
from src.services.product_service import get_all_products, get_product_by_id, create_product, update_product, delete_product
from src.models.schemas import Product, CreateProductDto, UpdateProductDto

@pytest.mark.asyncio
class TestProductService:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.initial_products = [
            Product(id="1", name="Notebook", description="Notebook Dell Inspiron", price=3500.0, stock=10, category="Electronics"),
            Product(id="2", name="Mouse", description="Mouse Logitech Wireless", price=150.0, stock=50, category="Electronics"),
            Product(id="3", name="Teclado", description="Teclado Mecânico RGB", price=450.0, stock=25, category="Electronics"),
        ]
        # Reset products to initial state before each test
        global products
        products.clear()
        products.extend(self.initial_products)

    async def test_get_all_products(self):
        """Should return all products"""
        result = await get_all_products()
        assert len(result) == 3
        assert result == self.initial_products

    async def test_get_product_by_id_when_exists(self):
        """Should return product when id exists"""
        result = await get_product_by_id("1")
        assert result.id == "1"
        assert result.name == "Notebook"

    async def test_get_product_by_id_when_not_found(self):
        """Should return None when product not found"""
        result = await get_product_by_id("999")
        assert result is None

    async def test_create_product(self):
        """Should create and return new product"""
        product_data = CreateProductDto(name="Monitor", description="Monitor 24 inch", price=1200.0, stock=15, category="Electronics")
        result = await create_product(product_data)
        assert result.id == "4"  # New product ID
        assert result.name == "Monitor"
        assert len(products) == 4  # Total products should increase

    async def test_update_product_when_exists(self):
        """Should update and return the product when id exists"""
        update_data = UpdateProductDto(name="Updated Notebook", price=3000.0)
        result = await update_product("1", update_data)
        assert result.name == "Updated Notebook"
        assert result.price == 3000.0

    async def test_update_product_when_not_found(self):
        """Should return None when product not found"""
        update_data = UpdateProductDto(name="Updated Product")
        result = await update_product("999", update_data)
        assert result is None

    async def test_delete_product_when_exists(self):
        """Should return True when product deleted"""
        result = await delete_product("1")
        assert result is True
        assert len(products) == 2  # Total products should decrease

    async def test_delete_product_when_not_found(self):
        """Should return False when product not found"""
        result = await delete_product("999")
        assert result is False
        assert len(products) == 3  # Total products should remain the same