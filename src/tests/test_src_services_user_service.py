import pytest
import pytest_asyncio
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
    assert result.name == "João Silva"

@pytest.mark.asyncio
async def test_get_user_by_id_when_not_found():
    """Should return None when user not found"""
    result = await get_user_by_id("999")
    assert result is None

@pytest.mark.asyncio
async def test_create_user_with_valid_data():
    """Should create and return new user"""
    user_data = CreateUserDto(name="Ana", email="ana@example.com", age=28)
    result = await create_user(user_data)
    assert result.id == "4"
    assert result.name == "Ana"

@pytest.mark.asyncio
async def test_update_user_when_exists():
    """Should update and return user when id exists"""
    user_data = UpdateUserDto(name="João Updated", email="joao_updated@example.com")
    result = await update_user("1", user_data)
    assert result is not None
    assert result.name == "João Updated"

@pytest.mark.asyncio
async def test_update_user_when_not_found():
    """Should return None when user not found"""
    user_data = UpdateUserDto(name="Nonexistent User")
    result = await update_user("999", user_data)
    assert result is None

@pytest.mark.asyncio
async def test_delete_user_when_exists():
    """Should return True when user deleted"""
    result = await delete_user("1")
    assert result is True
    assert await get_user_by_id("1") is None

@pytest.mark.asyncio
async def test_delete_user_when_not_found():
    """Should return False when user not found"""
    result = await delete_user("999")
    assert result is False