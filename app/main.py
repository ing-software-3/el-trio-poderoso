from fastapi import FastAPI
from app.routes import producto_routes

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

# Aquí le decimos a la aplicación que use todas las rutas que hicimos para los productos
app.include_router(producto_routes.router)
