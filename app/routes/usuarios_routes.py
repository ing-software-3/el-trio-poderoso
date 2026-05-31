from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.usuarios import Usuario
from app.schemas.usuarios_schema import UsuarioCreate
from app.db.database import get_db  

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/")
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()


@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return {"error": "Usuario no encontrado"}
    return usuario


@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, datos: UsuarioCreate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    
    if not usuario:
        return {"error": "Usuario no encontrado"}
    
    usuario.nombre = datos.nombre
    usuario.rol = datos.rol
    usuario.correo = datos.correo
    usuario.contraseña = datos.contraseña

    db.commit()
    db.refresh(usuario)
    return usuario



@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    
    if not usuario:
        return {"error": "Usuario no encontrado"}
    
    db.delete(usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado correctamente"}
