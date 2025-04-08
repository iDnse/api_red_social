# "cod_tip_aco"	"integer"		"NO"
# "nom_tip_aco"	"character varying"	50	"NO"
# "fky_cat_aco"	"integer"		"NO"
# "est_tip_aco"	"character"	1	"NO"

from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from app.database.database import Base
import enum

class Estado(enum.Enum):
    A = "Activo"
    I = "Inactivo"

class TipoAcontecimiento(Base):
    __tablename__ = "tipo_acontecimiento"
    __table_args__ = {"schema":"general"}

    cod_tip_aco = Column(
        Integer,
        primary_key = True,
        index = True
    )

    nom_tip_aco = Column(
        String,
        nullable = False,
        unique = True,
    )

    fky_cat_aco = Column(
        Integer,
        ForeignKey("general.categoria_acontecimiento.cod_cat_aco"),
        nullable = False
    )

    est_tip_aco = Column(
        Enum(Estado),
        nullable=False,
        default=Estado.A
    )
