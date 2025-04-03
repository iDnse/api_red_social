from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.general.categoria_acontecimiento import CategoriaAcontecimientoResponse
from app.controllers.general.categoria_acontecimiento import get_all_categoria_acontecimiento

router = APIRouter()

@router.get("/", response_model=list[CategoriaAcontecimientoResponse])
def read_tipo_acontecimiento(
    db : Session = Depends(get_db)
):
    return get_all_categoria_acontecimiento(db)