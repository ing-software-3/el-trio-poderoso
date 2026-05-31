import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.database import Base, get_db

# Configuración de tu base de datos secundaria de pruebas en XAMPP
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/prueba_test"

# Creamos el motor de conexión para MySQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Crea las tablas en 'prueba_test' automáticamente antes de empezar"""
    Base.metadata.create_all(bind=engine)
    yield
    # Al terminar todas las pruebas, limpia la base de datos
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session():
    """Genera una sesión limpia y aislada para cada prueba independiente"""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def client(db_session):
    """Intercepta FastAPI para que use la base de datos de pruebas"""
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()