from sqlalchemy import Column, Integer, String, Float, Date
from app.db.database import Base
from datetime import date

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    categoria = Column(String(100))
    cantidad = Column(Integer)
    precio = Column(Float)
    fecha_registro = Column(Date, default=date.today)
