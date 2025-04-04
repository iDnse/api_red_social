from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.general.categoria_acontecimiento import (
    CategoriaAcontecimientoCreate,
    CategoriaAcontecimientoResponse,
    CategoriaAcontecimientoUpdate
)
from app.controllers.general.categoria_acontecimiento import (
    get_all_categoria_acontecimiento,
    get_categoria_acontecimiento_by_cod,
    create_categoria_acontecimiento,
    update_categoria_acontecimiento,
    delete_categoria_acontecimiento
)

router = APIRouter()

@router.get("/", response_model = list[CategoriaAcontecimientoResponse])
def read_categoria (
    skip : int = Query(0, description = "Numero de registro a omitir"),
    limit : int = Query(10, description = "Numero maximo de registro"),
    db : Session = Depends(get_db)
):
    return get_all_categoria_acontecimiento(db, skip = skip, limit = limit)

@router.post("/", response_model = CategoriaAcontecimientoResponse, status_code = status.HTTP_201_CREATED)
def create_categoria(
    categoria : CategoriaAcontecimientoCreate,
    db : Session = Depends(get_db)
):
    return create_categoria_acontecimiento(db, categoria)

@router.get("/{cod}", response_model=CategoriaAcontecimientoResponse)
def read_categoria_by_id(
    cod : int,
    db : Session = Depends(get_db)
):
    categoria = get_categoria_acontecimiento_by_cod(db, cod)
    if not categoria :
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Categoria no encontrada"
        )
    return categoria

@router.put("/{cod}", response_model=CategoriaAcontecimientoResponse)
def update_categoria(
    cod : int,
    categoria_date : CategoriaAcontecimientoUpdate,
    db : Session = Depends(get_db)
):
    categoria = update_categoria_acontecimiento(db, cod, categoria_date)
    if not categoria :
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "categoria no encontrada"
        )
    return categoria

@router.delete("/{cod}", response_model=CategoriaAcontecimientoResponse)
def delete_categoria(
    cod : int,
    db : Session = Depends(get_db)
):
    categoria  = delete_categoria_acontecimiento(db, cod)
    if not categoria :
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Categoria no encontrada"
        )
    return categoria