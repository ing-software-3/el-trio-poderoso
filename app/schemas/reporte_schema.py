<<<<<<< HEAD

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
=======
from pydantic import BaseModel

class ReporteCreate(BaseModel):
    descripcion: str
    tipo: str

class ReporteResponse(BaseModel):
    id: int
    descripcion: str
    tipo: str

    class Config:
        from_attributes = True
>>>>>>> 7ac7fd6 (feat: modulos reportes funcional)
