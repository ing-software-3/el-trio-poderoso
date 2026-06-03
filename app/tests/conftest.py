# import pytest
# from fastapi.testclient import TestClient

# from app.main import app
# from app.db.database import Base, engine, SessionLocal
# from app.models.producto import Producto
# from app.models.usuarios import Usuario
# from app.models.alertas import Alerta
# from app.models.reportes import Reporte
# from app.models.inventarios import Inventario
# from app.models.sistemas import Sistema

# 1. AQUÍ SÍ DECLARAMOS LA BASE DE DATOS DE PRUEBAS EXCLUSIVA
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/prueba_test"

# 2. Creamos un motor y una sesión exclusivos para los tests
engine_test = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

# @pytest.fixture(scope="session", autouse=True)
# def create_tables():
#     Base.metadata.create_all(bind=engine)
#     yield
#     #Base.metadata.drop_all(bind=engine)

>>>>>>> b6584d0da97cea8d3b0f205baa315b7bb0fc5317

# @pytest.fixture(autouse=True)
# def clean_database():
#     db = SessionLocal()
#     try:
#         # borrar primero tablas que dependen de producto
#         db.query(Inventario).delete()
#         db.query(Alerta).delete()
#         db.query(Reporte).delete()
#         db.query(Usuario).delete()
#         db.query(Producto).delete()
#         db.query(Sistema).delete()
#         db.commit()
#         yield
#     finally:
#         db.close()


# @pytest.fixture
# def client():
#     return TestClient(app)