from datetime import date
from sqlalchemy import String, Float, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100))
    categoria: Mapped[str] = mapped_column(String(100))
    cantidad: Mapped[int] = mapped_column(Integer)
    precio: Mapped[float] = mapped_column(Float)
    fecha_registro: Mapped[date] = mapped_column(Date)