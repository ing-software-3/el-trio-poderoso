from pydantic import BaseModel
from typing import Optional
from datetime import date


class AlertaCreate(BaseModel):
    producto_id: int
    mensaje: str


class AlertaResponse(BaseModel):
    id: Optional[int] = None
    producto_id: int
    mensaje: str
    fecha_creacion: date

    class Config:
        from_attributes = True