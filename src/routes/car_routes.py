from fastapi import APIRouter
from src.controllers import car_controller
from src.models.schemas import Car, CreateCarDto, UpdateCarDto

router = APIRouter(prefix="/api/cars", tags=["cars"])


@router.get("/", response_model=list[Car])
async def get_all_cars():
    return await car_controller.get_all_cars()


@router.get("/{car_id}", response_model=Car)
async def get_car_by_id(car_id: str):
    return await car_controller.get_car_by_id(car_id)


@router.post("/", response_model=Car, status_code=201)
async def create_car(car_data: CreateCarDto):
    return await car_controller.create_car(car_data)


@router.put("/{car_id}", response_model=Car)
async def update_car(car_id: str, car_data: UpdateCarDto):
    return await car_controller.update_car(car_id, car_data)


@router.delete("/{car_id}")
async def delete_car(car_id: str):
    return await car_controller.delete_car(car_id)

