from fastapi import FastAPI
<<<<<<< HEAD
from app.routes import producto_routes       # ✅ CORRECTO
from app.routes import reporte_routes        # ✅ AGREGA ESTE
=======
from app.routes import producto_routes
from app.routes import reporte_routes
from app.core.database import engine, Base
from app.models import reportes
>>>>>>> bbe077c (cambios en la manin antes de subir a la rama)


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

<<<<<<< HEAD
<<<<<<< HEAD
# Aquí le decimos a la aplicación que use todas las rutas que hicimos para los productos
=======
# ✅ RUTAS
>>>>>>> 7ee1a10 (trabajo final sandra)
=======
# ✅ Rutas
>>>>>>> bbe077c (cambios en la manin antes de subir a la rama)
app.include_router(producto_routes.router)
app.include_router(reporte_routes.router)