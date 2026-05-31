from pydantic import BaseModel
from typing import Optional
from datetime import date

# Este es el esquema que usa el PUT para recibir los datos editados
class ProductoBase(BaseModel):
    nombre: str
    categoria: str
    cantidad: int  
    precio: float
    fecha_registro: Optional[date] = None
    
class ProductoCreate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id: int

    class Config:
        from_attributes = True