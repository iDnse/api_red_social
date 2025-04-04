from sqlalchemy.orm import Session
from app.models.general.tipo_contacto import TipoContacto
from app.schemas.general.tipo_contacto import TipoContactoCreate, TipoContactoUpdate

def get_all_tipo_contacto(
        db : Session,
        skip : int = 0,
        limit : int = 0
):
    return db.query(TipoContacto).offset(skip).limit(limit).all()

def create_tipo_contacto(
        db : Session,
        tipo_contacto : TipoContactoCreate
):
    db_tipo = TipoContacto(**tipo_contacto.model_dump())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

def get_tipo_contacto_by_cod(
        db : Session,
        cod : int
):
    return db.query(TipoContacto).filter(TipoContacto.cod_tico == cod).first()

def update_tipo_contacto(
        db : Session,
        cod : int,
        tipo_contacto : TipoContactoUpdate
):
    db_tipo = db.query(TipoContacto).filter(TipoContacto.cod_tico == cod).first()
    if db_tipo :
        for key, value in tipo_contacto.model_dump(exclude_unset=True).items():
            setattr(db_tipo, key, value)
            pass
        db.commit()
        db.refresh(db_tipo)
        pass
    return db_tipo

def delete_tipo_contacto(
        db : Session,
        cod : int
):
    db_tipo = db.query(TipoContacto).filter(TipoContacto.cod_tico == cod).first()
    if db_tipo:
        db.delete(db_tipo)
        db.commit()
        pass
    return db_tipo