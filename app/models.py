from sqlalchemy import Text, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Teacher(Base):
	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str] = mapped_column(nullable=False)
	description_teacher: Mapped[str] = mapped_column(Text, nullable=True)
	img: Mapped[str] = mapped_column(String(50), nullable=True)


class News(Base):
	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str] = mapped_column(nullable=False)
	description_new: Mapped[str] = mapped_column(Text, nullable=True)
	img: Mapped[str] = mapped_column(String(50), nullable=True)