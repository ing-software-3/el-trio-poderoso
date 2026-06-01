from fastapi.testclient import TestClient
from app.main import app
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

    id_producto = producto_body["id"]

    return id_producto


# CREAR

def test_create_producto():

    id_producto = crear_producto()

    assert id_producto is not None


# GET ID

def test_get_producto_by_id():

    id_producto = crear_producto()

    response = client.get(f"/productos/{id_producto}")

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200


# UPDATE

def test_update_producto():

    id_producto = crear_producto()

    data = {
        "nombre": "Producto Actualizado",
        "categoria": "Didácticos",
        "cantidad": 50,
        "precio": 2500,
        "fecha_registro": "2026-05-31"
    }

    response = client.put(
        f"/productos/{id_producto}",
        json=data
    )

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200


# # DELETE

# def test_delete_producto():

#     id_producto = crear_producto()

#     response = client.delete(f"/productos/{id_producto}")

#     print(response.status_code)
#     print(response.json())

#     assert response.status_code == 200