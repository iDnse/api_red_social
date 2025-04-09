# "cod_con"	"integer"		"NO"
# "des_con"	"character varying"	100	"NO"
# "act_con"	"date"		"NO"
# "fky_per"	"integer"		"NO"
# "fky_tip_co"	"integer"		"NO"
# "fky_tip_pri"	"integer"		"NO"
# "est_con"	"character"	1	"NO"
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from app.database.database import Base
import enum
from app.models.perfil_personal.persona import Persona
from app.models.general.tipo_contacto import TipoContacto
from app.models.seguridad.tipo_privacidad import TipoPrivacidad


class Estado (enum.Enum):
    A = "Activo"
    I = "Inactivo"

class Contacto(Base):
    __tablename__ = "contacto"
    __table_args__ = {"schema":"perfil_personal"}

    cod_con = Column(
        Integer,
        primary_key = True,
        index = True,
        nullable = False,
        unique = True
    )

    des_con = Column(
        String(100),
        nullable = True,
        unique = True
    )

    act_con = Column(
        Date,
        nullable = False
    )

    fky_per = Column(
        Integer,
        ForeignKey(Persona.cod_per),
        nullable = False
    )

    fky_tip_co = Column(
        Integer,
        ForeignKey(TipoContacto.cod_tico),
        nullable = False
    )

    fky_tip_pri = Column(
        Integer,
        ForeignKey(TipoPrivacidad.cod_tip),
        nullable = False
    )

    est_con = Column(
        Enum(Estado),
        default = Estado.A
    )