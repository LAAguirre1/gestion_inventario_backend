from sqlalchemy.orm import Session

from app.model.impresora import Impresora
from app.schema.impresora import ImpresoraCreate, ImpresoraUpdate

from app.service.base import CRUDBase
from typing import Optional


class CRUDImpresora(CRUDBase[Impresora, ImpresoraCreate, ImpresoraUpdate]):
    def get_by_num_serie(self, db: Session, *, num_serie: str) -> Optional[Impresora]:
        return db.query(Impresora).filter(Impresora.num_serie == num_serie).first()
    

    def create_impresora(self, db: Session, impresora: ImpresoraCreate):
        db_impresora = Impresora(**impresora.model_dump())
        db.add(db_impresora)
        db.commit()
        db.refresh(db_impresora)
        return db_impresora

impresora = CRUDImpresora(Impresora)