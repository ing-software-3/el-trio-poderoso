from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)


def crear_usuario():

    unique = str(uuid.uuid4())[:8]

    usuario_data = {
        "nombre": f"Usuario {unique}",
        "rol": "docente",
        "correo": f"usuario{unique}@test.com",
        "contraseña": "123456"
    }

    usuario_response = client.post("/usuarios", json=usuario_data)
    assert usuario_response.status_code in [200, 201], usuario_response.text

    usuario_body = usuario_response.json()

    # Si tu API responde con "idUsuario", cambia esta línea por:
    # id_usuario = usuario_body["idUsuario"]
    id_usuario = usuario_body["id"]

    return id_usuario


# CREAR
def test_create_usuario():

    id_usuario = crear_usuario()

    assert id_usuario is not None


# GET ID
def test_get_usuario_by_id():

    id_usuario = crear_usuario()

    response = client.get(f"/usuarios/{id_usuario}")

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200


# UPDATE
def test_update_usuario():

    id_usuario = crear_usuario()

    data = {
        "nombre": "Usuario Actualizado",
        "rol": "coordinador",
        "correo": f"actualizado{uuid.uuid4().hex[:8]}@test.com",
        "contraseña": "654321"
    }

    response = client.put(
        f"/usuarios/{id_usuario}",
        json=data
    )

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200


# DELETE
# def test_delete_usuario():

#     id_usuario = crear_usuario()

#     response = client.delete(f"/usuarios/{id_usuario}")

#     print(response.status_code)

#     assert response.status_code in [200, 204]