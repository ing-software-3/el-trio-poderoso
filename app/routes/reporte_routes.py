<<<<<<< HEAD
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.reporte_schema import ReporteCreate, ReporteResponse
=======

from fastapi import APIRouter
>>>>>>> bbe077c (cambios en la manin antes de subir a la rama)

router = APIRouter(
    prefix="/reportes",
    tags=["Reportes"]
)

<<<<<<< HEAD
# Base temporal (lista en memoria)
reportes_db = []

@router.get("/", response_model=List[ReporteResponse])
def listar_reportes():
    return reportes_db

@router.get("/{reporte_id}", response_model=ReporteResponse)
def obtener_reporte(reporte_id: int):
    for reporte in reportes_db:
        if reporte["id"] == reporte_id:
            return reporte
    raise HTTPException(status_code=404, detail="Reporte no encontrado")

@router.post("/", response_model=ReporteResponse)
def crear_reporte(reporte: ReporteCreate):
    nuevo = reporte.dict()
    nuevo["id"] = len(reportes_db) + 1
    reportes_db.append(nuevo)
    return nuevo

@router.put("/{reporte_id}", response_model=ReporteResponse)
def actualizar_reporte(reporte_id: int, reporte: ReporteCreate):
    for i, r in enumerate(reportes_db):
        if r["id"] == reporte_id:
            reportes_db[i].update(reporte.dict())
            return reportes_db[i]
    raise HTTPException(status_code=404, detail="Reporte no encontrado")

@router.delete("/{reporte_id}")
def eliminar_reporte(reporte_id: int):
    for i, r in enumerate(reportes_db):
        if r["id"] == reporte_id:
            reportes_db.pop(i)
            return {"mensaje": "Reporte eliminado"}
    raise HTTPException(status_code=404, detail="Reporte no encontrado")
=======
@router.get("/")
def obtener_reportes():
    return {
        "total_productos": 1,
        "inventario_total": 10,
        "mensaje": "Reporte general del sistema funcionando"
    }
>>>>>>> bbe077c (cambios en la manin antes de subir a la rama)
