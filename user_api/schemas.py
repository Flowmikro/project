from datetime import date

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    """
    Схема пользователя
    """
    username: str
    email: EmailStr


class UserUpdateSchema(BaseModel):
    """
    Схема для patch запроса
    """
    username: str | None = None
    email: EmailStr | None = None


class UserPaginateSchema(UserSchema):
    """
    Схема для пагинации
    """
    registration_date: date
