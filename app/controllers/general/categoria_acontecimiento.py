from sqlalchemy.orm import Session
from app.models.general.categoria_acontecimiento import CategoriaAcontecimiento
from app.schemas.general.categoria_acontecimiento import CategoriaAcontecimientoCreate,CategoriaAcontecimientoResponse,CategoriaAcontecimientoUpdate

def get_all_categoria_acontecimiento(
        db : Session,
        skip : int = 0,
        limit : int = 10
):
    return db.query(CategoriaAcontecimiento).offset(skip).limit(limit).all()