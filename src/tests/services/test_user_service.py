import pytest
import pytest_asyncio
from unittest.mock import patch
from src.services.user_service import get_all_users, get_user_by_id, create_user, update_user, delete_user
from src.models.schemas import User, CreateUserDto, UpdateUserDto

@pytest.mark.asyncio
class TestUserService:
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.users_backup = [
            User(id="1", name="João Silva", email="joao@example.com", age=30),
            User(id="2", name="Maria Santos", email="maria@example.com", age=25),
            User(id="3", name="Pedro Oliveira", email="pedro@example.com", age=35),
        ]
        global users
        users.clear()
        users.extend(self.users_backup)

    async def test_get_all_users(self):
        result = await get_all_users()
        assert len(result) == 3
        assert result == self.users_backup

    async def test_get_user_by_id_when_exists(self):
        result = await get_user_by_id("1")
        assert result.id == "1"
        assert result.name == "João Silva"

    async def test_get_user_by_id_when_not_found(self):
        result = await get_user_by_id("999")
        assert result is None

    async def test_create_user(self):
        user_data = CreateUserDto(name="Ana", email="ana@example.com", age=28)
        result = await create_user(user_data)
        assert result.id == "4"
        assert result.name == "Ana"
        assert len(users) == 4

    async def test_update_user_when_exists(self):
        update_data = UpdateUserDto(name="João Updated", email="joao_updated@example.com")
        result = await update_user("1", update_data)
        assert result.name == "João Updated"
        assert result.email == "joao_updated@example.com"

    async def test_update_user_when_not_found(self):
        update_data = UpdateUserDto(name="Nonexistent User")
        result = await update_user("999", update_data)
        assert result is None

    async def test_delete_user_when_exists(self):
        result = await delete_user("1")
        assert result is True
        assert len(users) == 2

    async def test_delete_user_when_not_found(self):
        result = await delete_user("999")
        assert result is False
        assert len(users) == 3