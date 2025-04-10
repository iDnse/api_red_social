from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.controllers.perfil_personal.publicacion import(
    get_all_publicacion,
    get_cod_publicacion,
    create_publicacion,
    update_publicacion,
    delete_publicacion
)
from app.schemas.perfil_personal.publicacion import (
    PublicacionCreate,
    PublicacionUpdate,
    PublicacionResponse
)

router = APIRouter()



@router.get("/", response_model=list[PublicacionResponse])
def read(
    skip:int=Query(0,description="Registros omitidos"),
    limit:int=Query(100,description="Nuemero registro maximos"),
    db:Session=Depends(get_db)
):
    return get_all_publicacion(db, skip=skip, limit=limit)




@router.post(
    "/",
    response_model=PublicacionResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    publiacion:PublicacionUpdate,
    db:Session=Depends(get_db)
):
    db_publiacion= create_publicacion(db,publiacion)
    if not db_publiacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Publicacion no creada"
        )
    return db_publiacion




@router.get(
    "/{cod}",
    response_model=PublicacionResponse
)
def read_cod(
    cod:int,
    db:Session=Depends(get_db)
):
    db_publicacion = get_cod_publicacion(db,cod)
    if not db_publicacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Publicacion cod {cod} no encontrado"
        )
    return db_publicacion






@router.put(
    "/{cod}",
    response_model=PublicacionResponse,
)
def update(
    cod:int,
    publicacion:PublicacionUpdate,
    db:Session=Depends(get_db)
):
    db_publicacion = update_publicacion(db, cod, publicacion)
    if not db_publicacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Publicacion {cod} no encontrada"
        )
    return  db_publicacion




@router.delete(
    "/{cod}",
    response_model=PublicacionResponse
)
def delete(
    cod:int,
    db:Session=Depends(get_db)
):
    db_publicacion = delete_publicacion(db,cod)
    if not db_publicacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Publicacion {cod} no encontrada"
        )
    return  db_publicacion