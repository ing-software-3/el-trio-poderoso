from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from datetime import datetime


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100))
    categoria: Mapped[str] = mapped_column(String(100))
    cantidad: Mapped[int] = mapped_column(Integer, default=0)
    precio: Mapped[float] = mapped_column(Float)
    fecha_registro: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


    # Esta parte la hicimos siguiendo el dibujo del diagrama de clases que nos pidió el profe