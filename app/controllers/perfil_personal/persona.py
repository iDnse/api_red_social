from sqlalchemy.orm import Session
from app.models.perfil_personal.persona import Persona
from app.schemas.perfil_personal.persona import (
    PersonaCreate,
    PersonaUpdate
)

def get_all_persona(
        db : Session,
        skip : int = 0,
        limit : int = 0
):
    return db.query(Persona).offset(skip).limit(limit).all()

def create_persona(
        db : Session,
        persona : PersonaCreate
):
    db_persona = Persona(**persona.model_dump())
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    return db_persona

def get_persona_by_cod(
        db : Session,
        cod : int
):
    return db.query(Persona).filter(Persona.cod_per == cod).first()

def update_persona(
        db : Session,
        cod : int,
        persona : PersonaUpdate
):
    db_persona = db.query(Persona).filter(Persona.cod_per == cod).first()
    if db_persona:
        for key, value in persona.model_dump(
            exclude_unset = True
        ).items():
            setattr(db_persona, key, value)
            pass
        db.commit()
        db.refresh(db_persona)
        pass
    return db_persona

def delete_persona(
        db : Session,
        cod : int
):
    db_persona = db.query(Persona).filter(Persona.cod_per == cod).first()
    if db_persona:
        db.delete(db_persona)
        db.commit()
        pass
    return db_persona