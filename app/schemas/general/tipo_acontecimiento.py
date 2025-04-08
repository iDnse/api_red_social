# "cod_tip_aco"	"integer"		"NO"
# "nom_tip_aco"	"character varying"	50	"NO"
# "fky_cat_aco"	"integer"		"NO"
# "est_tip_aco"	"character"	1	"NO"

from pydantic import BaseModel

class TipoAcontecimientoBase(BaseModel):
    nom_tip_aco : str
    fky_cat_aco : int
    est_tip_aco : str

class TipoAcontecimientoCreate(TipoAcontecimientoBase):
    pass

class TipoAcontecimientoUpdate(TipoAcontecimientoBase):
    pass

class TipoAcontecimientoResponse(TipoAcontecimientoBase):
    cod_tip_aco : int
    class Config:
        from_attributes : True