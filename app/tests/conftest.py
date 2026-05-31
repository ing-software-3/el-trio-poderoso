import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.db.database import Base, engine, SessionLocal
from app.models.producto import Producto
from app.models.usuarios import Usuario
from app.models.alertas import Alerta
from app.models.reportes import Reporte
from app.models.inventarios import Inventario
from app.models.sistemas import Sistema


@pytest.fixture(scope="session", autouse=True)
def create_tables():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(autouse=True)
def clean_database():
    db = SessionLocal()
    try:
        # borrar primero tablas que dependen de producto
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
    return TestClient(app)