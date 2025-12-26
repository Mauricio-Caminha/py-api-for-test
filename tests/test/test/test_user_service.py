import pytest
from unittest.mock import patch, MagicMock
from src.models.schemas import User, CreateUserDto, UpdateUserDto
from src.services.user_service import get_all_users, get_user_by_id, create_user, update_user, delete_user

@pytest.mark.asyncio
class TestUserService:
    @pytest.fixture
    def user_data(self):
        return CreateUserDto(name="New User", email="newuser@example.com", age=28)

    @pytest.fixture
    def update_data(self):
        return UpdateUserDto(name="Updated User")

    async def test_get_all_users_should_return_all_users(self):
        # Act
        result = await get_all_users()

        # Assert
        assert len(result) == 3
        assert result[0].name == "João Silva"

    async def test_get_user_by_id_should_return_user_when_id_exists(self):
        # Act
        result = await get_user_by_id("1")

        # Assert
        assert result is not None
        assert result.name == "João Silva"

    async def test_get_user_by_id_should_return_none_when_id_does_not_exist(self):
        # Act
        result = await get_user_by_id("999")

        # Assert
        assert result is None

    async def test_create_user_should_add_user_and_return_it(self, user_data):
        # Act
        result = await create_user(user_data)

        # Assert
        assert result.name == user_data.name
        assert len(await get_all_users()) == 4

    async def test_update_user_should_return_updated_user_when_id_exists(self, update_data):
        # Act
        result = await update_user("1", update_data)

        # Assert
        assert result is not None
        assert result.name == update_data.name

    async def test_update_user_should_return_none_when_id_does_not_exist(self, update_data):
        # Act
        result = await update_user("999", update_data)

        # Assert
        assert result is None

    async def test_delete_user_should_return_true_when_user_deleted(self):
        # Act
        result = await delete_user("1")

        # Assert
        assert result is True
        assert len(await get_all_users()) == 2

    async def test_delete_user_should_return_false_when_user_does_not_exist(self):
        # Act
        result = await delete_user("999")

        # Assert
        assert result is False