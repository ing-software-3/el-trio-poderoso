import enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base

class UserRole(str, enum.Enum):
    admin = "admin"
    user = "user"

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100))
    correo: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    contraseña: Mapped[str] = mapped_column(String(255))
    rol: Mapped[str] = mapped_column(
        String(10),
        default=UserRole.user.value,
        nullable=False
    )