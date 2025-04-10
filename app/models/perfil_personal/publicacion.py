# "cod_pub"	"integer"		"NO"
# "fec_pub"	"date"		"NO"
# "tit_pub"	"character varying"		"NO"
# "des_pub"	"text"		"YES"
# "fky_ciu"	"integer"		"YES"
# "fky_per"	"integer"		"NO"
# "fky_tip_aco"	"integer"		"NO"
# "fky_tip_pri"	"integer"		"NO"
# "est_pub"	"character"	1	"NO"

# Estatus de la Publicación:
# A: Publicada y Visible
# P: Programada para ser publicada en una fecha determinada
# S: Suspendida por la red social al incumplirse las normas comunitarias 
# E: Eliminado por la persona 
from sqlalchemy import Column, Integer, Date, String, Enum, ForeignKey
from app.database.database import Base
import enum
from app.models.ubicacion.ciudad import Ciudad
from app.models.perfil_personal.persona import Persona
from app.models.general.tipo_acontecimiento import TipoAcontecimiento
from app.models.seguridad.tipo_privacidad import TipoPrivacidad

class Estado(enum.Enum):
    A = 'Publicada y Visible'
    P = 'Programada para ser publicada en una fecha determinada'
    S = 'Suspendida por la red social al incumplirse las normas comunitarias '
    E = 'Eliminado por la persona '

class Publicacion(Base):
    __tablename__ = "publicacion"
    __table_args__ = {"schema" : "perfil_personal"}

    cod_pub = Column(
        Integer,
        primary_key = True,
        nullable = False,
        unique = True
    )

    fec_pub = Column(
        Date,
        nullable = False
    )

    tit_pub = Column(
        String(255),
        nullable = False
    )

    des_pub = Column(
        String(255)
    )

    fky_ciu = Column(
        Integer,
        ForeignKey(Ciudad.cod_ciu),
        nullable = False
    )

    fky_per = Column(
        Integer,
        ForeignKey(Persona.cod_per),
        nullable = False
    )

    fky_tip_aco = Column(
        Integer,
        ForeignKey(TipoAcontecimiento.cod_tip_aco),
        nullable = False
    )
    
    fky_tip_pri = Column(
        Integer,
        ForeignKey(TipoPrivacidad.cod_tip),
        nullable = False
    )

    est_pub = Column(
        Enum(Estado),
        default = Estado.A
    )