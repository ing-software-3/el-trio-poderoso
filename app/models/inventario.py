from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer
from app.db.database import Base

class Inventario(Base):
    __tablename__ = "inventarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
