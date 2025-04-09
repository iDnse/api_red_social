from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.perfil_personal.persona import (
    PersonaCreate,
    PersonaUpdate,
    PersonaResponse
)
from app.controllers.perfil_personal.persona import (
    get_all_persona,
    get_persona_by_cod,
    create_persona,
    update_persona,
    delete_persona
)

router = APIRouter()

@router.get(
    "/",
    response_model = list[PersonaResponse]
)
def read(
    skip : int = Query(
        0,
        description = "Numero de registros a omitir"
    ),
    limit : int = Query(
        10,
        description = "Numero maximo de registro"
    ),
    db : Session = Depends(get_db)
):
    return get_all_persona(db, skip = skip, limit = limit)

@router.post(
    "/",
    response_model = PersonaResponse,
    status_code = status.HTTP_201_CREATED
)
def create(
    persona : PersonaCreate,
    db : Session = Depends(get_db)
):
    db_persona = create_persona(db, persona)
    if not db_persona:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "persona no creada"
        )
    return db_persona

@router.get(
    "/{cod}",
    response_model = PersonaResponse
)
def read_by_cod(
    cod : int,
    db : Session = Depends(get_db)
):
    db_persona = get_persona_by_cod(db, cod)
    if not db_persona:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "persona no encontrada"
        )
    return db_persona

@router.put(
    "/{cod}",
    response_model = PersonaResponse
)
def update(
 cod : int,
 persona : PersonaUpdate,
 db : Session = Depends(get_db)   
):
    db_persona = update_persona(db,cod,persona)
    if not persona:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"persona de codigo:{cod} no encontrada"
        )
    return db_persona

@router.delete(
    "/{cod}",
    response_model = PersonaResponse
)
def delete(
    cod : int,
    db : Session = Depends(get_db)
):
    db_persona = delete_persona(db, cod)
    if not db_persona:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"persona de codigo:{cod} no encontrado"
        )
    return db_persona