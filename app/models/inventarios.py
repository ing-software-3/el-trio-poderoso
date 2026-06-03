from sqlalchemy import Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from app.db.database import Base
from app.models.producto import Producto

class Inventario(Base):
    __tablename__ = "inventarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    producto_id: Mapped[int] = mapped_column(Integer, ForeignKey("productos.id", ondelete="CASCADE"), nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)  # Positivo si entra mercancía, negativo si sale
    fecha_movimiento: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))

    # Relación para saber qué producto se movió
    producto: Mapped[Producto] = relationship("Producto")