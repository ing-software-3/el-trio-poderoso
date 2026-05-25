from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session as DBSession
from typing import List
<<<<<<< HEAD
<<<<<<< HEAD
from core.database import SessionLocal
from crud import producto_crud
from schemas.producto_schema import ProductoCreate, ProductoResponse, ProductoBase 
=======
from app.core.database import SessionLocal
from app.models import producto_crud
from app.schemas.producto_schema import ProductoCreate, ProductoResponse, ProductoBase
>>>>>>> bbe077c (cambios en la manin antes de subir a la rama)
=======

from app.db.database import SessionLocal
from app.models.producto import Producto
from app.schemas.producto import ProductoCreate, ProductoResponse, ProductoBase
<<<<<<< HEAD
>>>>>>> d508e30 (feat: módulo de productos funcional con conexión a base de datos)
=======
>>>>>>> 7ac7fd6 (feat: modulos reportes funcional)

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

<<<<<<< HEAD
<<<<<<< HEAD

=======
# ✅ conexión a la base de datos
>>>>>>> d508e30 (feat: módulo de productos funcional con conexión a base de datos)
def get_db():
=======
# Con esta función el programa se conecta a la base de datos de XAMPP cada vez que alguien pide algo
def get_db(): # Esta función nos da una sesión para hablar con la base de datos
>>>>>>> bbe077c (cambios en la manin antes de subir a la rama)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ GET → todos los productos
@router.get("/", response_model=List[ProductoResponse])
<<<<<<< HEAD
def listar_productos(db: DBSession = Depends(get_db)): # Usamos DBSession para indicar que es la sesión de la base de datos
    return producto_crud.get_productos(db)
=======
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()
>>>>>>> d508e30 (feat: módulo de productos funcional con conexión a base de datos)

# ✅ GET → producto por ID
@router.get("/{producto_id}", response_model=ProductoResponse)
<<<<<<< HEAD
def obtener_producto(producto_id: int, db: DBSession = Depends(get_db)):
    producto = producto_crud.get_producto(db, producto_id)
=======
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
>>>>>>> d508e30 (feat: módulo de productos funcional con conexión a base de datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# ✅ POST → crear producto
@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
<<<<<<< HEAD
def crear_producto(item: ProductoCreate, db: DBSession = Depends(get_db)):
    return producto_crud.create_producto(db, item)
=======
def crear_producto(item: ProductoCreate, db: Session = Depends(get_db)):
    nuevo = Producto(
        nombre=item.nombre,
        categoria=item.categoria,
        cantidad=item.cantidad,
        precio=item.precio
    )
>>>>>>> d508e30 (feat: módulo de productos funcional con conexión a base de datos)

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo

# ✅ PUT → actualizar producto
@router.put("/{producto_id}", response_model=ProductoResponse)
<<<<<<< HEAD
def actualizar_producto(producto_id: int, item: ProductoBase, db: DBSession = Depends(get_db)):
    producto = producto_crud.update_producto(db, producto_id, item)
=======
def actualizar_producto(producto_id: int, item: ProductoBase, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

>>>>>>> d508e30 (feat: módulo de productos funcional con conexión a base de datos)
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
<<<<<<< HEAD
def eliminar_producto(producto_id: int, db: DBSession = Depends(get_db)):
    if not producto_crud.delete_producto(db, producto_id):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": f"Producto con ID {producto_id} eliminado correctamente"}
=======
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(producto)
    db.commit()

    return {"mensaje": f"Producto con ID {producto_id} eliminado correctamente"}
<<<<<<< HEAD
>>>>>>> d508e30 (feat: módulo de productos funcional con conexión a base de datos)
=======
>>>>>>> 7ac7fd6 (feat: modulos reportes funcional)
