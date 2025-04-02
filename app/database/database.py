# motor para conexion de db
from sqlalchemy import create_engine 
# clase base del modelo
from sqlalchemy.ext.declarative import declarative_base
# fabrica sesiones para interactura con la db
from sqlalchemy.orm import sessionmaker

# seguridad de credenciales a variables de entorno
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

#creacion de motor
engine = create_engine(DATABASE_URL,
                       #sessiones abiertas
                       pool_size=10,
                       #maximo cuando la sesion esta llena
                       max_overflow=2,
                       #verifica que la conexion este activa
                       pool_pre_ping=True,
                       #muestra el resultado sql en consola
                       echo=True
)

SessionLocal = sessionmaker(
    # requiere un commit manual para que guarde la sesion
    autocommit = False,
    # control manual de la sincronizacion con la db
    autoflush = False,
    #As
    bind = engine
)

# base de los modelos
Base = declarative_base()

# funcion de entrada
def get_db():
    db = SessionLocal()
    try:
        #devuelve db si esta todo ok
        yield db
    finally:
        # tanto como que falle o que est ok, se cierra db
        db.close()
