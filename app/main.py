from fastapi import FastAPI
from app.database.database import Base, engine
from app.routes.general.categoria_acontecimiento import router as categoria_acontecimiento
from app.routes.general.tipo_contacto import router as tipo_contacto

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API",
    description="API"
)

app.include_router(categoria_acontecimiento, prefix="/categoria_acontecimiento", tags=["CategoriaAcontecimiento"])
app.include_router(tipo_contacto, prefix="/tipo_contacto", tags=["TipoContacto"])