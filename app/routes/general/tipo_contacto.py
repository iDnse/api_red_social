from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.general.tipo_contacto import(
    TipoContactoCreate,
    TipoContactoResponse,
    TipoContactoUpdate
)
from app.controllers.general.tipo_contacto import (
    get_all_tipo_contacto,
    get_tipo_contacto_by_cod,
    create_tipo_contacto,
    update_tipo_contacto,
    delete_tipo_contacto
)

router = APIRouter()

@router.get("/", response_model = list[TipoContactoResponse])
def read_tipo(
    skip : int = Query(0, description = "Numero de registro a omitir"),
    limit : int = Query(10, description = "Numero maximo de registro"),
    db : Session = Depends(get_db)
):
    return get_all_tipo_contacto(db, skip = skip, limit = limit)

@router.post("/", response_model = TipoContactoResponse, status_code = status.HTTP_404_NOT_FOUND)
def create_tipo(
    tipo : TipoContactoCreate,
    db : Session = Depends(get_db)
):
    return create_tipo_contacto(db, tipo)

@router.get("/{cod}", response_model = TipoContactoResponse)
def read_tipo_by_cod(
    cod : int,
    db : Session = Depends(get_db)
):
    tipo = get_tipo_contacto_by_cod(db, cod)
    if not tipo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Tipo de contacto no encontrado"
        )
    return tipo

@router.put("/{cod}", response_model = TipoContactoResponse)
def update_tipo(
    cod : int,
    tipo_date : TipoContactoUpdate,
    db : Session = Depends(get_db)
):
    tipo = update_tipo_contacto(db, cod, tipo_date)
    if not tipo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Tipo de contacto no encontrado"
        )
    return tipo

@router.delete("/{cod}", response_model = TipoContactoResponse)
def delete_tipo(
    cod : int,
    db : Session = Depends(get_db)
):
    tipo = delete_tipo_contacto(db, cod)
    if not tipo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Tipo de contacto no encontrado"
        )
    return tipo