from sqlalchemy import String, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from app_config.session_manager import Base


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(unique=True)
    registration_date: Mapped[date] = mapped_column(Date, default=date.today())





