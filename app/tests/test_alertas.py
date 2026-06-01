from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)


def crear_producto():
    unique = str(uuid.uuid4())[:8]

    producto_data = {
        "nombre": f"Producto {unique}",
        "categoria": "Papelería",
        "cantidad": 20,
        "precio": 1500,
        "fecha_registro": "2026-05-31"
    }

    producto_response = client.post("/productos/", json=producto_data)
    assert producto_response.status_code in [200, 201], producto_response.text

    producto_body = producto_response.json()
    return producto_body["id"]


def crear_alerta():
    id_producto = crear_producto()

    alerta_data = {
        "producto_id": id_producto,
        "mensaje": "Quedan menos de 5 unidades en inventario"
    }

    alerta_response = client.post("/alertas/", json=alerta_data)
    assert alerta_response.status_code in [200, 201], alerta_response.text

    alerta_body = alerta_response.json()
    return alerta_body["id"]


def buscar_alerta_en_lista(id_alerta):
    response = client.get("/alertas/")
    assert response.status_code == 200, response.text

    alertas = response.json()
    for alerta in alertas:
        if alerta["id"] == id_alerta:
            return alerta

    return None


# CREAR
def test_create_alerta():
    id_alerta = crear_alerta()
    assert id_alerta is not None


# GET / LISTAR
def test_get_alerta_list():
    id_alerta = crear_alerta()

    alerta_en_lista = buscar_alerta_en_lista(id_alerta)
    assert alerta_en_lista is not None
    assert alerta_en_lista["id"] == id_alerta


# UPDATE
def test_update_alerta():
    id_alerta = crear_alerta()
    id_producto = crear_producto()

    data = {
        "producto_id": id_producto,
        "mensaje": "Alerta actualizada: revisar stock"
    }

    response = client.put(f"/alertas/{id_alerta}", json=data)

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200
    assert response.json()["mensaje"] == "Alerta actualizada: revisar stock"


# # DELETE
# def test_delete_alerta():
#     id_alerta = crear_alerta()

#     response = client.delete(f"/alertas/{id_alerta}")

#     print(response.status_code)
#     print(response.json())

#     assert response.status_code == 200
#     assert "eliminada correctamente" in response.json()["mensaje"]