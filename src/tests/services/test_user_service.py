import pytest
from unittest.mock import patch
from src.services.user_service import get_all_users, get_user_by_id, create_user, update_user, delete_user
from src.models.schemas import User, CreateUserDto, UpdateUserDto

@pytest.mark.asyncio
async def test_get_all_users():
    """Should return all users"""
    result = await get_all_users()
    assert len(result) == 3
    assert result[0].name == "João Silva"

@pytest.mark.asyncio
async def test_get_user_by_id_when_exists():
    """Should return user when id exists"""
    result = await get_user_by_id("1")
    assert result is not None
    assert result.id == "1"
    assert result.name == "João Silva"

@pytest.mark.asyncio
async def test_get_user_by_id_when_not_exists():
    """Should return None when user id does not exist"""
    result = await get_user_by_id("999")
    assert result is None

@pytest.mark.asyncio
async def test_create_user():
    """Should create a new user"""
    user_data = CreateUserDto(name="Ana", email="ana@example.com", age=28)
    result = await create_user(user_data)
    assert result.id == "4"
    assert result.name == "Ana"
    assert len(await get_all_users()) == 4

@pytest.mark.asyncio
async def test_update_user_when_exists():
    """Should update user when id exists"""
    user_data = UpdateUserDto(name="João Updated", email="joao.updated@example.com", age=31)
    result = await update_user("1", user_data)
    assert result is not None
    assert result.name == "João Updated"
    assert result.age == 31

@pytest.mark.asyncio
async def test_update_user_when_not_exists():
    """Should return None when user id does not exist"""
    user_data = UpdateUserDto(name="Nonexistent User", email="nonexistent@example.com", age=40)
    result = await update_user("999", user_data)
    assert result is None

@pytest.mark.asyncio
async def test_delete_user_when_exists():
    """Should delete user when id exists"""
    result = await delete_user("1")
    assert result is True

@pytest.mark.asyncio
async def test_delete_user_when_not_exists():
    """Should return False when user id does not exist"""
    result = await delete_user("999")
    assert result is False