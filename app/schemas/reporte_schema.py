from pydantic import BaseModel
from typing import Optional

# Este es el molde para cuando creamos o actualizamos un reporte
class ReporteBase(BaseModel):
    descripcion: str
    tipo: str # Ejemplo: "Inversión", "Stock Bajo", "Mensual"

class ReporteCreate(ReporteBase):
    pass

class ReporteResponse(ReporteBase):
    id: int
    class Config:
        from_attributes = True