from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db   # ✅ IMPORTANTE
from app.models.producto import Producto
from app.schemas.producto_schema import ProductoCreate, ProductoResponse, ProductoBase

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

@router.get("/", response_model=List[ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()



@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return producto



@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(item: ProductoCreate, db: Session = Depends(get_db)):
    nuevo = Producto(
        nombre=item.nombre,
        categoria=item.categoria,
        cantidad=item.cantidad,
        precio=item.precio,
        fecha_registro=item.fecha_registro
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo

@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(producto_id: int, item: ProductoBase, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    producto.nombre = item.nombre
    producto.categoria = item.categoria
    producto.cantidad = item.cantidad
    producto.precio = item.precio
    producto.fecha_registro = item.fecha_registro

    db.commit()
    db.refresh(producto)

    return producto

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(producto)
    db.commit()

    return {"mensaje": f"Producto con ID {producto_id} eliminado correctamente"}