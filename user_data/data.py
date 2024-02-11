from datetime import date, timedelta
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app_config.session_manager import get_session
from models.user_model import UserModel


async def get_user_registered_in_the_last_week(session: AsyncSession = Depends(get_session)):
    """
    Получаем результат количество пользователей, зарегистрированных за последние 7 дней.
    """
    count_user = await session.execute(
        select(func.count()).where(UserModel.registration_date >= date.today() - timedelta(days=7))
    )
    return count_user.scalar()


async def top_five_users_with_long_names(session: AsyncSession = Depends(get_session)):
    """
    Получаем топ-5 пользователей с самыми длинными именами
    """
    top_users = await session.execute(
        select(UserModel.username)
        .order_by(func.length(UserModel.username).desc())
        .limit(5)
    )

    return top_users.scalars().all()


async def number_of_specific_domains(session: AsyncSession = Depends(get_session)):
    """
    Получаем долю пользователей с адресами электронной почты 'example.com'
    """
    total_users = await session.execute(select(func.count(UserModel.id)))
    total_users = total_users.scalar()

    users_with_specific_domain = await session.execute(select(func.count()).filter(
        UserModel.email.like('%@example.com')
    ))

    users_with_specific_domain = users_with_specific_domain.scalar()
    percentage_users_with_specific_domain = (users_with_specific_domain / total_users) * 100
    return f'{percentage_users_with_specific_domain:.2f}%'  # результат в процентах
