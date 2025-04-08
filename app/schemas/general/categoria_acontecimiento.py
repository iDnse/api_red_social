# "cod_cat_aco"	"integer"	"NO"		32
# "nom_cat_aco"	"character varying"	"NO"	75	
# "est_cat_aco"	"character"	"NO"	1	

from pydantic import BaseModel

class CategoriaAcontecimientoBase(BaseModel):
    nom_cat_aco : str
    est_cat_aco : str

class CategoriaAcontecimientoCreate(CategoriaAcontecimientoBase):
    pass

class CategoriaAcontecimientoUpdate(CategoriaAcontecimientoBase):
    pass

class CategoriaAcontecimientoResponse(CategoriaAcontecimientoBase):
    cod_cat_aco : int
    class Config: 
        from_attributes : True