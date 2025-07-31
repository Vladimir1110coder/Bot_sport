from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Text, func, String, DateTime

class Base(DeclarativeBase):
    create: Mapped[DateTime] = mapped_column(DateTime, default = func.now())
    update: Mapped[DateTime] = mapped_column(DateTime, default = func.now(), onupdate = func.now())

class Player(Base):
    __tablename__ = 'Player'

    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    name: Mapped[str] = mapped_column(String(150), nullable = False)
    word: Mapped[str] = mapped_column(String(150), nullable = False)
