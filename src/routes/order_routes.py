from fastapi import APIRouter
from src.controllers import order_controller
from src.models.schemas import Order, CreateOrderDto, UpdateOrderDto

router = APIRouter(prefix="/api/orders", tags=["orders"])


@router.get("/", response_model=list[Order])
async def get_all_orders():
    return await order_controller.get_all_orders()


@router.get("/{order_id}", response_model=Order)
async def get_order_by_id(order_id: str):
    return await order_controller.get_order_by_id(order_id)


@router.post("/", response_model=Order, status_code=201)
async def create_order(order_data: CreateOrderDto):
    return await order_controller.create_order(order_data)


@router.put("/{order_id}", response_model=Order)
async def update_order(order_id: str, order_data: UpdateOrderDto):
    return await order_controller.update_order(order_id, order_data)


@router.delete("/{order_id}")
async def delete_order(order_id: str):
    return await order_controller.delete_order(order_id)

