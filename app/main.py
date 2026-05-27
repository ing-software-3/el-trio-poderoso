from fastapi import FastAPI
from routes import usuarios
from app.routes import producto_routes
from app.routes import reporte_routes
from app.db.database import engine, Base

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

# ✅ RUTAS
app.include_router(producto_routes.router)
app.include_router(reporte_routes.router)

app.include_router(usuarios.router)