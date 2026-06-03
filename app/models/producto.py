from sqlalchemy import String, Integer, Float, Date
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base
from datetime import date
from typing import Optional

class Producto(Base):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100))
    categoria: Mapped[str] = mapped_column(String(100))
    cantidad: Mapped[int] = mapped_column(Integer)
    precio: Mapped[float] = mapped_column(Float)
    fecha_registro: Mapped[Optional[date]] = mapped_column(Date, default=date.today, nullable=True)