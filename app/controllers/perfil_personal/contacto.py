from sqlalchemy.orm import Session
from app.models.perfil_personal.contacto import Contacto
from app.schemas.perfil_personal.contacto import (
    ContactoUpdate,
    ContactoCreate
)

def get_all(
        db : Session,
        skip : int = 0,
        limit : int =0
):
    return db.query(Contacto).offset(skip).limit(limit).all()

def create(
        db : Session,
        contacto : ContactoCreate
):
    db_contacto = Contacto(**contacto.model_dump())
    db.add(db_contacto)
    db.commit()
    db.refresh(db_contacto)
    return db_contacto

def get_by_cod(
        db : Session,
        cod : int
):
    return db.query(Contacto).filter(Contacto.cod_con == cod).first()

def update(
        db : Session,
        cod : int,
        contacto : ContactoUpdate
):
    db_contacto = db.query(Contacto).filter(Contacto.cod_con == cod).first()
    if db_contacto:
        for key, value in contacto.model_dump(
            exclude_unset = True
        ).items():
            setattr(db_contacto,key,value)
            pass
        db.commit()
        db.refresh(db_contacto)
        pass
    return db_contacto

def delete(
        db : Session,
        cod : int
):
    db_contacto = db.query(Contacto).filter(Contacto.cod_con == cod).first()
    if db_contacto:
        db.delete(db_contacto)
        db.commit()
        pass
    return db_contacto