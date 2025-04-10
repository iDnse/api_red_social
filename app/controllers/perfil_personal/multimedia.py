from sqlalchemy.orm import Session
from app.models.perfil_personal.multimedia import Multimedia
from app.schemas.perfil_personal.multimedia import (
    MultimediaCreate,
    MultimediaUpdate
)

def get_all(
        db : Session,
        skip : int = 0,
        limit : int = 0
):
    return db.query(Multimedia).offset(skip).limit(limit).all()

def create(
        db : Session,
        multimedia = MultimediaCreate
):
    db_multimedia = Multimedia(**multimedia.model_dump())
    db.add(db_multimedia)
    db.commit()
    db.refresh(db_multimedia)
    return db_multimedia

def get_by_cod(
        db : Session,
        cod : int
):
    return db.query(Multimedia).filter(Multimedia.cod_mul ==  cod).first()

def update(
        db : Session,
        cod : int,
        multimedia : MultimediaUpdate
):
    db_multimedia = db.query(Multimedia).filter(Multimedia.cod_mul == cod).first()
    if db_multimedia:
        for key, value in multimedia.model_dump(
            exclude_unset = True
        ).items():
            setattr(db_multimedia, key, value)
            pass
        db.commit()
        db.refresh(db_multimedia)
        pass
    return db_multimedia

def delete(
        db : Session,
        cod : int
):
    db_multimedia = db.query(Multimedia).filter(Multimedia.cod_mul == cod).first()
    if db_multimedia:
        db.delete(db_multimedia)
        db.commit()
        pass
    return db_multimedia