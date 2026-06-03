
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base

class Reporte(Base):
    __tablename__ = "reportes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    descripcion: Mapped[str] = mapped_column(String(200))
    tipo: Mapped[str] = mapped_column(String(100))

