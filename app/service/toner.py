from sqlalchemy.orm import Session

from app.model.toner import Toner
from app.schema.toner import TonerCreate, TonerUpdate

from app.service.base import CRUDBase
from typing import Optional


class CRUDToner(CRUDBase[Toner, TonerCreate, TonerUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Toner]:
        return db.query(Toner).filter(Toner.nombre == name).first()
    

toner = CRUDToner(Toner)