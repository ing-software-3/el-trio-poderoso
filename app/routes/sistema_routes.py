from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db  # IMPORT CORRECTO
from app.models.sistemas import Sistema
from app.models.producto import Producto
from app.models.usuarios import Usuario
from app.models.alertas import Alerta
from app.models.reportes import Reporte
from app.schemas.sistema_schema import SistemaUpdate, PanelControlResponse

router = APIRouter(
    prefix="/sistema",
    tags=["Sistema Central"]
)


# ======================================================
# PANEL DE CONTROL (READ)
# ======================================================
@router.get("/panel-control", response_model=PanelControlResponse)
def ver_panel_control(db: Session = Depends(get_db)):

    config = db.query(Sistema).first()

    if not config:
        config = Sistema(
            nombre_sistema="Sistema Liceo Expresiones Pedagógicas",
            modo_mantenimiento=False
        )
        db.add(config)
        db.commit()
        db.refresh(config)

    total_prod = db.query(Producto).count()
    total_user = db.query(Usuario).count()
    total_aler = db.query(Alerta).count()
    total_rep = db.query(Reporte).count()

    return {
        "nombre_sistema": config.nombre_sistema,
        "modo_mantenimiento": config.modo_mantenimiento,
        "total_productos_en_inventario": total_prod,
        "total_usuarios_registrados": total_user,
        "total_alertas_activas": total_aler,
        "total_reportes_generados": total_rep
    }


# ======================================================
# CREAR CONFIGURACIÓN
# ======================================================
@router.post("/inicializar")
def inicializar_sistema(db: Session = Depends(get_db)):

    existe = db.query(Sistema).first()

    if existe:
        return {
            "mensaje": "El sistema ya está inicializado",
            "id": existe.id
        }

    nuevo_sistema = Sistema()
    db.add(nuevo_sistema)
    db.commit()
    db.refresh(nuevo_sistema)

    return {
        "mensaje": "Sistema central inicializado con éxito",
        "id": nuevo_sistema.id
    }


# ======================================================
# ACTUALIZAR CONFIGURACIÓN
# ======================================================
@router.put("/configuracion")
def actualizar_configuracion(item: SistemaUpdate, db: Session = Depends(get_db)):

    config = db.query(Sistema).first()

    if not config:
        raise HTTPException(status_code=404, detail="El sistema no ha sido inicializado")

    config.nombre_sistema = item.nombre_sistema
    config.modo_mantenimiento = item.modo_mantenimiento

    db.commit()

    return {
        "mensaje": "Configuración del sistema actualizada correctamente"
    }


# ======================================================
# BORRAR CONFIGURACIÓN
# ======================================================
@router.delete("/reiniciar")
def reiniciar_sistema(db: Session = Depends(get_db)):

    config = db.query(Sistema).first()

    if not config:
        raise HTTPException(status_code=404, detail="No hay nada que reiniciar")

    db.delete(config)
    db.commit()

    return {
        "mensaje": "Configuración del sistema eliminada"
    }