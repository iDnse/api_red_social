from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.perfil_personal.solicitud import (
    SolicitudCreate,
    SolicitudUpdate,
    SolicitudResponse
)
from app.controllers.perfil_personal.solicitud import (
    get_all_solicitudd,
    get_cod_solicitud,
    create_solicitud,
    update_solicitud,
    delete_solicitud
)


router = APIRouter()



@router.get(
    "/",
    response_model= list[SolicitudResponse]
)
def read(
    skip: int= Query(0, description="Registro omitidos"),
    limit: int= Query(100, description="Numero registro maximos"),
    db:Session=Depends(get_db)
):
    return get_all_solicitudd(db, skip=skip, limit=limit)




@router.post(
    "/",
    response_model= SolicitudResponse,
    status_code= status.HTTP_201_CREATED
)
def create(
    solicitud: SolicitudCreate,
    db: Session=Depends(get_db)
):
    db_solicitud = create_solicitud(db, solicitud)
    if not db_solicitud:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="solicitud no se creo"
        )
    return db_solicitud




@router.get(
    "/{cod}",
    response_model= SolicitudResponse
)
def read_cod(
    cod: int,
    db: Session=Depends(get_db)
):
    db_solicitud = get_cod_solicitud(db, cod)
    if not db_solicitud:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=f"solicitud de codigo {cod}, no encontrado"
        )
    return db_solicitud





@router.put(
    "/{cod}",
    response_model= SolicitudResponse
)
def update(
    cod : int,
    solicitud : SolicitudUpdate,
    db:Session=Depends(get_db)
):
    db_solicitud = update_solicitud(cod, solicitud, db)
    if not db_solicitud:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=f"Solicitud de codgio {cod}, no encontrado"
        )
    return db_solicitud




@router.delete(
    "/{cod}",
    response_model= SolicitudResponse
)
def delete(
    cod:int,
    db:Session=Depends(get_db)
):
    db_solicitud = delete_solicitud(cod, db)
    if not db_solicitud:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=f"Solicitud de codigo {cod}, no encontrada"
        )
    return db_solicitud