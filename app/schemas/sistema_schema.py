from pydantic import BaseModel
from typing import List, Optional

# Esquema para actualizar la configuración del sistema (PUT)
class SistemaUpdate(BaseModel):
    nombre_sistema: str
    modo_mantenimiento: bool

# El esquema de respuesta que muestra el "Panel de Control" que pide tu diagrama
class PanelControlResponse(BaseModel):
    nombre_sistema: str
    modo_mantenimiento: bool
    total_productos_en_inventario: int
    total_usuarios_registrados: int
    total_alertas_activas: int
    total_reportes_generados: int

    class Config:
        from_attributes = True
        