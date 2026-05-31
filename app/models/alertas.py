from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import date
from app.db.database import Base

class Alerta(Base):
    __tablename__ = "alertas"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id", ondelete="CASCADE"), nullable=False)
    mensaje = Column(String(255), nullable=False)
    fecha_creacion = Column(Date, default=date.today)

    # Relación con el Producto (como pide tu diagrama +producto: Producto)
    producto = relationship("Producto")
    