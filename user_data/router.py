from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app_config.session_manager import get_session
from . import data


router = APIRouter()


@router.get('/information')
async def get_information(session: AsyncSession = Depends(get_session)) -> dict:
    return {
        'Количество пользователей, зарегистрированных за последние 7 дней': await data.get_user_registered_in_the_last_week(session=session),
        'Топ-5 пользователей с самыми длинными именами': await data.top_five_users_with_long_names(session=session),
        "Доля пользователей с доменом электронной почты 'example.com'": await data.number_of_specific_domains(session=session),
    }
