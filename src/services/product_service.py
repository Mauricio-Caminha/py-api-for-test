from typing import Optional
from src.models.schemas import Product, CreateProductDto, UpdateProductDto

# Simulação de banco de dados em memória
products: list[Product] = [
    Product(
        id="1",
        name="Notebook",
        description="Notebook Dell Inspiron",
        price=3500.0,
        stock=10,
        category="Electronics",
    ),
    Product(
        id="2",
        name="Mouse",
        description="Mouse Logitech Wireless",
        price=150.0,
        stock=50,
        category="Electronics",
    ),
    Product(
        id="3",
        name="Teclado",
        description="Teclado Mecânico RGB",
        price=450.0,
        stock=25,
        category="Electronics",
    ),
]


async def get_all_products() -> list[Product]:
    return products


async def get_product_by_id(product_id: str) -> Optional[Product]:
    return next((product for product in products if product.id == product_id), None)


async def create_product(product_data: CreateProductDto) -> Product:
    new_product = Product(
        id=str(len(products) + 1),
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        stock=product_data.stock,
        category=product_data.category,
    )
    products.append(new_product)
    return new_product


async def update_product(product_id: str, product_data: UpdateProductDto) -> Optional[Product]:
    product_index = next((i for i, product in enumerate(products) if product.id == product_id), None)
    
    if product_index is None:
        return None
    
    product_dict = products[product_index].model_dump()
    update_dict = product_data.model_dump(exclude_unset=True)
    updated_product = Product(**{**product_dict, **update_dict})
    products[product_index] = updated_product
    
    return updated_product


async def delete_product(product_id: str) -> bool:
    product_index = next((i for i, product in enumerate(products) if product.id == product_id), None)
    
    if product_index is None:
        return False
    
    products.pop(product_index)
    return True

