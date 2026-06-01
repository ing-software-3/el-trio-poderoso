import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.database import Base, get_db  # Traemos get_db para sobreescribirlo
from app.models.producto import Producto
from app.models.usuarios import Usuario
from app.models.alertas import Alerta
from app.models.reportes import Reporte
from app.models.inventarios import Inventario
from app.models.sistemas import Sistema

# 1. AQUÍ SÍ DECLARAMOS LA BASE DE DATOS DE PRUEBAS EXCLUSIVA
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/prueba_test"

# 2. Creamos un motor y una sesión exclusivos para los tests
engine_test = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

@pytest.fixture(scope="session", autouse=True)
def create_tables():
    """Crea las tablas en prueba_test y las borra SOLO al final de todas las pruebas"""
    Base.metadata.create_all(bind=engine_test)
    yield
    Base.metadata.drop_all(bind=engine_test) # Si quieres verlas en XAMPP, ponle un # al principio de esta línea

@pytest.fixture(autouse=True)
def clean_database():
    """Limpia los datos de prueba_test entre cada test para que no se dupliquen"""
    db = TestingSessionLocal()
    try:
        db.query(Inventario).delete()
        db.query(Alerta).delete()
        db.query(Reporte).delete()
        db.query(Usuario).delete()
        db.query(Producto).delete()
        db.query(Sistema).delete()
        db.commit()
        yield
    finally:
        db.close()

@pytest.fixture
def client():
    """Sobreescribe la base de datos de la app para que FastAPI use prueba_test en los tests"""
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
            
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)