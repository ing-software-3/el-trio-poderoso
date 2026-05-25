from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Esquema de datos que coincide con tu base de datos en MySQL
class ProductoBase(BaseModel):
    nombre: str
    categoria: str
    stock: int
    precio: float
    fecha_registro: Optional[datetime] = None
    
class ProductoCreate(ProductoBase):
    pass # No necesitamos campos adicionales para la creación por ahora

class ProductoResponse(ProductoBase):
    id: int
    fecha_registro: datetime

    class Config:
        from_attributes = True