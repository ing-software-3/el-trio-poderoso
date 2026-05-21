from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base

class Alerta(Base):
    __tablename__ = "alertas"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    mensaje: Mapped[str] = mapped_column(String(255))
    fecha_creacion: Mapped[date] = mapped_column(Date)

    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"))