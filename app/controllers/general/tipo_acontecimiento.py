from sqlalchemy.orm import Session
from app.models.general.tipo_acontecimiento import TipoAcontecimiento
from app.schemas.general.tipo_acontecimiento import (
    TipoAcontecimientoCreate,
    TipoAcontecimientoUpdate
)

def get_all_tipo_acontecimiento(
        db : Session,
        skip: int = 0,
        limit: int = 0
):
    return db.query(TipoAcontecimiento).offset(skip).limit(limit).all()

def create_tipo_acontecimiento(
        db : Session,
        tipo_acontecimiento : TipoAcontecimientoCreate
):
    db_tipo = TipoAcontecimiento(**tipo_acontecimiento.model_dump())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

def get_tipo_acontecimiento_by_cod(
        db : Session,
        cod : int
):
    return db.query(TipoAcontecimiento).filter(TipoAcontecimiento.cod_tip_aco == cod).first()

def update_tipo_acontecimiento(
        db : Session,
        cod : int,
        tipo_acontecimiento : TipoAcontecimientoUpdate
):
    db_tipo = db.query(TipoAcontecimiento).filter(TipoAcontecimiento.cod_tip_aco == cod).first()
    if db_tipo :
        for key, value in tipo_acontecimiento.model_dump(exclude_unset = True).items():
            setattr(db_tipo, key, value)
            pass
        db.commit()
        db.refresh(db_tipo)
        pass
    return db_tipo

def delete_tipo_acontecimiento(
        db : Session,
        cod : int 
):
    db_tipo = db.query(TipoAcontecimiento).filter(TipoAcontecimiento.cod_tip_aco == cod).first()
    if db_tipo :
        db.delete(db_tipo)
        db.commit()
        pass
    return db_tipo