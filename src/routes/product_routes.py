from fastapi import APIRouter
from src.controllers import product_controller
from src.models.schemas import Product, CreateProductDto, UpdateProductDto

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("/", response_model=list[Product])
async def get_all_products():
    return await product_controller.get_all_products()


@router.get("/{product_id}", response_model=Product)
async def get_product_by_id(product_id: str):
    return await product_controller.get_product_by_id(product_id)


@router.post("/", response_model=Product, status_code=201)
async def create_product(product_data: CreateProductDto):
    return await product_controller.create_product(product_data)


@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: str, product_data: UpdateProductDto):
    return await product_controller.update_product(product_id, product_data)


@router.delete("/{product_id}")
async def delete_product(product_id: str):
    return await product_controller.delete_product(product_id)

