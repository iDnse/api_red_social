from sqlalchemy.orm import Session
from app.models.perfil_personal.solicitud import Solicitud
from app.schemas.perfil_personal.solicitud import (
    SolicitudCreate,
    SolicitudUpdate
)

def get_all_solicitudd(
        db:Session,
        skip: int= 0,
        limit: int= 0
):
    return db.query(Solicitud).offset(skip).limit(limit).all()



def create_solicitud(
        db:Session,
        solicitud:SolicitudCreate
):
    db_solicitud = Solicitud(**solicitud.model_dump())
    db.add(db_solicitud)
    db.commit()
    db.refresh(db_solicitud)
    return db_solicitud


def get_cod_solicitud(
        db:Session,
        cod:int
):
    return  db.query(Solicitud).filter(Solicitud.cod_sol == cod).first()



def update_solicitud(
        cod:int,
        solicitud:SolicitudUpdate,
        db:Session
):
    db_solicitud = db.query(Solicitud).filter(Solicitud.cod_sol == cod).first()
    if db_solicitud:
        for key, value in solicitud.model_dump(exclude_unset=True).items():
            setattr(db_solicitud, key, value)
            pass
        db.commit()
        db.refresh(db_solicitud)
        pass
    return db_solicitud



def delete_solicitud(
        cod:int,
        db:Session
):
    db_solicitud = db.query(Solicitud).filter(Solicitud.cod_sol == cod).first()
    if db_solicitud:
        db.delete(db_solicitud)
        db.commit()
        pass
    return db_solicitud