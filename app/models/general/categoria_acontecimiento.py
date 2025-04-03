# "cod_cat_aco"	"integer"	"NO"		32
# "nom_cat_aco"	"character varying"	"NO"	75	
# "est_cat_aco"	"character"	"NO"	1	

from sqlalchemy import Column, Integer, String, Enum
from app.database.database import Base
import enum

class Estado(enum.Enum):
    A = "Activo"
    I = "Inactivo"

class CategoriaAcontecimiento(Base):
    __tablename__ = "categoria_acontecimiento"
    __table_args__ = {'schema': 'general'}

    cod_cat_aco = Column(
        Integer,
        primary_key=True,
        index=True,
        unique= True,
        nullable=True
    )

    nom_cat_aco = Column(
        String(75),
        index=True,
        unique=True,
        nullable=False
    )

    est_cat_aco = Column(
        Enum(Estado),
        nullable=False,
        default=Estado.A
    )