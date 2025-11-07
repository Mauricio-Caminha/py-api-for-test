from fastapi import HTTPException, status
from src.models.schemas import Order, CreateOrderDto, UpdateOrderDto
from src.services import order_service


async def get_all_orders() -> list[Order]:
    return await order_service.get_all_orders()


async def get_order_by_id(order_id: str) -> Order:
    order = await order_service.get_order_by_id(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order


async def create_order(order_data: CreateOrderDto) -> Order:
    return await order_service.create_order(order_data)


async def update_order(order_id: str, order_data: UpdateOrderDto) -> Order:
    updated_order = await order_service.update_order(order_id, order_data)
    if not updated_order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return updated_order


async def delete_order(order_id: str) -> dict:
    deleted = await order_service.delete_order(order_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return {"message": "Order deleted successfully"}

