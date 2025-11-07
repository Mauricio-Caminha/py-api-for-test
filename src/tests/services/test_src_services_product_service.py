import pytest
import pytest_asyncio
from src.services.product_service import get_all_products, get_product_by_id, create_product, update_product, delete_product
from src.models.schemas import Product, CreateProductDto, UpdateProductDto

@pytest_asyncio.fixture
async def setup_products():
    # Clear the products list before each test
    global products
    products.clear()
    products.extend([
        Product(id="1", name="Notebook", description="Notebook Dell Inspiron", price=3500.0, stock=10, category="Electronics"),
        Product(id="2", name="Mouse", description="Mouse Logitech Wireless", price=150.0, stock=50, category="Electronics"),
        Product(id="3", name="Teclado", description="Teclado Mecânico RGB", price=450.0, stock=25, category="Electronics"),
    ])
    yield
    products.clear()

@pytest.mark.asyncio
async def test_get_all_products(setup_products):
    result = await get_all_products()
    assert len(result) == 3

@pytest.mark.asyncio
async def test_get_product_by_id_existing(setup_products):
    result = await get_product_by_id("1")
    assert result.id == "1"
    assert result.name == "Notebook"

@pytest.mark.asyncio
async def test_get_product_by_id_non_existing(setup_products):
    result = await get_product_by_id("999")
    assert result is None

@pytest.mark.asyncio
async def test_create_product(setup_products):
    new_product_data = CreateProductDto(name="Monitor", description="Monitor 24 inch", price=800.0, stock=15, category="Electronics")
    result = await create_product(new_product_data)
    assert result.id == "4"
    assert result.name == "Monitor"
    assert len(products) == 4

@pytest.mark.asyncio
async def test_update_product_existing(setup_products):
    update_data = UpdateProductDto(price=3000.0, stock=5)
    result = await update_product("1", update_data)
    assert result.id == "1"
    assert result.price == 3000.0
    assert result.stock == 5

@pytest.mark.asyncio
async def test_update_product_non_existing(setup_products):
    update_data = UpdateProductDto(price=3000.0, stock=5)
    result = await update_product("999", update_data)
    assert result is None

@pytest.mark.asyncio
async def test_delete_product_existing(setup_products):
    result = await delete_product("1")
    assert result is True
    assert len(products) == 2

@pytest.mark.asyncio
async def test_delete_product_non_existing(setup_products):
    result = await delete_product("999")
    assert result is False
    assert len(products) == 3