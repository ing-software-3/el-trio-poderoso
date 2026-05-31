from fastapi import FastAPI
from app.db.database import engine, Base
# ✅ Agrupamos todos los imports de las rutas en un solo lugar limpio
from app.routes import alertas_routes, producto_routes, reporte_routes, inventario_routes, usuarios_routes

# ✅ 1. Primero creamos la aplicación de FastAPI
app = FastAPI(
    title="Sistema de Inventario - Liceo Infantil Expresiones Pedagógicas",
    description="API para la gestión de materiales didácticos y de oficina"
)

# ✅ 2. Creamos las tablas de la base de datos
Base.metadata.create_all(bind=engine)

# ✅ 3. Ruta de bienvenida
@app.get("/")
def get_start():
    return {
        "mensaje": "Bienvenido al Sistema de Inventario",
        "institucion": "Liceo Infantil Expresiones Pedagógicas",
        "estado": "Online"
    }

# ✅ 4. Incluimos TODOS los routers (¡Aquí acomodamos el tuyo abajo de app!)
app.include_router(producto_routes.router)
app.include_router(reporte_routes.router)
app.include_router(usuarios_routes.router)
app.include_router(alertas_routes.router)
app.include_router(inventario_routes.router)  # <--- ¡Listo tu inventario!
