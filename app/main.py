from fastapi import FastAPI
from app.routes import producto_routes       # ✅ CORRECTO
from app.routes import reporte_routes        # ✅ AGREGA ESTE

app = FastAPI(
    title="Sistema de Inventario - Liceo Infantil Expresiones Pedagógicas",
    description="API para la gestión de materiales didácticos y de oficina"
)

@app.get("/")
def get_start():
    return {
        "mensaje": "Bienvenido al Sistema de Inventario",
        "institucion": "Liceo Infantil Expresiones Pedagógicas",
        "estado": "Online"
    }

<<<<<<< HEAD
# Aquí le decimos a la aplicación que use todas las rutas que hicimos para los productos
=======
# ✅ RUTAS
>>>>>>> 7ee1a10 (trabajo final sandra)
app.include_router(producto_routes.router)
app.include_router(reporte_routes.router)