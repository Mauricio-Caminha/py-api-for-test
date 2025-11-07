from fastapi import HTTPException, status
from src.models.schemas import Car, CreateCarDto, UpdateCarDto
from src.services import car_service


async def get_all_cars() -> list[Car]:
    return await car_service.get_all_cars()


async def get_car_by_id(car_id: str) -> Car:
    car = await car_service.get_car_by_id(car_id)
    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Car not found"
        )
    return car


async def create_car(car_data: CreateCarDto) -> Car:
    return await car_service.create_car(car_data)


async def update_car(car_id: str, car_data: UpdateCarDto) -> Car:
    updated_car = await car_service.update_car(car_id, car_data)
    if not updated_car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Car not found"
        )
    return updated_car


async def delete_car(car_id: str) -> dict:
    deleted = await car_service.delete_car(car_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Car not found"
        )
    return {"message": "Car deleted successfully"}

