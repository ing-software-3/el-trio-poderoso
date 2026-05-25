from pydantic import BaseModel

# ✅ Base para crear o actualizar reportes
class ReporteBase(BaseModel):
    descripcion: str
    tipo: str


# ✅ Para crear reporte
class ReporteCreate(ReporteBase):
    pass


# ✅ Respuesta que devuelve la API
class ReporteResponse(ReporteBase):
    id: int

    class Config:
        from_attributes = True