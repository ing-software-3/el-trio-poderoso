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
from app.core.database import SessionLocal
from app.models.products import Product 
from app.models.reportes import Reporte # El modelo para guardar en la BD
from app.schemas.reporte_schema import ReporteCreate, ReporteResponse
from sqlalchemy import func
>>>>>>> 7c6b5c2 (fix:limpieza final y estructura del proyecto)

router = APIRouter(
    prefix="/reportes",
    tags=["Reportes"]
)

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
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- OPCIONES DE CÁLCULO (DINÁMICAS) ---

@router.get("/inversion-total")
def reporte_inversion(db: Session = Depends(get_db)):
    # Hacemos la suma: precio * stock de todos los productos
    total = db.query(func.sum(Product.precio * Product.stock)).scalar()
    return {
        "titulo": "Reporte de Inversión Total",
        "valor_total": total if total else 0,
        "mensaje": "Este es el capital total en productos"
    }

@router.get("/stock-bajo")
def reporte_stock_bajo(db: Session = Depends(get_db)):
    # Buscamos productos que tengan 5 o menos (puedes cambiar el 5)
    productos_criticos = db.query(Product).filter(Product.stock <= 5).all()
    return {
        "titulo": "Reporte de Productos por Agotarse",
        "cantidad_criticos": len(productos_criticos),
        "productos": productos_criticos
    }

# --- OPCIONES DE GESTIÓN (LO QUE PIDIÓ EL PROFE: POST, DELETE) ---

# Esta opción permite guardar un comentario o registro de un reporte (POST)
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

# Esta opción permite ver todos los reportes que hemos guardado
@router.get("/historial", response_model=List[ReporteResponse])
def ver_historial_reportes(db: Session = Depends(get_db)):
    return db.query(Reporte).all()

# Esta opción permite borrar un reporte guardado (DELETE)
@router.delete("/borrar/{reporte_id}")
def eliminar_reporte_guardado(reporte_id: int, db: Session = Depends(get_db)):
    reporte = db.query(Reporte).filter(Reporte.id == reporte_id).first()
    if not reporte:
        raise HTTPException(status_code=404, detail="Ese registro de reporte no existe")
    
    db.delete(reporte)
    db.commit()
    return {"mensaje": f"Reporte {reporte_id} borrado correctamente"}
>>>>>>> 7c6b5c2 (fix:limpieza final y estructura del proyecto)
