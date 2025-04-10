from sqlalchemy.orm import Session
from app.models.perfil_personal.publicacion import Publicacion
from app.schemas.perfil_personal.publicacion import (
    PublicacionCreate,
    PublicacionUpdate
)




def get_all_publicacion(
        db : Session,
        skip : int = 0,
        limit : int = 0
):
    return db.query(Publicacion).offset(skip).limit(limit).all()



def create_publicacion(
        db : Session,
        publicacion : PublicacionCreate,
):
    db_publicacion = Publicacion(**publicacion.model_dump())
    db.add(db_publicacion)
    db.commit()
    db.refresh(db_publicacion)
    return db_publicacion



def get_cod_publicacion(
        db : Session,
        cod : int
):
    return db.query(Publicacion).filter(Publicacion.cod_pub == cod).first()



def update_publicacion(
        db : Session,
        cod : int,
        publicacion : PublicacionUpdate
):
    db_publicacion = db.query(Publicacion).filter(Publicacion.cod_pub == cod).first()
    if db_publicacion:
        for key, value in publicacion.model_dump(exclude_unset=True).items():
            setattr(db_publicacion, key, value)
            pass
        db.commit()
        db.refresh(db_publicacion)
        pass
    return db_publicacion



def delete_publicacion(
        db : Session,
        cod : int
):
    db_publicacion = db.query(Publicacion).filter(Publicacion.cod_pub == cod).first()
    if db_publicacion :
        db.delete(db_publicacion)
        db.commit()
        pass
    return db_publicacion