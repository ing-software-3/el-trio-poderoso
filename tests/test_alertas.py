import pytest
import random

def test_crud_alertas_completo(client):
    """Prueba el ciclo completo (CRUD) de las alertas de stock crítico"""
    
    # ------------------------------------------------------------------------
    # 1. POST: Crear una nueva alerta de prueba
    # ------------------------------------------------------------------------
    id_producto_falso = random.randint(501, 999)
    datos_alerta = {
        "producto_id": id_producto_falso,
        "mensaje": "Alerta: Quedan menos de 5 cajas de colores en bodega",
        "estado": "ACTIVA"
    }
    
    response_post = client.post("/alertas/", json=datos_alerta)
    assert response_post.status_code in [200, 201]
    
    alerta_guardada = response_post.json()
    alerta_id = alerta_guardada["id"]
    assert alerta_guardada["estado"] == "ACTIVA"

    # ------------------------------------------------------------------------
    # 2. GET ALL: Ver el listado de alertas de la administración
    # ------------------------------------------------------------------------
    response_get_all = client.get("/alertas/")
    assert response_get_all.status_code == 200
    assert len(response_get_all.json()) > 0

    # ------------------------------------------------------------------------
    # 3. GET BY ID: Consultar la alerta por su ID
    # ------------------------------------------------------------------------
    response_get_id = client.get(f"/alertas/{alerta_id}")
    assert response_get_id.status_code == 200
    assert response_get_id.json()["id"] == alerta_id

    # ------------------------------------------------------------------------
    # 4. PUT: Cambiar el estado de la alerta (ej: pasar de ACTIVA a RESUELTA)
    # ------------------------------------------------------------------------
    datos_actualizados = {
        "producto_id": id_producto_falso,
        "mensaje": "Alerta: Stock de colores reabastecido",
        "estado": "RESUELTA"  # Ya las compraron, se resuelve la alerta
    }
    response_put = client.put(f"/alertas/{alerta_id}", json=datos_actualizados)
    assert response_put.status_code == 200
    assert response_put.json()["estado"] == "RESUELTA"

    # ------------------------------------------------------------------------
    # 5. DELETE: Eliminar una alerta vieja de la base de datos
    # ------------------------------------------------------------------------
    response_delete = client.delete(f"/alertas/{alerta_id}")
    assert response_delete.status_code == 200
    
    # Comprobar que fue eliminada
    response_verificar = client.get(f"/alertas/{alerta_id}")
    assert "error" in response_verificar.json() or response_verificar.status_code == 404