# "cod_ciu"	"integer"		"NO"
# "nom_ciu"	"character varying"	50	"NO"
# "des_ciu"	"character varying"	255	"NO"
# "fky_est"	"integer"		"NO"
# "fky_zon"	"integer"		"NO"
# "est_ciu"	"character"	1	"NO"
# Estatus: A: Activo I: Inactivo

from sqlalchemy import Column, Integer
from app.database.database import Base


class Ciudad(Base):
    __tablename__="ciudad"
    __table_args__={"schema":"ubicacion"}

    cod_ciu = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True
    )