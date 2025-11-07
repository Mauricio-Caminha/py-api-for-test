import pytest
import pytest_asyncio
from src.services.user_service import get_all_users, get_user_by_id, create_user, update_user, delete_user
from src.models.schemas import User, CreateUserDto, UpdateUserDto

@pytest_asyncio.fixture
async def setup_users():
    # Clear the user list before each test
    global users
    users = []
    users.append(User(id="1", name="João Silva", email="joao@example.com", age=30))
    users.append(User(id="2", name="Maria Santos", email="maria@example.com", age=25))
    users.append(User(id="3", name="Pedro Oliveira", email="pedro@example.com", age=35))

@pytest.mark.asyncio
async def test_get_all_users(setup_users):
    result = await get_all_users()
    assert len(result) == 3

@pytest.mark.asyncio
async def test_get_user_by_id_existing_user(setup_users):
    result = await get_user_by_id("1")
    assert result.id == "1"
    assert result.name == "João Silva"

@pytest.mark.asyncio
async def test_get_user_by_id_non_existing_user(setup_users):
    result = await get_user_by_id("999")
    assert result is None

@pytest.mark.asyncio
async def test_create_user(setup_users):
    new_user_data = CreateUserDto(name="Ana Costa", email="ana@example.com", age=28)
    result = await create_user(new_user_data)
    assert result.id == "4"
    assert result.name == "Ana Costa"
    assert len(users) == 4

@pytest.mark.asyncio
async def test_update_user_existing_user(setup_users):
    update_data = UpdateUserDto(name="João Updated", email="joao.updated@example.com")
    result = await update_user("1", update_data)
    assert result.name == "João Updated"
    assert result.email == "joao.updated@example.com"

@pytest.mark.asyncio
async def test_update_user_non_existing_user(setup_users):
    update_data = UpdateUserDto(name="Non Existing User")
    result = await update_user("999", update_data)
    assert result is None

@pytest.mark.asyncio
async def test_delete_user_existing_user(setup_users):
    result = await delete_user("1")
    assert result is True
    assert len(users) == 2

@pytest.mark.asyncio
async def test_delete_user_non_existing_user(setup_users):
    result = await delete_user("999")
    assert result is False
    assert len(users) == 3