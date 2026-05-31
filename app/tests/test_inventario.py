def test_crud_inventario_completo(client):
    response_producto = client.post("/productos/", json={
        "nombre": "Resma",
        "descripcion": "Resma de papel",
        "cantidad": 50,
        "categoria": "Papelería",
        "precio": 12000
    })
    assert response_producto.status_code in [200, 201], response_producto.text

    producto_id = response_producto.json()["id"]

    response_movimiento = client.post("/inventario/mover", json={
        "producto_id": producto_id,
        "cantidad": 15
    })
    assert response_movimiento.status_code in [200, 201], response_movimiento.text