# "cod_tip"	"integer"		"NO"
# "nom_tip"	"character varying"	25	"NO"
# "est_tip"	"character"	1	"NO"
from sqlalchemy import Column, Integer
from app.database.database import Base

class TipoPrivacidad(Base):
    __tablename__ = "tipo_privacidad"
    __table_args__ = {"schema" : "seguridad"}

    cod_tip = Column(
        Integer,
        index = True,
        primary_key = True,
        nullable = False,
        unique = True
    )