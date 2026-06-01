from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)


def crear_producto():
    unique = str(uuid.uuid4())[:8]

    producto_data = {
        "nombre": f"Producto {unique}",
        "categoria": "Papelería",
        "cantidad": 50,
        "precio": 12000,
        "fecha_registro": "2026-05-31"
    }

    response = client.post("/productos/", json=producto_data)
    assert response.status_code in [200, 201], response.text

    body = response.json()
    return body["id"]


def crear_movimiento(producto_id):
    movimiento_data = {
        "producto_id": producto_id,
        "cantidad": 15
    }

    response = client.post("/inventario/mover", json=movimiento_data)
    assert response.status_code in [200, 201], response.text

    return response.json()


def obtener_movimiento(producto_id):
    response = client.get("/inventario/historial")
    assert response.status_code == 200, response.text

    movimientos = response.json()
    for movimiento in movimientos:
        if movimiento["producto_id"] == producto_id:
            return movimiento

    return None


def test_create_movimiento_inventario():
    producto_id = crear_producto()
    respuesta = crear_movimiento(producto_id)

    assert "mensaje" in respuesta
    assert "producto" in respuesta
    assert "nuevo_stock" in respuesta
    assert respuesta["nuevo_stock"] == 65


def test_get_historial_inventario():
    producto_id = crear_producto()
    crear_movimiento(producto_id)

    response = client.get("/inventario/historial")
    assert response.status_code == 200, response.text

    historial = response.json()
    assert isinstance(historial, list)
    assert len(historial) > 0


def test_update_movimiento_inventario():
    producto_id = crear_producto()
    crear_movimiento(producto_id)

    movimiento = obtener_movimiento(producto_id)
    assert movimiento is not None

    movimiento_id = movimiento["id_movimiento"]

    data_actualizada = {
        "producto_id": producto_id,
        "cantidad": 25
    }

    response = client.put(f"/inventario/actualizar/{movimiento_id}", json=data_actualizada)
    assert response.status_code == 200, response.text
    assert "actualizado correctamente" in response.json()["mensaje"]

# """
# def test_delete_movimiento_inventario():
#     producto_id = crear_producto()
#     crear_movimiento(producto_id)

#     movimiento = obtener_movimiento(producto_id)
#     assert movimiento is not None

#     movimiento_id = movimiento["id_movimiento"]

#     response = client.delete(f"/inventario/borrar/{movimiento_id}")
#     assert response.status_code == 200, response.text
#     assert "eliminado del historial" in response.json()["mensaje"]
# """