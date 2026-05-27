from fastapi import APIRouter
from schemas.user import UsuarioCreate, UsuarioResponse

router = APIRouter()

usuarios = []


@router.post("/usuarios")
def crear_usuario(usuario: UsuarioCreate):
    usuarios.append(usuario)
    return {
        "mensaje": "Usuario creado correctamente",
        "usuario": usuario
    }


@router.get("/usuarios")
def listar_usuarios():
    return usuarios