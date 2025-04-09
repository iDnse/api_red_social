from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.perfil_personal.contacto import(
    ContactoCreate,
    ContactoResponse,
    ContactoUpdate
)
from app.controllers.perfil_personal.contacto import(
    get_all,
    get_by_cod,
    create,
    update,
    delete
)

router = APIRouter()

@router.get(
    "/",
    response_model = list[ContactoResponse]
)
def read_contacto(
    skip : int = Query(
        0,
        description = "Numero de registro a omitir"
    ),
    limit : int = Query(
        100,
        description = "Numero maximo de registro"
    ),
    db : Session = Depends(get_db)
):
    return get_all(db, skip=skip, limit=limit)

@router.post(
    "/",
    response_model = ContactoResponse,
    status_code = status.HTTP_201_CREATED
)
def create_contacto(
    contacto : ContactoCreate,
    db : Session =Depends(get_db)
):
    db_contacto = create(db,contacto)
    if not db_contacto:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "contacto no creado"
        )
    return db_contacto

@router.get(
    "/{cod}",
    response_model = ContactoResponse
)
def read_by_cod(
    cod : int,
    db : Session = Depends(get_db)
):
    db_contacto = get_by_cod(db, cod)
    if not db_contacto:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "contacto no encontrado"
        )
    return db_contacto

@router.put(
    "/{cod}",
    response_model = ContactoResponse
)
def update_contacto(
    cod : int,
    contacto : ContactoUpdate,
    db : Session = Depends(get_db)
):
    db_contacto = update(db, cod, contacto)
    if not db_contacto:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "contacto no encontrado"
        )
    return db_contacto

@router.delete(
    "/{cod}",
    response_model = ContactoResponse
)
def delete_contacto(
    cod : int,
    db : Session = Depends(get_db)
):
    db_contacto = delete(db,cod)
    if not db_contacto:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "contacto no encontrado"
        )
    return db_contacto