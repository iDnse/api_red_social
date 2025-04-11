from fastapi import FastAPI
from app.database.database import Base, engine
from app.routes.general.categoria_acontecimiento import router as categoria_acontecimiento
from app.routes.general.tipo_contacto import router as tipo_contacto
from app.routes.general.tipo_acontecimiento import router as tipo_acontecimiento
from app.routes.perfil_personal.persona import router as persona
from app.routes.perfil_personal.contacto import router as contacto_persona
from app.routes.perfil_personal.multimedia import router as multimedia_persona
from app.routes.perfil_personal.publicacion import router as publicacion_persona
from app.routes.perfil_personal.solicitud import router as solicitud_persona

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API",
    description="API"
)

app.include_router(categoria_acontecimiento, prefix="/categoria_acontecimiento", tags=["CategoriaAcontecimiento"])
app.include_router(tipo_contacto, prefix="/tipo_contacto", tags=["TipoContacto"])
app.include_router(tipo_acontecimiento, prefix="/tipo_acontecimiento", tags=["TipoAcontecimiento"])
app.include_router(persona, prefix="/persona", tags=["Persona"])
app.include_router(contacto_persona, prefix="/contacto_persona", tags=["ContactoPersona"])
app.include_router(multimedia_persona, prefix="/multimedia_persona", tags=["MultimediaPersona"])
app.include_router(publicacion_persona, prefix="/publicacion_persona", tags=["PublicacionPersona"])
app.include_router(solicitud_persona, prefix="/solicitud_persona", tags=["SolicitudPersona"])