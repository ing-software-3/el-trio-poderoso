from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base

class Sistema(Base):
    __tablename__ = "sistemas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre_sistema: Mapped[str] = mapped_column(String(100), default="Sistema Liceo Expresiones Pedagógicas")
    modo_mantenimiento: Mapped[bool] = mapped_column(Boolean, default=False)