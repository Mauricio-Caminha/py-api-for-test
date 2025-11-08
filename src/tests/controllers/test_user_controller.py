import pytest
from unittest.mock import patch, AsyncMock
from fastapi import HTTPException
from src.controllers.user_controller import get_all_users, get_user_by_id, create_user, update_user, delete_user
from src.models.schemas import User, CreateUserDto, UpdateUserDto

@pytest.mark.asyncio
class TestUserController:
    
    @patch('src.services.user_service.get_all_users', new_callable=AsyncMock)
    async def test_get_all_users(self, mock_get_all_users):
        """Should return a list of users"""
        mock_get_all_users.return_value = [User(id="1", name="John", email="john@example.com")]
        
        result = await get_all_users()
        
        assert len(result) == 1
        assert result[0].name == "John"
    
    @patch('src.services.user_service.get_user_by_id', new_callable=AsyncMock)
    async def test_get_user_by_id_when_exists(self, mock_get_user_by_id):
        """Should return user when id exists"""
        mock_user = User(id="1", name="John", email="john@example.com")
        mock_get_user_by_id.return_value = mock_user
        
        result = await get_user_by_id("1")
        
        assert result.id == "1"
        assert result.name == "John"
    
    @patch('src.services.user_service.get_user_by_id', new_callable=AsyncMock)
    async def test_get_user_by_id_when_not_exists(self, mock_get_user_by_id):
        """Should raise HTTPException when user not found"""
        mock_get_user_by_id.return_value = None
        
        with pytest.raises(HTTPException) as exc_info:
            await get_user_by_id("999")
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "User not found"
    
    @patch('src.services.user_service.create_user', new_callable=AsyncMock)
    async def test_create_user(self, mock_create_user):
        """Should create a new user"""
        user_data = CreateUserDto(name="Jane", email="jane@example.com")
        mock_user = User(id="2", name="Jane", email="jane@example.com")
        mock_create_user.return_value = mock_user
        
        result = await create_user(user_data)
        
        assert result.id == "2"
        assert result.name == "Jane"
    
    @patch('src.services.user_service.update_user', new_callable=AsyncMock)
    async def test_update_user_when_exists(self, mock_update_user):
        """Should update user when id exists"""
        user_data = UpdateUserDto(name="John Doe", email="john.doe@example.com")
        mock_user = User(id="1", name="John Doe", email="john.doe@example.com")
        mock_update_user.return_value = mock_user
        
        result = await update_user("1", user_data)
        
        assert result.id == "1"
        assert result.name == "John Doe"
    
    @patch('src.services.user_service.update_user', new_callable=AsyncMock)
    async def test_update_user_when_not_exists(self, mock_update_user):
        """Should raise HTTPException when user not found"""
        user_data = UpdateUserDto(name="John Doe", email="john.doe@example.com")
        mock_update_user.return_value = None
        
        with pytest.raises(HTTPException) as exc_info:
            await update_user("999", user_data)
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "User not found"
    
    @patch('src.services.user_service.delete_user', new_callable=AsyncMock)
    async def test_delete_user_when_exists(self, mock_delete_user):
        """Should delete user when id exists"""
        mock_delete_user.return_value = True
        
        result = await delete_user("1")
        
        assert result == {"message": "User deleted successfully"}
    
    @patch('src.services.user_service.delete_user', new_callable=AsyncMock)
    async def test_delete_user_when_not_exists(self, mock_delete_user):
        """Should raise HTTPException when user not found"""
        mock_delete_user.return_value = False
        
        with pytest.raises(HTTPException) as exc_info:
            await delete_user("999")
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "User not found"