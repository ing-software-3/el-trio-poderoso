from fastapi import FastAPI
from app.routes import usuarios, alertas
from app.routes import producto_routes, reporte_routes
from app.db.database import engine, Base

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
app.include_router(usuarios.router)
app.include_router(alertas.router)  