import random

def test_modulo_reportes_completo(client):
    """Prueba las consultas de inversión, stock bajo y el CRUD de reportes guardados"""

    numero_falso = random.randint(1000, 9999)
    producto_critico = {
        "nombre": f"Marcadores Borrables {numero_falso}",
        "categoria": "Oficina",
        "cantidad": 3,
        "precio": 3500,
        "fecha_registro": "2026-05-31"
    }

    response_producto = client.post("/productos/", json=producto_critico)
    assert response_producto.status_code in [200, 201], response_producto.text

    response_inversion = client.get("/reportes/inversion-total")
    assert response_inversion.status_code == 200
    datos_inversion = response_inversion.json()
    assert "valor_total" in datos_inversion
    assert datos_inversion["valor_total"] >= 10500

    response_stock = client.get("/reportes/stock-bajo")
    assert response_stock.status_code == 200
    datos_stock = response_stock.json()
    assert datos_stock["cantidad_criticos"] >= 1
    assert len(datos_stock["productos"]) > 0

    datos_reporte = {
        "descripcion": "Reporte mensual de inventarios críticos para Rectoría",
        "tipo": "Inventario"
    }
    response_post = client.post("/reportes/guardar", json=datos_reporte)
    assert response_post.status_code == 200, response_post.text

    reporte_guardado = response_post.json()
    reporte_id = reporte_guardado["id"]
    assert reporte_guardado["tipo"] == "Inventario"

    response_historial = client.get("/reportes/historial")
    assert response_historial.status_code == 200
    assert len(response_historial.json()) > 0

    response_delete = client.delete(f"/reportes/borrar/{reporte_id}")
    assert response_delete.status_code == 200
    assert "eliminado correctamente" in response_delete.json()["mensaje"]

    response_delete_404 = client.delete(f"/reportes/borrar/{reporte_id}")
    assert response_delete_404.status_code == 404