from fastapi import HTTPException, status
from src.models.schemas import Product, CreateProductDto, UpdateProductDto
from src.services import product_service


async def get_all_products() -> list[Product]:
    return await product_service.get_all_products()


async def get_product_by_id(product_id: str) -> Product:
    product = await product_service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product


async def create_product(product_data: CreateProductDto) -> Product:
    return await product_service.create_product(product_data)


async def update_product(product_id: str, product_data: UpdateProductDto) -> Product:
    updated_product = await product_service.update_product(product_id, product_data)
    if not updated_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return updated_product


async def delete_product(product_id: str) -> dict:
    deleted = await product_service.delete_product(product_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return {"message": "Product deleted successfully"}

