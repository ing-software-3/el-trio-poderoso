from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import SessionLocal
from app.models.producto import Producto
from app.schemas.producto import ProductoCreate, ProductoResponse, ProductoBase

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

# ✅ conexión a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ GET → todos los productos
@router.get("/", response_model=List[ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()

# ✅ GET → producto por ID
@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# ✅ POST → crear producto
@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(item: ProductoCreate, db: Session = Depends(get_db)):
    nuevo = Producto(
        nombre=item.nombre,
        categoria=item.categoria,
        cantidad=item.cantidad,
        precio=item.precio
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo

# ✅ PUT → actualizar producto
@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(producto_id: int, item: ProductoBase, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    producto.nombre = item.nombre
    producto.categoria = item.categoria
    producto.cantidad = item.cantidad
    producto.precio = item.precio

    db.commit()
    db.refresh(producto)

    return producto

# ✅ DELETE → eliminar producto
@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(producto)
    db.commit()

    return {"mensaje": f"Producto con ID {producto_id} eliminado correctamente"}