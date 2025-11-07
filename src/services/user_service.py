from typing import Optional
from src.models.schemas import User, CreateUserDto, UpdateUserDto

# Simulação de banco de dados em memória
users: list[User] = [
    User(id="1", name="João Silva", email="joao@example.com", age=30),
    User(id="2", name="Maria Santos", email="maria@example.com", age=25),
    User(id="3", name="Pedro Oliveira", email="pedro@example.com", age=35),
]


async def get_all_users() -> list[User]:
    return users


async def get_user_by_id(user_id: str) -> Optional[User]:
    return next((user for user in users if user.id == user_id), None)


async def create_user(user_data: CreateUserDto) -> User:
    new_user = User(
        id=str(len(users) + 1),
        name=user_data.name,
        email=user_data.email,
        age=user_data.age,
    )
    users.append(new_user)
    return new_user


async def update_user(user_id: str, user_data: UpdateUserDto) -> Optional[User]:
    user_index = next((i for i, user in enumerate(users) if user.id == user_id), None)
    
    if user_index is None:
        return None
    
    user_dict = users[user_index].model_dump()
    update_dict = user_data.model_dump(exclude_unset=True)
    updated_user = User(**{**user_dict, **update_dict})
    users[user_index] = updated_user
    
    return updated_user


async def delete_user(user_id: str) -> bool:
    user_index = next((i for i, user in enumerate(users) if user.id == user_id), None)
    
    if user_index is None:
        return False
    
    users.pop(user_index)
    return True

