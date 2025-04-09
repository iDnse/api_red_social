from sqlalchemy import Column, Integer
from app.database.database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    __table_args__ = {"schema":"seguridad"}

    cod_usu = Column(
        Integer,
        primary_key = True,
        nullable = False,
        unique = True
    )