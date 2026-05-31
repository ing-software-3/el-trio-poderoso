from fastapi import FastAPI
from app.db.database import engine, Base


import app.models.producto
import app.models.reportes
import app.models.usuarios
import app.models.alertas


from app.routes import alertas_routes, producto_routes, reporte_routes, inventario_routes, usuarios_routes

app = FastAPI(
    title="Sistema de Inventario - Liceo Infantil Expresiones Pedagógicas",
    description="API para la gestión de materiales didácticos y de oficina"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def get_start():
    return {
        "mensaje": "Bienvenido al Sistema de Inventario",
        "institucion": "Liceo Infantil Expresiones Pedagógicas",
        "estado": "Online"
    }

app.include_router(producto_routes.router)
app.include_router(reporte_routes.router)
app.include_router(usuarios_routes.router)
app.include_router(alertas_routes.router)
app.include_router(inventario_routes.router)
