from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)


def crear_reporte():

    unique = str(uuid.uuid4())[:8]

    reporte_data = {
        "descripcion": f"Reporte de inventario {unique}",
        "tipo": "Inventario"
    }

    reporte_response = client.post("/reportes/guardar", json=reporte_data)
    assert reporte_response.status_code in [200, 201], reporte_response.text

    reporte_body = reporte_response.json()
    id_reporte = reporte_body["id"]

    return id_reporte


# CREAR
def test_create_reporte():

    id_reporte = crear_reporte()

    assert id_reporte is not None


# HISTORIAL
def test_get_historial_reportes():

    crear_reporte()

    response = client.get("/reportes/historial")

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200


# INVERSIÓN TOTAL
def test_get_inversion_total():

    response = client.get("/reportes/inversion-total")

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200


# STOCK BAJO
def test_get_stock_bajo():

    response = client.get("/reportes/stock-bajo")

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200


# # DELETE
# def test_delete_reporte():

#     id_reporte = crear_reporte()

#     response = client.delete(f"/reportes/borrar/{id_reporte}")

#     print(response.status_code)
#     print(response.json())

#     assert response.status_code == 200