from pydantic import BaseModel
from typing import Optional
from datetime import date

# Lo que enviamos desde Swagger para crear la alerta
class AlertaCreate(BaseModel):
    producto_id: int
    mensaje: str

# Lo que Swagger nos responde con los datos de la base de datos
class AlertaResponse(BaseModel):
    id: int
    producto_id: int
    mensaje: str
    fecha_creacion: date

    class Config:
        from_attributes = True