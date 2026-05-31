from fastapi import FastAPI
from app.db.database import engine, Base

#  1. Importamos todos los routers de las rutas en un solo lugar limpio
from app.routes import (
    producto_routes,
    reporte_routes,
    usuarios_routes,
    alertas_routes,
    inventario_routes,
    sistema_routes  # <-- ¡Tu nuevo router del sistema central!
)

#  2. TRUCO DIRECTO EN LA MAIN (Para que cree la tabla sin usar __init__.py)
# Al importar el modelo aquí mismo, SQLAlchemy lo lee al arrancar y crea la tabla "sistemas"
from app.models.sistemas import Sistema 


#  3. Creamos la aplicación de FastAPI con los datos del Liceo
app = FastAPI(
    title="Sistema de Inventario - Liceo Infantil Expresiones Pedagógicas",
    description="API para la gestión de materiales didácticos y de oficina"
)


# 4. Creamos las tablas de la base de datos automáticamente
Base.metadata.create_all(bind=engine)


# 5. Ruta de bienvenida en la raíz de la API
@app.get("/")
def get_start():
    return {
        "mensaje": "Bienvenido al Sistema de Inventario",
        "institucion": "Liceo Infantil Expresiones Pedagógicas",
        "estado": "Online"
    }


#  6. Incluimos TODOS los routers para que aparezcan en Swagger
app.include_router(producto_routes.router)
app.include_router(reporte_routes.router)
app.include_router(usuarios_routes.router)
app.include_router(alertas_routes.router)
app.include_router(inventario_routes.router)
app.include_router(sistema_routes.router)  # <--- ¡Tu Sistema Central conectado con éxito!