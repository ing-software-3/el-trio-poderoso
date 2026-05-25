from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from app.core.database import SessionLocal
from app.models.producto import Producto
from app.models.reportes import Reporte
from app.schemas.reporte_schema import ReporteCreate, ReporteResponse

router = APIRouter(
    prefix="/reportes",
    tags=["Reportes"]
)

# ✅ Conexión a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ======================================================
# ✅ REPORTES DINÁMICOS
# ======================================================

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


# ======================================================
# ✅ CRUD DE REPORTES (LO QUE PIDIÓ EL PROFE)
# ======================================================

@router.post("/guardar", response_model=ReporteResponse)
def guardar_reporte(item: ReporteCreate, db: Session = Depends(get_db)):
    nuevo = Reporte(
        descripcion=item.descripcion,
        tipo=item.tipo
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo


@router.get("/historial", response_model=List[ReporteResponse])
def ver_historial(db: Session = Depends(get_db)):
    return db.query(Reporte).all()


@router.delete("/borrar/{reporte_id}")
def eliminar_reporte(reporte_id: int, db: Session = Depends(get_db)):
    reporte = db.query(Reporte).filter(Reporte.id == reporte_id).first()

    if not reporte:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")

    db.delete(reporte)
    db.commit()

    return {"mensaje": f"Reporte {reporte_id} eliminado correctamente"