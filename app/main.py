from fastapi import FastApi
from pydantic import BaseModel

app = FastApi()

productos = [
    {"id": 1, "producto": "Monitor", "precio": 5000},
    {"id": 2, "producto": "Teclado", "precio": 5000},
    {"id": 3, "producto": "Mouse", "precio": 5000},
    {"id": 4, "producto": "Celular", "precio": 5000},
]

class Producto(BaseModel):
    id: int
    producto: str
    precio: float

@app.get("/")
def get_start():
    return {"clase": "sofware III"}

@app.get("/productos")
def get_productos():
    return {"codigo": 200, "data": productos}

@app.get("/producto/{producto_id}")
def get_producto (producto_id: int):
    for producto in productos:
        if producto["id"] == producto_id:
            return {"codigo": 200, "data": producto}
    raise HTTPException(status_code=404, detail={"codigo": 404, "mensaje": "Producto no encontrado"})
