from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Inventario(Base):
    __tablename__ = "inventarios"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id", ondelete="CASCADE"), nullable=False)
    cantidad = Column(Integer, nullable=False)  # Positivo si entra mercancía, negativo si sale
    fecha_movimiento = Column(DateTime, default=datetime.utcnow)

    # Relación para saber qué producto se movió
    producto = relationship("Producto")