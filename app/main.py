from fastapi import FastAPI
from app.db.database import engine, Base

# IMPORTAR TODOS LOS MODELOS
import app.models.producto
import app.models.reportes
import app.models.usuarios
import app.models.alertas
import app.models.inventarios
import app.models.sistemas

# IMPORTAR TODOS LOS ROUTERS
from app.routes import (
    producto_routes,
    reporte_routes,
    usuarios_routes,
    alertas_routes,
    inventario_routes,
    sistema_routes
)

# CREAR APP
app = FastAPI(
    title="Sistema de Inventario - Liceo Infantil Expresiones Pedagógicas",
    description="API para la gestión de materiales didácticos y de oficina"
)

# CREAR TABLAS
Base.metadata.create_all(bind=engine)

"""
# RUTA INICIAL
@app.get("/")
def get_start():
    return {
        "mensaje": "Bienvenido al Sistema de Inventario",
        "institucion": "Liceo Infantil Expresiones Pedagógicas",
        "estado": "Online"
    }
"""

# INCLUIR TODOS LOS ROUTERS
app.include_router(producto_routes.router)
app.include_router(reporte_routes.router)
app.include_router(usuarios_routes.router)
app.include_router(alertas_routes.router)
app.include_router(inventario_routes.router)
app.include_router(sistema_routes.router)