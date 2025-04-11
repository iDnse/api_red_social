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

from pydantic import BaseModel
from datetime import date

class SolicitudBase(BaseModel):
    fk1_per : int
    fk2_per : int
    act_sol : date
    est_sol : str

class SolicitudCreate(SolicitudBase):
    pass 

class SolicitudUpdate(SolicitudBase):
    pass 

class SolicitudResponse(SolicitudBase):
    cod_sol : int
    class Config:
        from_attributes : True