from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.database.database import Base

"""
Modelo de categoría de acontecimientos.

Attributes:
    cod_cat_aco: Código único de la categoría (PK)
    nom_cat_aco: Nombre de la categoría
    est_cat_aco: Estado de la categoría (activo/inactivo)
    fecha_creacion: Fecha de creación del registro
    fecha_actualizacion: Fecha de última actualización
"""
class CategoriaAcontecimiento(Base):
    __tablename__ = "categoria_acontecimiento"
    __table_args__ = (
        {"schema": "general"},
        {"comment": "Tabla que almacena las categorías de acontecimientos"}
    )

    # Columnas principales
    cod_cat_aco: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True,
        index=True,
        comment="Código único de la categoría"
    )
    
    nom_cat_aco: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        comment="Nombre descriptivo de la categoría"
    )
    
    est_cat_aco: Mapped[str] = mapped_column(
        String(1),
        nullable=False,
        default="A",
        comment="Estado: A=Activo, I=Inactivo"
    )
    
    # Metadatos adicionales
    fecha_creacion: Mapped[datetime] = mapped_column(
        default=datetime.utcnow,
        comment="Fecha de creación del registro"
    )
    
    fecha_actualizacion: Mapped[datetime] = mapped_column(
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        comment="Fecha de última actualización"
    )

    def __repr__(self) -> str:
        return f"<CategoriaAcontecimiento(cod={self.cod_cat_aco}, nombre={self.nom_cat_aco})>"