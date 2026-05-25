<<<<<<< HEAD
<<<<<<< HEAD
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.reporte_schema import ReporteCreate, ReporteResponse
=======

from fastapi import APIRouter
>>>>>>> bbe077c (cambios en la manin antes de subir a la rama)
=======
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import func
>>>>>>> 7c6b5c2 (fix:limpieza final y estructura del proyecto)

from app.db.database import SessionLocal  # ✅ CORREGIDO
from app.models.producto import Producto
from app.models.reportes import Reporte
from app.schemas.reporte_schema import ReporteCreate, ReporteResponse

router = APIRouter(
    prefix="/reportes",
    tags=["Reportes"]
)

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
# Función para conectar a la DB
=======
# conexión a la base de datos
>>>>>>> 7ac7fd6 (feat: modulos reportes funcional)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- REPORTES DINÁMICOS ---

@router.get("/inversion-total")
def reporte_inversion(db: Session = Depends(get_db)):
    total = db.query(func.sum(Producto.precio * Producto.cantidad)).scalar()
    return {
        "titulo": "Reporte de Inversión Total",
        "valor_total": total if total else 0,
        "mensaje": "Este es el capital total en productos"
    }

@router.get("/stock-bajo")
def reporte_stock_bajo(db: Session = Depends(get_db)):
    productos_criticos = db.query(Producto).filter(Producto.cantidad <= 5).all()
    return {
        "titulo": "Reporte de Productos por Agotarse",
        "cantidad_criticos": len(productos_criticos),
        "productos": productos_criticos
    }

# --- REPORTES GUARDADOS ---

@router.post("/guardar", response_model=ReporteResponse)
def guardar_registro_reporte(item: ReporteCreate, db: Session = Depends(get_db)):
    nuevo_reporte = Reporte(
        descripcion=item.descripcion,
        tipo=item.tipo
    )
    db.add(nuevo_reporte)
    db.commit()
    db.refresh(nuevo_reporte)
    return nuevo_reporte

@router.get("/historial", response_model=List[ReporteResponse])
def ver_historial_reportes(db: Session = Depends(get_db)):
    return db.query(Reporte).all()

@router.delete("/borrar/{reporte_id}")
def eliminar_reporte_guardado(reporte_id: int, db: Session = Depends(get_db)):
    reporte = db.query(Reporte).filter(Reporte.id == reporte_id).first()
    if not reporte:
        raise HTTPException(status_code=404, detail="Ese registro de reporte no existe")
    
    db.delete(reporte)
    db.commit()
    return {"mensaje": f"Reporte {reporte_id} borrado correctamente"}
>>>>>>> 7c6b5c2 (fix:limpieza final y estructura del proyecto)
