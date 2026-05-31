from pydantic import BaseModel, EmailStr
from typing import Optional


class UsuarioCreate(BaseModel):
    nombre: str
    rol: str
    correo: EmailStr
    contraseña: str


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    rol: str
    correo: EmailStr

    class Config:
        from_attributes = True  