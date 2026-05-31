from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db  #  IMPORT CORRECTO
from app.models.producto import Producto
from app.models.alertas import Alerta
from app.schemas.alertas_schema import AlertaCreate, AlertaResponse

router = APIRouter(
    prefix="/alertas",
    tags=["Alertas"]
)

@router.post("/", response_model=AlertaResponse, status_code=status.HTTP_201_CREATED)
def crear_alerta(alerta: AlertaCreate, db: Session = Depends(get_db)):
    
    # Validar que el producto exista
    producto_existe = db.query(Producto).filter(Producto.id == alerta.producto_id).first()
    
    if not producto_existe:
        raise HTTPException(status_code=404, detail="El producto para esta alerta no existe")

    nueva_alerta = Alerta(
        producto_id=alerta.producto_id,
        mensaje=alerta.mensaje
    )
    
    db.add(nueva_alerta)
    db.commit()
    db.refresh(nueva_alerta)

    return nueva_alerta

@router.get("/", response_model=List[AlertaResponse])
def listar_alertas(db: Session = Depends(get_db)):
    return db.query(Alerta).all()


@router.put("/{alerta_id}", response_model=AlertaResponse)
def actualizar_alerta(alerta_id: int, alerta_actualizada: AlertaCreate, db: Session = Depends(get_db)):

    alerta = db.query(Alerta).filter(Alerta.id == alerta_id).first()

    if not alerta:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")

    # Validar que el producto exista
    producto_existe = db.query(Producto).filter(Producto.id == alerta_actualizada.producto_id).first()

    if not producto_existe:
        raise HTTPException(status_code=404, detail="El producto especificado no existe")

    alerta.producto_id = alerta_actualizada.producto_id
    alerta.mensaje = alerta_actualizada.mensaje

    db.commit()
    db.refresh(alerta)

    return alerta

@router.delete("/{alerta_id}")
def eliminar_alerta(alerta_id: int, db: Session = Depends(get_db)):

    alerta = db.query(Alerta).filter(Alerta.id == alerta_id).first()

    if not alerta:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")

    db.delete(alerta)
    db.commit()

    return {"mensaje": f"Alerta {alerta_id} eliminada correctamente"}