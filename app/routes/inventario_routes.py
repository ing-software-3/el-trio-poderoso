from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.producto import Producto
from app.models.inventarios import Inventario
from app.models.alertas import Alerta
from app.schemas.inventario_schema import MovimientoInventario, RespuestaInventario

router = APIRouter(
    prefix="/inventario",
    tags=["Inventario"]
)

# MOVER INVENTARIO
@router.post("/mover", response_model=RespuestaInventario, status_code=status.HTTP_201_CREATED)
def mover_inventario(item: MovimientoInventario, db: Session = Depends(get_db)):

    producto = db.query(Producto).filter(Producto.id == item.producto_id).first()
    
    if not producto:
        raise HTTPException(status_code=404, detail="El producto no existe")

    nuevo_stock = producto.cantidad + item.cantidad

    # CORREGIDO AQUÍ
    if nuevo_stock < 0:
        raise HTTPException(
            status_code=400,
            detail=f"Inventario insuficiente. Solo tienes {producto.cantidad} unidades disponibles."
        )

    producto.cantidad = nuevo_stock

    nuevo_movimiento = Inventario(
        producto_id=item.producto_id,
        cantidad=item.cantidad
    )

    db.add(nuevo_movimiento)
    
    # Generar alerta automática si el stock es bajo (<= 5 unidades) (RF08)
    if nuevo_stock <= 5:
        alerta_existente = db.query(Alerta).filter(
            Alerta.producto_id == item.producto_id,
            Alerta.mensaje.like("%Stock bajo%")
        ).first()
        
        if not alerta_existente:
            alerta_automatica = Alerta(
                producto_id=item.producto_id,
                mensaje=f"Stock bajo: El producto '{producto.nombre}' tiene solo {nuevo_stock} unidades disponibles."
            )
            db.add(alerta_automatica)

    db.commit()
    db.refresh(producto)

    tipo_accion = "adicionadas" if item.cantidad > 0 else "retiradas"

    return {
        "mensaje": f"Inventario actualizado. Unidades {tipo_accion} correctamente.",
        "producto": producto.nombre,
        "nuevo_stock": producto.cantidad
    }


#  HISTORIAL
@router.get("/historial")
def ver_historial_movimientos(db: Session = Depends(get_db)):

    movimientos = db.query(Inventario).all()

    resultado = []
    for m in movimientos:
        resultado.append({
            "id_movimiento": m.id,
            "producto_id": m.producto_id,
            "producto_nombre": m.producto.nombre if m.producto else "Desconocido",
            "cantidad_movida": m.cantidad,
            "fecha": m.fecha_movimiento
        })

    return resultado


# ACTUALIZAR HISTORIAL
@router.put("/actualizar/{movimiento_id}")
def actualizar_movimiento_viejo(movimiento_id: int, item: MovimientoInventario, db: Session = Depends(get_db)):

    movimiento = db.query(Inventario).filter(Inventario.id == movimiento_id).first()

    if not movimiento:
        raise HTTPException(status_code=404, detail="Registro de inventario no encontrado")

    movimiento.producto_id = item.producto_id
    movimiento.cantidad = item.cantidad

    db.commit()

    return {"mensaje": f"Movimiento {movimiento_id} actualizado correctamente en el historial"}


# ELIMINAR
@router.delete("/borrar/{movimiento_id}")
def eliminar_movimiento_historial(movimiento_id: int, db: Session = Depends(get_db)):

    movimiento = db.query(Inventario).filter(Inventario.id == movimiento_id).first()

    if not movimiento:
        raise HTTPException(status_code=404, detail="Registro de inventario no encontrado")

    db.delete(movimiento)
    db.commit()

    return {"mensaje": f"Movimiento {movimiento_id} eliminado del historial"}