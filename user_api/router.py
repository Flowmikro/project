from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination import paginate, Page, add_pagination
from sqlalchemy import select

from app_config.session_manager import get_session
from models.user_model import UserModel
from .schemas import UserSchema, UserUpdateSchema, UserPaginateSchema

router = APIRouter()


@router.get('/get-users', response_model=Page[UserPaginateSchema])
async def get_users(session: AsyncSession = Depends(get_session)) -> Page[UserPaginateSchema]:
    query = select(UserModel).order_by(UserModel.id)
    result = await session.execute(query)
    users = result.scalars().all()
    return paginate(users)


@router.post('/create-user')
async def create_user(user: UserSchema, session: AsyncSession = Depends(get_session)) -> UserSchema:
    session.add(UserModel(**user.model_dump()))
    await session.commit()
    return user


@router.patch('/update-user/{user_id}')
async def update_user(user_id: int, user_update: UserUpdateSchema,
                      session: AsyncSession = Depends(get_session)) -> dict:
    user_db = await session.get(UserModel, user_id)

    if user_db:
        for attr, value in user_update.model_dump(exclude_unset=True).items():
            setattr(user_db, attr, value)
        await session.commit()

        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')


@router.delete('/delete-user/{user_id}')
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)) -> dict:
    user = await session.get(UserModel, user_id)
    if user:
        await session.delete(user)
        await session.commit()
        return {'message': 'Пользователь удален'}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пользователь не найден')


add_pagination(router)