from datetime import date
from sqlalchemy import Date, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base

class Reporte(Base):
    __tablename__ = "reportes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fecha_generacion: Mapped[date] = mapped_column(Date)
    datos: Mapped[dict] = mapped_column(JSON)