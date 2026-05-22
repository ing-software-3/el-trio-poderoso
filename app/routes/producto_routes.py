from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session as DBSession
from typing import List
<<<<<<< HEAD
from core.database import SessionLocal
from crud import producto_crud
from schemas.producto_schema import ProductoCreate, ProductoResponse, ProductoBase 
=======
from app.core.database import SessionLocal
from app.models import producto_crud
from app.schemas.producto_schema import ProductoCreate, ProductoResponse, ProductoBase
>>>>>>> bbe077c (cambios en la manin antes de subir a la rama)

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

<<<<<<< HEAD

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

@router.get("/", response_model=List[ProductoResponse])
def listar_productos(db: DBSession = Depends(get_db)): # Usamos DBSession para indicar que es la sesión de la base de datos
    return producto_crud.get_productos(db)

@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener_producto(producto_id: int, db: DBSession = Depends(get_db)):
    producto = producto_crud.get_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(item: ProductoCreate, db: DBSession = Depends(get_db)):
    return producto_crud.create_producto(db, item)

@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(producto_id: int, item: ProductoBase, db: DBSession = Depends(get_db)):
    producto = producto_crud.update_producto(db, producto_id, item)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: DBSession = Depends(get_db)):
    if not producto_crud.delete_producto(db, producto_id):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": f"Producto con ID {producto_id} eliminado correctamente"}
