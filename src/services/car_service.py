from typing import Optional
from src.models.schemas import Car, CreateCarDto, UpdateCarDto
from src.types.enums import CarColor

# Simulação de banco de dados em memória
cars: list[Car] = [
    Car(id="1", brand="Toyota", model="Corolla", year=2020, color=CarColor.WHITE, price=85000.0),
    Car(id="2", brand="Honda", model="Civic", year=2021, color=CarColor.BLACK, price=92000.0),
    Car(id="3", brand="Ford", model="Focus", year=2019, color=CarColor.RED, price=75000.0),
]


async def get_all_cars() -> list[Car]:
    return cars


async def get_car_by_id(car_id: str) -> Optional[Car]:
    return next((car for car in cars if car.id == car_id), None)


async def create_car(car_data: CreateCarDto) -> Car:
    new_car = Car(
        id=str(len(cars) + 1),
        brand=car_data.brand,
        model=car_data.model,
        year=car_data.year,
        color=car_data.color,
        price=car_data.price,
    )
    cars.append(new_car)
    return new_car


async def update_car(car_id: str, car_data: UpdateCarDto) -> Optional[Car]:
    car_index = next((i for i, car in enumerate(cars) if car.id == car_id), None)
    
    if car_index is None:
        return None
    
    car_dict = cars[car_index].model_dump()
    update_dict = car_data.model_dump(exclude_unset=True)
    updated_car = Car(**{**car_dict, **update_dict})
    cars[car_index] = updated_car
    
    return updated_car


async def delete_car(car_id: str) -> bool:
    car_index = next((i for i, car in enumerate(cars) if car.id == car_id), None)
    
    if car_index is None:
        return False
    
    cars.pop(car_index)
    return True

