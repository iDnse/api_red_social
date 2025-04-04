from sqlalchemy.orm import Session
from app.models.general.categoria_acontecimiento import CategoriaAcontecimiento
from app.schemas.general.categoria_acontecimiento import CategoriaAcontecimientoCreate,CategoriaAcontecimientoUpdate

def get_all_categoria_acontecimiento(
        db : Session,
        skip : int = 0,
        limit : int = 10
):
    return db.query(CategoriaAcontecimiento).offset(skip).limit(limit).all()

def create_categoria_acontecimiento(
        db: Session, 
        categoria_acontecimiento: CategoriaAcontecimientoCreate
):
    db_categoria = CategoriaAcontecimiento(**categoria_acontecimiento.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def get_categoria_acontecimiento_by_cod(
        db : Session,
        cod : int
):
    return db.query(CategoriaAcontecimiento).filter(CategoriaAcontecimiento.cod_cat_aco == cod).first()

def update_categoria_acontecimiento(
        db : Session,
        cod : int,
        categoria_acontecimiento = CategoriaAcontecimientoUpdate
):
    db_categoria = db.query(CategoriaAcontecimiento).filter(CategoriaAcontecimiento.cod_cat_aco == cod).first()
    if db_categoria:
        for key, value in categoria_acontecimiento.dict(exclude_unset=True).items():
            setattr(db_categoria, key, value)
        db.commit()
        db.refresh(db_categoria)
        pass
    return db_categoria
    
    
def delete_categoria_acontecimiento (
        db : Session,
        cod : int
):
    db_categoria = db.query(CategoriaAcontecimiento).filter(CategoriaAcontecimiento.cod_cat_aco == cod).first()
    if db_categoria:
        db.delete(db_categoria)
        db.commit()
        pass 
    return db_categoria