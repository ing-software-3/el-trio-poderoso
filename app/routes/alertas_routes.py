from fastapi import APIRouter
from datetime import date
from app.schemas.alertas_schema import AlertaCreate, AlertaResponse

router = APIRouter(prefix="/alertas", tags=["Alertas"])

alertas = []
contador_alertas = 1


@router.post("/", response_model=AlertaResponse)
def crear_alerta(alerta: AlertaCreate):
    global contador_alertas

    nueva_alerta = {
        "id": contador_alertas,
        "producto_id": alerta.producto_id,
        "mensaje": alerta.mensaje,
        "fecha_creacion": date.today()
    }

    alertas.append(nueva_alerta)
    contador_alertas += 1

    return nueva_alerta


@router.get("/", response_model=list[AlertaResponse])
def listar_alertas():
    return alertas