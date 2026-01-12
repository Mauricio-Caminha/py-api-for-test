from typing import Optional
from datetime import datetime
from src.models.schemas import Order, CreateOrderDto, UpdateOrderDto, OrderItem
from src.types.enums import OrderStatus

# Simulação de banco de dados em memória
orders: list[Order] = [
    Order(
        id="1",
        userId="1",
        items=[OrderItem(productId="1", quantity=2, price=3500.0)],
        total=7000.0,
        status=OrderStatus.PENDING,
        createdAt="2025-11-07T18:18:08.792Z",
    ),
    Order(
        id="2",
        userId="2",
        items=[OrderItem(productId="2", quantity=1, price=150.0)],
        total=150.0,
        status=OrderStatus.COMPLETED,
        createdAt="2025-11-07T18:18:08.792Z",
    ),
    Order(
        id="3",
        userId="1",
        items=[OrderItem(productId="3", quantity=1, price=450.0)],
        total=450.0,
        status=OrderStatus.PROCESSING,
        createdAt="2025-11-07T18:18:08.792Z",
    ),
]


async def get_all_orders() -> list[Order]:
    return orders


async def get_order_by_id(order_id: str) -> Optional[Order]:
    return next((order for order in orders if order.id == order_id), None)


async def create_order(order_data: CreateOrderDto) -> Order:
    total = order_data.total if order_data.total is not None else 0.0
    status = order_data.status if order_data.status is not None else OrderStatus.PENDING
    
    new_order = Order(
        id=str(len(orders) + 1),
        userId=order_data.userId,
        items=order_data.items,
        total=total,
        status=status,
        createdAt=datetime.now().isoformat(),
    )
    orders.append(new_order)
    return new_order


async def update_order(order_id: str, order_data: UpdateOrderDto) -> Optional[Order]:
    order_index = next((i for i, order in enumerate(orders) if order.id == order_id), None)
    
    if order_index is None:
        return None
    
    order_dict = orders[order_index].model_dump()
    update_dict = order_data.model_dump(exclude_unset=True)
    # Preserva o ID e createdAt
    updated_order = Order(
        **{**order_dict, **update_dict, "id": orders[order_index].id, "createdAt": orders[order_index].createdAt}
    )
    orders[order_index] = updated_order
    
    return updated_order


async def delete_order(order_id: str) -> bool:
    order_index = next((i for i, order in enumerate(orders) if order.id == order_id), None)
    
    if order_index is None:
        return False
    
    orders.pop(order_index)
    return True

