from fastapi import FastAPI
from app.routes import producto_routes
from app.routes import reporte_routes
from app.core.database import engine, Base
from app.models import reportes

app = FastAPI(
    title="Sistema de Inventario - Liceo Infantil Expresiones Pedagógicas",
    description="API para la gestión de materiales didácticos y de oficina"
)

# ✅ Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

@app.get("/")
def get_start():
    return {
        "mensaje": "Bienvenido al Sistema de Inventario",
        "institucion": "Liceo Infantil Expresiones Pedagógicas",
        "estado": "Online"
    }

# ✅ Rutas
app.include_router(producto_routes.router)
app.include_router(reporte_routes.router)