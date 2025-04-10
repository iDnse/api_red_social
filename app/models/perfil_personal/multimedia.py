# "cod_mul"	"integer"		"NO"
# "url_mul"	"character varying"	255	"NO"
# "fky_pub"	"integer"		"NO"
# "est_mul"	"character"	1	"NO"
# P: Publicado Correctamente
# X: Suspendida la imagen o video por infringir normas comunitarias
# R: Restringida para pùblico sensible
# S: Publicaciòn de temas polìticos o sociales.

from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from app.database.database import Base
import enum
from app.models.perfil_personal.publicacion import Publicacion

class Estado(enum.Enum):
    P = "Publicado"
    X = "Suspendida"
    R = "Restringida"
    S = "Suspendido Otros"

class Multimedia(Base):
    __tablename__ = "multimedia"
    __table_args__ = {"schema" : "perfil_personal"}

    cod_mul = Column(
        Integer,
        primary_key = True,
        index = True,
        nullable = False,
        unique = True
    )

    url_mul = Column(
        String(255),
        nullable = False
    )

    fky_pub = Column(
        Integer,
        ForeignKey(Publicacion.cod_pub),
        nullable = False
    )

    est_mul = Column(
        Enum(Estado),
        default = Estado.P
    )