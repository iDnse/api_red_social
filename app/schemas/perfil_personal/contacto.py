# "cod_con"	"integer"		"NO"
# "des_con"	"character varying"	100	"NO"
# "act_con"	"date"		"NO"
# "fky_per"	"integer"		"NO"
# "fky_tip_co"	"integer"		"NO"
# "fky_tip_pri"	"integer"		"NO"
# "est_con"	"character"	1	"NO"
from pydantic import BaseModel
from datetime import date

class ContactoBase(BaseModel):
    des_con : str
    act_con : date
    fky_per : int
    fky_tip_co : int
    fky_tip_pri : int
    est_con : str

class ContactoCreate(ContactoBase):
    pass

class ContactoUpdate(ContactoBase):
    pass

class ContactoResponse(ContactoBase):
    cod_con : int
    class Config:
        from_attributes : True