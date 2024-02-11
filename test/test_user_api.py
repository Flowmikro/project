from httpx import AsyncClient


async def test_create_user(async_client: AsyncClient):
    """
    Тест для проверки создания пользователя, post запрос
    """
    user = {
        "username": "test name",
        "email": "test@test.com"
    }
    response = await async_client.post('/create-user', json=user)
    assert response.status_code == 200
    assert response.json() == user


async def test_get_users(async_client: AsyncClient):
    """
    Тест для вывода пользователей и пагинации, get запрос
    """
    response = await async_client.get('/get-users')
    assert response.status_code == 200
    data = response.json()
    assert 'items' in data
    assert 'page' in data
    assert 'pages' in data
    assert 'size' in data


async def test_update_user(async_client: AsyncClient):
    """
    Тест для проверки обновления пользователя, patch запрос
    """
    user_id = 1
    response = await async_client.patch(f'/update-user/{user_id}', json={
        "username": "New test name",
        "email": "newtest@test.com"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "User updated successfully"}


async def test_update_user_id_not_found(async_client: AsyncClient):
    """
    Тест для проверки ошибки 'пользователь не найден', patch запрос
    """
    user_id = 99
    response = await async_client.patch(f'/update-user/{user_id}', json={
        "username": "New test name",
        "email": "newtest@test.com"
    })
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


async def test_delete_user(async_client: AsyncClient):
    """
    Тест для проверки удаления пользователя, delete запрос
    """
    user_id = 1
    response = await async_client.delete(f'/delete-user/{user_id}')
    assert response.status_code == 200
    assert response.json() == {'message': 'Пользователь удален'}


async def test_delete_user_id_not_found(async_client: AsyncClient):
    """
    Тест для проверки ошибки 'пользователь не найден', delete запрос
    """
    user_id = 99
    response = await async_client.delete(f'/delete-user/{user_id}')
    assert response.status_code == 404
    assert response.json() == {"detail": "Пользователь не найден"}
