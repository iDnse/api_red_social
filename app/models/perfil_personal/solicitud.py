# "cod_sol"	"integer"		"NO"
# "fk1_per"	"integer"		"NO"
# "fk2_per"	"integer"		"NO"
# "act_sol"	"date"		"NO"
# "est_sol"	"character"	1	"NO"

# "fk1_per"	"integer"	"perfil_personal.persona.cod_per"
# "fk2_per"	"integer"	"perfil_personal.persona.cod_per"

# Estatus de la Solicitud:
# A: Aceptado
# P: Petición
# R: Rechazado

from sqlalchemy import Column, Integer, Date, Enum, ForeignKey
from app.database.database import Base
import enum
from app.models.perfil_personal.persona import Persona

class Estado(enum.Enum):
    A="Aceptado"
    P="Petición"
    R="Rechazado"

class Solicitud(Base):
    __tablename__ = "solicitud"
    __table_args__ = {"schema":"perfil_personal"}

    cod_sol = Column(
        Integer,
        primary_key=True,
        index=True,
        nullable=False,
        unique=True
    )

    fk1_per = Column(
        Integer,
        ForeignKey(Persona.cod_per),
        nullable=False
    )

    fk2_per = Column(
        Integer,
        ForeignKey(Persona.cod_per),
        nullable=False
    )

    act_sol = Column(
        Date,
        nullable=False
    )

    est_sol = Column(
        Enum(Estado),
        default=Estado.A
    )