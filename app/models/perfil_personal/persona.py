# "cod_per"	"integer"		"NO"
# "nm1_per"	"character varying"	25	"NO"
# "nm2_per"	"character varying"	25	"YES"
# "ap1_per"	"character varying"	25	"NO"
# "ap2_per"	"character varying"		"YES"
# "nac_per"	"date"		"NO"
# "sex_per"	"character"	1	"NO"
# "per_per"	"character varying"	255	"NO"
# "por_per"	"character varying"	255	"NO"
# "fky_usu"	"integer"		"NO"
# "est_per"	"character"	1	"NO"
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from app.database.database import Base
import enum
from app.models.seguridad.usuario import Usuario

class Sexo(enum.Enum):
    F = "Femenino"
    M = "Masculino"
    O = "Otros"

class Estado(enum.Enum):
    A = "Activo"
    I = "Inactivo"

class Persona(Base):
    __tablename__ = "persona"
    __table_args__ = {"schema":"perfil_personal"}

    cod_per = Column(
        Integer,
        primary_key = True,
        index = True,
        nullable = False
    )
    nm1_per = Column(
        String(25),
        nullable = False
    )
    nm2_per = Column(
        String(25),
        nullable = True
    )
    ap1_per = Column(
        String(25),
        nullable = False
    )
    ap2_per = Column(
        String(25),
        nullable = True
    )
    nac_per = Column(
        Date,
        nullable = False
    )
    sex_per = Column(
        Enum(Sexo),
        nullable = False
    )
    per_per = Column(
        String(255),
        nullable = True
    )
    por_per = Column(
        String(255),
        nullable = True
    )
    fky_usu = Column(
        Integer,
        ForeignKey(Usuario.cod_usu),
        nullable = False
    )
    est_per = Column(
        Enum(Estado),
        default = Estado.A
    )