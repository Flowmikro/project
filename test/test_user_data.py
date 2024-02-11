from httpx import AsyncClient
from datetime import date

from user_data.data import get_user_registered_in_the_last_week, top_five_users_with_long_names, \
    number_of_specific_domains
from models.user_model import UserModel
from test.conftest import async_session_maker


async def test_create_users():
    async with async_session_maker() as session:
        session.add(UserModel(username='test111test', email='test1@example.com', registration_date=date(2024, 2, 9)))
        session.add(UserModel(username='test12test', email='test2@example.com', registration_date=date(2024, 2, 8)))
        session.add(UserModel(username='test1test', email='test3@example.com', registration_date=date(2024, 2, 7)))
        session.add(UserModel(username='test4tes', email='test4@example.com', registration_date=date(2024, 2, 3)))
        session.add(UserModel(username='test5t', email='test5@example.com', registration_date=date(2024, 2, 6)))
        session.add(UserModel(username='test6', email='test6@example.com', registration_date=date(2024, 2, 1)))
        await session.commit()


async def test_get_user_registered_in_the_last_week():
    async with async_session_maker() as session:
        count_users = await get_user_registered_in_the_last_week(session=session)
        assert count_users == 4


async def test_top_five_users_with_long_names():
    async with async_session_maker() as session:
        top_user_names = [
            'test111test',
            'test12test',
            'test1test',
            'test4tes',
            'test5t',
        ]
        result = await top_five_users_with_long_names(session=session)
        assert top_user_names == result


async def test_number_of_specific_domains():
    async with async_session_maker() as session:
        result = await number_of_specific_domains(session=session)
        assert result == '100.00%'


async def test_get_information(async_client: AsyncClient):
    response = await async_client.get('/information')
    assert response.status_code == 200
    assert response.json() == {
        'Количество пользователей, зарегистрированных за последние 7 дней': 4,
        'Топ-5 пользователей с самыми длинными именами': [
            'test111test',
            'test12test',
            'test1test',
            'test4tes',
            'test5t',
        ],
        "Доля пользователей с доменом электронной почты 'example.com'": '100.00%'
    }
