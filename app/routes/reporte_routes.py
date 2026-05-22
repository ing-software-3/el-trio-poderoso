
from fastapi import APIRouter

router = APIRouter(
    prefix="/reportes",
    tags=["Reportes"]
)

@router.get("/")
def obtener_reportes():
    return {
        "total_productos": 1,
        "inventario_total": 10,
        "mensaje": "Reporte general del sistema funcionando"
    }
