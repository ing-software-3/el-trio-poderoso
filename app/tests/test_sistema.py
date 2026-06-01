from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# CREAR / INICIALIZAR

def inicializar_sistema():

    response = client.post("/sistema/inicializar")

    body = response.json()

    return body


def test_create_sistema():

    sistema = inicializar_sistema()

    assert sistema is not None
    assert "id" in sistema


# GET PANEL DE CONTROL

def test_get_panel_control():

    inicializar_sistema()

    response = client.get("/sistema/panel-control")

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200


# UPDATE CONFIGURACIÓN

def test_update_sistema():

    inicializar_sistema()

    data = {
        "nombre_sistema": "Sistema Actualizado",
        "modo_mantenimiento": True
    }

    response = client.put(
        "/sistema/configuracion",
        json=data
    )

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200


# DELETE / REINICIAR

# def test_delete_sistema():

#     inicializar_sistema()

#     response = client.delete("/sistema/reiniciar")

#     print(response.status_code)
#     print(response.json())

#     assert response.status_code == 200