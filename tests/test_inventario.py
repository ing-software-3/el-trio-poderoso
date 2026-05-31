import pytest
import random

def test_crud_inventario_completo(client):
    """Prueba el ciclo completo (CRUD) de un movimiento de inventario"""
    
    # ------------------------------------------------------------------------
    # 1. POST: Registrar un movimiento en el inventario
    # ------------------------------------------------------------------------
    id_producto_falso = random.randint(1, 500) # Evitamos IDs repetidos
    datos_movimiento = {
        "producto_id": id_producto_falso,
        "cantidad": 15,
        "tipo_movimiento": "ENTRADA",  # Ej: Llegaron resmas de papel al Liceo
        "motivo": "Compra de material de oficina mensual"
    }
    
    response_post = client.post("/inventario/", json=datos_movimiento)
    assert response_post.status_code in [200, 201]
    
    movimiento_guardado = response_post.json()
    movimiento_id = movimiento_guardado["id"] # Guardamos el ID para las siguientes pruebas
    assert movimiento_guardado["cantidad"] == 15
    assert movimiento_guardado["tipo_movimiento"] == "ENTRADA"

    # ------------------------------------------------------------------------
    # 2. GET ALL: Listar todos los movimientos
    # ------------------------------------------------------------------------
    response_get_all = client.get("/inventario/")
    assert response_get_all.status_code == 200
    assert len(response_get_all.json()) > 0

    # ------------------------------------------------------------------------
    # 3. GET BY ID: Obtener este movimiento específico
    # ------------------------------------------------------------------------
    response_get_id = client.get(f"/inventario/{movimiento_id}")
    assert response_get_id.status_code == 200
    assert response_get_id.json()["id"] == movimiento_id

    # ------------------------------------------------------------------------
    # 4. PUT: Actualizar el motivo o la cantidad del movimiento
    # ------------------------------------------------------------------------
    datos_actualizados = {
        "producto_id": id_producto_falso,
        "cantidad": 20,  # Corregimos de 15 a 20 resmas
        "tipo_movimiento": "ENTRADA",
        "motivo": "Compra corregida por auditoría del Liceo"
    }
    response_put = client.put(f"/inventario/{movimiento_id}", json=datos_actualizados)
    assert response_put.status_code == 200
    assert response_put.json()["cantidad"] == 20
    assert response_put.json()["motivo"] == "Compra corregida por auditoría del Liceo"

    # ------------------------------------------------------------------------
    # 5. DELETE: Borrar el registro del movimiento
    # ------------------------------------------------------------------------
    response_delete = client.delete(f"/inventario/{movimiento_id}")
    assert response_delete.status_code == 200
    
    # Verificar que ya no exista si lo intentamos buscar
    response_verificar = client.get(f"/inventario/{movimiento_id}")
    # Si tus rutas devuelven un JSON de error en vez de 404, validamos el texto:
    assert "error" in response_verificar.json() or response_verificar.status_code == 404