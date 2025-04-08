from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.general.tipo_acontecimiento import (
    TipoAcontecimientoResponse,
    TipoAcontecimientoCreate,
    TipoAcontecimientoUpdate
)
from app.controllers.general.tipo_acontecimiento import (
    get_all_tipo_acontecimiento,
    get_tipo_acontecimiento_by_cod,
    create_tipo_acontecimiento,
    update_tipo_acontecimiento,
    delete_tipo_acontecimiento
)

router = APIRouter()

@router.get("/", response_model = list[TipoAcontecimientoResponse])
def read_tipo(
    skip : int = Query(0, description = "Numero de registro a omitir"),
    limit : int = Query(10, description = "Numero maximo de registro"),
    db : Session = Depends(get_db)
):
    return get_all_tipo_acontecimiento(db, skip = skip, limit = limit)

@router.post("/", response_model = TipoAcontecimientoResponse, status_code = status.HTTP_404_NOT_FOUND)
def create_tipo(
    tipo : TipoAcontecimientoCreate,
    db : Session = Depends(get_db)
):
    return create_tipo_acontecimiento(db, tipo)

@router.get("/{cod}", response_model = TipoAcontecimientoResponse)
def  read_tipo_by_cod(
    cod : int,
    db : Session = Depends(get_db)
):
    db_tipo = get_tipo_acontecimiento_by_cod(db,cod)
    if not db_tipo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "tipo de acontecimeinto no encontrado"
        )
    return db_tipo

@router.put("/{cod}", response_model = TipoAcontecimientoResponse)
def update_tipo(
    cod : int,
    tipo : TipoAcontecimientoUpdate,
    db : Session = Depends(get_db)
):
    db_tipo = update_tipo_acontecimiento(
        db, cod, tipo
    )
    if not db_tipo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "tipo de acontecimiento no encontrado"
        )
    return db_tipo

@router.delete("/{cod}", response_model = TipoAcontecimientoResponse)
def delete_tipo(
    cod : int,
    db : Session = Depends(get_db)
):
    db_tipo = delete_tipo_acontecimiento(db, cod)
    if not db_tipo :
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "tipo acontecimiento no encontrado"
        )
    return db_tipo