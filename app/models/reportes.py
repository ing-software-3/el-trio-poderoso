
from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Reporte(Base):
    __tablename__ = "reportes"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(200))
    tipo = Column(String(100))

