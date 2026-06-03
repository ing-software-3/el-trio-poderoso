from sqlalchemy import String, Integer, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from app.db.database import Base
from app.models.producto import Producto

class Alerta(Base):
    __tablename__ = "alertas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    producto_id: Mapped[int] = mapped_column(Integer, ForeignKey("productos.id", ondelete="CASCADE"), nullable=False)
    mensaje: Mapped[str] = mapped_column(String(255), nullable=False)
    fecha_creacion: Mapped[date] = mapped_column(Date, default=date.today)

    # Relación con el Producto
    producto: Mapped[Producto] = relationship("Producto")
    