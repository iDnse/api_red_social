# "cod_pub"	"integer"		"NO"
# "fec_pub"	"date"		"NO"
# "tit_pub"	"character varying"		"NO"
# "des_pub"	"text"		"YES"
# "fky_ciu"	"integer"		"YES"
# "fky_per"	"integer"		"NO"
# "fky_tip_aco"	"integer"		"NO"
# "fky_tip_pri"	"integer"		"NO"
# "est_pub"	"character"	1	"NO"
from sqlalchemy import Column, Integer
from app.database.database import Base

class Publicacion(Base):
    __tablename__ = "publicacion"
    __table_args__ = {"schema" : "perfil_personal"}

    cod_pub = Column(
        Integer,
        primary_key = True,
        nullable = False,
        unique = True
    )