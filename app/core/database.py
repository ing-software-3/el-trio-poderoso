
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Conexión a MySQL (XAMPP)
DATABASE_URL = "mysql+pymysql://root:@localhost/eltriopoderoso"

# Crear conexión
engine = create_engine(DATABASE_URL)

# Crear sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()
