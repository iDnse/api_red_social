# "cod_mul"	"integer"		"NO"
# "url_mul"	"character varying"	255	"NO"
# "fky_pub"	"integer"		"NO"
# "est_mul"	"character"	1	"NO"
# P: Publicado Correctamente
# X: Suspendida la imagen o video por infringir normas comunitarias
# R: Restringida para pùblico sensible
# S: Publicaciòn de temas polìticos o sociales.
from pydantic import BaseModel

class MultimediaBase(BaseModel):
    url_mul : str
    fky_pub : int
    est_mul : str

class MultimediaCreate(MultimediaBase):
    pass

class MultimediaUpdate(MultimediaBase):
    pass

class MultimediaResponse(MultimediaBase):
    cod_mul : int
    class Config:
        from_attributes : True