import pytest
from unittest.mock import patch, AsyncMock
from fastapi import HTTPException
from src.controllers.product_controller import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product
)
from src.models.schemas import Product, CreateProductDto, UpdateProductDto

@pytest.mark.asyncio
class TestProductController:

    @patch('src.services.product_service.get_all_products', new_callable=AsyncMock)
    async def test_get_all_products(self, mock_get_all_products):
        """Should return a list of products"""
        mock_get_all_products.return_value = [Product(id="1", name="Product 1"), Product(id="2", name="Product 2")]
        
        result = await get_all_products()
        
        assert len(result) == 2
        assert result[0].name == "Product 1"

    @patch('src.services.product_service.get_product_by_id', new_callable=AsyncMock)
    async def test_get_product_by_id_when_exists(self, mock_get_product_by_id):
        """Should return product when id exists"""
        mock_product = Product(id="1", name="Product 1")
        mock_get_product_by_id.return_value = mock_product
        
        result = await get_product_by_id("1")
        
        assert result.id == "1"
        assert result.name == "Product 1"

    @patch('src.services.product_service.get_product_by_id', new_callable=AsyncMock)
    async def test_get_product_by_id_when_not_exists(self, mock_get_product_by_id):
        """Should raise HTTPException when product not found"""
        mock_get_product_by_id.return_value = None
        
        with pytest.raises(HTTPException) as exc_info:
            await get_product_by_id("999")
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Product not found"

    @patch('src.services.product_service.create_product', new_callable=AsyncMock)
    async def test_create_product(self, mock_create_product):
        """Should create a new product"""
        product_data = CreateProductDto(name="New Product")
        mock_product = Product(id="1", name="New Product")
        mock_create_product.return_value = mock_product
        
        result = await create_product(product_data)
        
        assert result.id == "1"
        assert result.name == "New Product"

    @patch('src.services.product_service.update_product', new_callable=AsyncMock)
    async def test_update_product_when_exists(self, mock_update_product):
        """Should update product when id exists"""
        product_data = UpdateProductDto(name="Updated Product")
        mock_product = Product(id="1", name="Updated Product")
        mock_update_product.return_value = mock_product
        
        result = await update_product("1", product_data)
        
        assert result.id == "1"
        assert result.name == "Updated Product"

    @patch('src.services.product_service.update_product', new_callable=AsyncMock)
    async def test_update_product_when_not_exists(self, mock_update_product):
        """Should raise HTTPException when product not found"""
        product_data = UpdateProductDto(name="Updated Product")
        mock_update_product.return_value = None
        
        with pytest.raises(HTTPException) as exc_info:
            await update_product("999", product_data)
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Product not found"

    @patch('src.services.product_service.delete_product', new_callable=AsyncMock)
    async def test_delete_product_when_exists(self, mock_delete_product):
        """Should delete product when id exists"""
        mock_delete_product.return_value = True
        
        result = await delete_product("1")
        
        assert result == {"message": "Product deleted successfully"}

    @patch('src.services.product_service.delete_product', new_callable=AsyncMock)
    async def test_delete_product_when_not_exists(self, mock_delete_product):
        """Should raise HTTPException when product not found"""
        mock_delete_product.return_value = False
        
        with pytest.raises(HTTPException) as exc_info:
            await delete_product("999")
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Product not found"