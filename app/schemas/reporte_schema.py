
from pydantic import BaseModel

class ReporteBase(BaseModel):
    descripcion: str
    tipo: str

class ReporteCreate(ReporteBase):
    pass

class ReporteResponse(ReporteBase):
    id: int

    class Config:
        from_attributes = True
