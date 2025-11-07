from fastapi import HTTPException, status
from src.models.schemas import User, CreateUserDto, UpdateUserDto
from src.services import user_service


async def get_all_users() -> list[User]:
    return await user_service.get_all_users()


async def get_user_by_id(user_id: str) -> User:
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


async def create_user(user_data: CreateUserDto) -> User:
    return await user_service.create_user(user_data)


async def update_user(user_id: str, user_data: UpdateUserDto) -> User:
    updated_user = await user_service.update_user(user_id, user_data)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return updated_user


async def delete_user(user_id: str) -> dict:
    deleted = await user_service.delete_user(user_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {"message": "User deleted successfully"}

