import random

def test_crear_usuario_en_el_liceo(client):
    """PRUEBA 1: Registrar un usuario con correo único aleatorio"""
    
    # Generamos un número al azar entre 1000 y 99999
    numero_aleatorio = random.randint(1000, 99999)
    
    # Creamos el correo dinámico usando ese número
    correo_dinamico = f"sandra.admin{numero_aleatorio}@liceo.com"
    
    datos_formulario = {
        "nombre": "Sandra Casas",
        "rol": "Administrador",
        "correo": correo_dinamico,  # Ahora nunca se va a repetir
        "contraseña": "claveSegura2026"
    }
    
    respuesta_del_sistema = client.post("/usuarios/", json=datos_formulario)
    
    assert respuesta_del_sistema.status_code in [200, 201]
    
    datos_guardados = respuesta_del_sistema.json()
    assert datos_guardados["nombre"] == "Sandra Casas"
    assert datos_guardados["correo"] == correo_dinamico