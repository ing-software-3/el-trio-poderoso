from fastapi import FastAPI
from app.db.database import engine, Base

# IMPORTAR TODOS LOS MODELOS
from app.models import (
    producto,  # noqa: F401
    reportes,  # noqa: F401
    usuarios,  # noqa: F401
    alertas,  # noqa: F401
    inventarios,  # noqa: F401
    sistemas,  # noqa: F401
)

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
app: FastAPI = FastAPI(
    title="Sistema de Inventario - Liceo Infantil Expresiones Pedagógicas",
    description="API para la gestión de materiales didácticos y de oficina"
)

# CREAR TABLAS
Base.metadata.create_all(bind=engine)

"""
# RUTA INICIAL
@app.get("/", tags=["Inicio"])
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