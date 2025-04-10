# "cod_pub"	"integer"		"NO"
# "fec_pub"	"date"		"NO"
# "tit_pub"	"character varying"		"NO"
# "des_pub"	"text"		"YES"
# "fky_ciu"	"integer"		"YES"
# "fky_per"	"integer"		"NO"
# "fky_tip_aco"	"integer"		"NO"
# "fky_tip_pri"	"integer"		"NO"
# "est_pub"	"character"	1	"NO"

from pydantic import BaseModel
from datetime import date

class PublicacionBase(BaseModel):
    fec_pub : date
    tit_pub : str
    des_pub : str
    fky_ciu : int
    fky_per : int
    fky_tip_aco : int
    fky_tip_pri : int
    est_pub : str
    pass

class PublicacionCreate(PublicacionBase):
    pass

class PublicacionUpdate(PublicacionBase):
    pass

class PublicacionResponse(PublicacionBase):
    cod_pub : int
    class Config:
        from_attributes : True