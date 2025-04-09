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
from pydantic import BaseModel
from datetime import date

class PersonaBase(BaseModel):
    nm1_per : str
    nm2_per : str
    ap1_per : str
    ap2_per : str
    nac_per : date
    sex_per : str
    per_per : str
    por_per : str
    fky_usu : int
    est_per : str

class PersonaCreate(PersonaBase):
    pass

class PersonaUpdate(PersonaBase):
    pass

class PersonaResponse(PersonaBase):
    cod_per : int
    class Config:
        from_attributes : True