# "cod_tico"	"integer"	
# "nom_tico"	"character varying"	50
# "est_tico"	"character"	1

from sqlalchemy import Column, Integer, String, Enum
from app.database.database import Base
import enum

class Estado(enum.Enum):
    A = "Activo"
    I = "Inactivo"

class TipoContacto(Base):
    __tablename__ = "tipo_contacto"
    __table_args__ = {"schema":"general"}

    cod_tico = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    nom_tico = Column(
        String(50),
        nullable=False,
        unique=True
    )

    est_tico = Column(
        Enum(Estado),
        nullable=False,
        default=Estado.A
    )