def test_crud_alertas_completo(client):
    response_producto = client.post("/productos/", json={
        "nombre": "Lápiz",
        "descripcion": "Lápiz de prueba",
        "cantidad": 20,
        "categoria": "Útiles escolares",
        "precio": 1000
    })
    assert response_producto.status_code in [200, 201], response_producto.text

    producto_id = response_producto.json()["id"]

    response_alerta = client.post("/alertas/", json={
        "producto_id": producto_id,
        "mensaje": "Alerta: quedan pocos lápices"
    })
    assert response_alerta.status_code in [200, 201], response_alerta.text