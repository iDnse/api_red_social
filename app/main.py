from fastapi import FastAPI
from app.database.database import Base, engine
from app.routes.general.categoria_acontecimiento import router as categoria_acontecimiento_routers

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API",
    description="API"
)

app.include_router(categoria_acontecimiento_routers, prefix="/categoria_acontecimiento", tags=["CategoriaAcontecimiento"])