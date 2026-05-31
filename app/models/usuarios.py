from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    rol = Column(String(50))
    correo = Column(String(100), unique=True)
    contraseña = Column(String(100))
