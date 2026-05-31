from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class Sistema(Base):
    __tablename__ = "sistemas"

    id = Column(Integer, primary_key=True, index=True)
    nombre_sistema = Column(String(100), default="Sistema Liceo Expresiones Pedagógicas")
    modo_mantenimiento = Column(Boolean, default=False)