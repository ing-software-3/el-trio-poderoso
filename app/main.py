from fastapi import FastAPI, HTTPException
from datetime import date

from app.models.user import Usuario
from app.models.alerta import Alerta
from app.models.reporte import Reporte
from app.models.inventario import Inventario


# Base de datos
from app.db.database import SessionLocal, engine, Base

# Modelos (SQLAlchemy)
from app.models.producto import Producto

# Schemas (Pydantic)
from pydantic import BaseModel

# ✅ Crear las tablas automáticamente
Base.metadata.create_all(bind=engine)

app = FastAPI()

# ================================
# 📦 SCHEMA (validación de entrada)
# ================================

class ProductoCreate(BaseModel):
    nombre: str
    categoria: str
    cantidad: int
    precio: float
    fecha_registro: date


# ================================
# 🚀 ENDPOINTS
# ================================

@app.get("/")
def get_inicio():
    return {"mensaje": "API Inventario funcionando 🔥"}

@app.on_event("startup")
def startup_event():
    print("✅ Creando tablas...")
    Base.metadata.create_all(bind=engine)


# ✅ Obtener todos los productos
@app.get("/productos")
def get_productos():
    db = SessionLocal()
    productos = db.query(Producto).all()
    db.close()

    return {"codigo": 200, "data": productos}


# ✅ Obtener producto por ID
@app.get("/producto/{producto_id}")
def get_producto(producto_id: int):
    db = SessionLocal()

    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    db.close()

    if producto:
        return {"codigo": 200, "data": producto}

    raise HTTPException(
        status_code=404,
        detail={"codigo": 404, "mensaje": "Producto no encontrado"}
    )


# ✅ Crear producto (INSERT)
@app.post("/producto")
def crear_producto(producto: ProductoCreate):
    db = SessionLocal()

    nuevo_producto = Producto(
        nombre=producto.nombre,
        categoria=producto.categoria,
        cantidad=producto.cantidad,
        precio=producto.precio,
        fecha_registro=producto.fecha_registro
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    db.close()

    return {"mensaje": "Producto creado ✅", "data": nuevo_producto}


# ✅ Actualizar producto
@app.put("/producto/{producto_id}")
def actualizar_producto(producto_id: int, datos: ProductoCreate):
    db = SessionLocal()

    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        db.close()
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    producto.nombre = datos.nombre
    producto.categoria = datos.categoria
    producto.cantidad = datos.cantidad
    producto.precio = datos.precio
    producto.fecha_registro = datos.fecha_registro

    db.commit()
    db.refresh(producto)
    db.close()

    return {"mensaje": "Producto actualizado ✅", "data": producto}


# ✅ Eliminar producto
@app.delete("/producto/{producto_id}")
def eliminar_producto(producto_id: int):
    db = SessionLocal()

    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        db.close()
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(producto)
    db.commit()
    db.close()

    return {"mensaje": "Producto eliminado ✅"}

