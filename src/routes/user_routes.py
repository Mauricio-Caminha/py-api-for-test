from fastapi import APIRouter
from src.controllers import user_controller
from src.models.schemas import User, CreateUserDto, UpdateUserDto

router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/", response_model=list[User])
async def get_all_users():
    return await user_controller.get_all_users()


@router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: str):
    return await user_controller.get_user_by_id(user_id)


@router.post("/", response_model=User, status_code=201)
async def create_user(user_data: CreateUserDto):
    return await user_controller.create_user(user_data)


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: str, user_data: UpdateUserDto):
    return await user_controller.update_user(user_id, user_data)


@router.delete("/{user_id}")
async def delete_user(user_id: str):
    return await user_controller.delete_user(user_id)

