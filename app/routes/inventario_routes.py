from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import SessionLocal
from app.models.producto import Producto

router = APIRouter(
    prefix="/inventario",
    tags=["Inventario"]
)

# ✅ Conexión a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ======================================================
# ✅ OPERACIONES DE INVENTARIO
# ======================================================

# 1. Registrar Entrada (Aumentar Stock)
@router.put("/registrar-entrada/{producto_id}")
def registrar_entrada(producto_id: int, cantidad: int, db: Session = Depends(get_db)):
    if cantidad <= 0:
        raise HTTPException(status_code=400, detail="La cantidad debe ser mayor a cero")
        
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    producto.cantidad += cantidad
    db.commit()
    db.refresh(producto)
    
    return {
        "mensaje": f"Entrada registrada. Se sumaron {cantidad} unidades.",
        "producto": producto.nombre,
        "nuevo_stock": producto.cantidad
    }


# 2. Registrar Salida (Disminuir Stock)
@router.put("/registrar-salida/{producto_id}")
def registrar_salida(producto_id: int, cantidad: int, db: Session = Depends(get_db)):
    if cantidad <= 0:
        raise HTTPException(status_code=400, detail="La cantidad debe ser mayor a cero")
        
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
        
    if producto.cantidad < cantidad:
        raise HTTPException(
            status_code=400, 
            detail=f"Stock insuficiente. Solo hay {producto.cantidad} unidades disponibles."
        )
    
    producto.cantidad -= cantidad
    db.commit()
    db.refresh(producto)
    
    return {
        "mensaje": f"Salida registrada. Se restaron {cantidad} unidades.",
        "producto": producto.nombre,
        "nuevo_stock": producto.cantidad
    }


# 3. Consultar Stock de un Producto Específico
@router.get("/consultar-stock/{producto_id}")
def consultar_stock(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
        
    return {
        "producto_id": producto.id,
        "producto": producto.nombre,
        "stock_actual": producto.cantidad
    }