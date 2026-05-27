from pydantic import BaseModel
from typing import Optional


class Usuario(BaseModel):
    id: Optional[int] = None
    nombre: str
    rol: str
    correo: str
    contraseña: str