from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Estos son como los formularios que creamos para que los datos de los productos queden bien organizados
class ProductoBase(BaseModel):
    nombre: str
    categoria: str
    cantidad: int
    precio: float
    fecha_registro: Optional[datetime] = None
    
class ProductoCreate(ProductoBase):
    pass # Aquí usamos los mismos datos de arriba porque para crear el producto no necesitamos nada extra

class ProductoResponse(ProductoBase):
    id: int
    fecha_registro: datetime

    class Config:
        from_attributes = True