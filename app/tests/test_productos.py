import random

def test_crud_productos_completo(client):
    """Prueba el ciclo completo (CRUD) de la gestión de productos del Liceo"""

    numero_falso = random.randint(1000, 9999)
    datos_producto = {
        "nombre": f"Plastilina Escolar Extragrande {numero_falso}",
        "categoria": "Didácticos",
        "cantidad": 12,
        "precio": 4500,
        "fecha_registro": "2026-05-31"
    }

    response_post = client.post("/productos/", json=datos_producto)
    assert response_post.status_code in [200, 201], response_post.text

    producto_guardado = response_post.json()
    producto_id = producto_guardado["id"]
    assert producto_guardado["nombre"] == datos_producto["nombre"]

    response_get_all = client.get("/productos/")
    assert response_get_all.status_code == 200
    assert len(response_get_all.json()) > 0

    response_get_id = client.get(f"/productos/{producto_id}")
    assert response_get_id.status_code == 200
    assert response_get_id.json()["id"] == producto_id

    datos_actualizados = {
        "nombre": f"Plastilina Escolar Extragrande {numero_falso}",
        "categoria": "Didácticos",
        "cantidad": 8,
        "precio": 4800,
        "fecha_registro": "2026-05-31"
    }

    response_put = client.put(f"/productos/{producto_id}", json=datos_actualizados)
    assert response_put.status_code == 200
    assert response_put.json()["cantidad"] == 8
    assert response_put.json()["precio"] == 4800

    response_delete = client.delete(f"/productos/{producto_id}")
    assert response_delete.status_code == 200
    assert "eliminado correctamente" in response_delete.json()["mensaje"]

    response_404 = client.get(f"/productos/{producto_id}")
    assert response_404.status_code == 404
    assert response_404.json()["detail"] == "Producto no encontrado"