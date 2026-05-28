from pydantic import BaseModel

# 📦 Lo que el usuario va a digitar en Swagger para mover el inventario
class MovimientoInventario(BaseModel):
    producto_id: int
    cantidad: int  # 🔍 Usamos cantidad para que combine con la base de datos

# 📋 Lo que el sistema le va a responder en la pantalla de Swagger al terminar
class RespuestaInventario(BaseModel):
    mensaje: str
    producto: str
    nuevo_stock: int

    class Config:
        from_attributes = True  # ✅ Esto es para Pydantic V2, el "orm_mode" moderno