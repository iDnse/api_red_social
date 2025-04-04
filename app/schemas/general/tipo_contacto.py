# "cod_tico"	"integer"	
# "nom_tico"	"character varying"	50
# "est_tico"	"character"	1

from pydantic import BaseModel

class TipoContactoBase(BaseModel):
    nom_tico : str
    est_tico : str

class TipoContactoCreate(TipoContactoBase):
    pass

class TipoContactoUpdate(TipoContactoBase):
    pass

class TipoContactoResponse(TipoContactoBase):
    cod_tico : int
    class Config:
        from_attributes : True