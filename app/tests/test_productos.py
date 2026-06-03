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


def test_buscar_productos():
    unique_name = f"BuscarMe_{uuid.uuid4().hex[:6]}"
    producto_data = {
        "nombre": unique_name,
        "categoria": "Didácticos Especiales",
        "cantidad": 10,
        "precio": 5000,
        "fecha_registro": "2026-05-31"
    }
    client.post("/productos/", json=producto_data)

    # Buscamos por nombre
    response = client.get("/productos/", params={"nombre": unique_name})
    assert response.status_code == 200
    res_json = response.json()
    assert len(res_json) == 1
    assert res_json[0]["nombre"] == unique_name

    # Buscamos por categoría
    response_cat = client.get("/productos/", params={"categoria": "Didácticos Especiales"})
    assert response_cat.status_code == 200
    assert len(response_cat.json()) >= 1