from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.perfil_personal.multimedia import(
    MultimediaUpdate,
    MultimediaCreate,
    MultimediaResponse
)
from app.controllers.perfil_personal.multimedia import(
    get_all,
    get_by_cod,
    create,
    update,
    delete
)

router = APIRouter()

@router.get(
    "/",
    response_model = list[MultimediaResponse]
)
def read_multimedia(
    skip : int = Query(
        0,
        description = "Numero de registros omitidos"
    ),
    limit : int = Query(
        100,
        description = "Numero maximo de registro"
    ),
    db : Session = Depends(get_db)
):
    return get_all(db, skip = skip, limit = limit)

@router.post(
    "/",
    response_model = MultimediaResponse,
    status_code = status.HTTP_201_CREATED
)
def create_multimedia(
    multimedia : MultimediaCreate,
    db : Session = Depends(get_db)
):
    db_multimedia = create(db, multimedia)
    if not db_multimedia:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Multimedia no creado :\n {db_multimedia}"
        )
    return db_multimedia

@router.get(
    "/{cod}",
    response_model = MultimediaResponse
)
def red_by_cod(
    cod : int,
    db : Session = Depends(get_db)
):
    db_multimedia = get_by_cod(db, cod)
    if not db_multimedia:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"multimedia de codigo {cod}, no existe"
        )
    return db_multimedia

@router.put(
    "/{cod}",
    response_model = MultimediaResponse
)
def update_multimedia(
    cod : int,
    multimedia : MultimediaUpdate,
    db : Session = Depends(get_db)
):
    db_multimedia = update(db, cod, multimedia)
    if not db_multimedia:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"multimedia de codigo {cod}, no ha sido encontrado"
        )
    return db_multimedia

@router.delete(
    "/{cod}",
    response_model = MultimediaResponse 
)
def delete_multimedia(
    cod : int,
    db : Session = Depends(get_db)
):
    db_multimedia = delete(db,cod)
    if not db_multimedia:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"multimedia con codigo {cod}, no encontrado"
        )
    return db_multimedia