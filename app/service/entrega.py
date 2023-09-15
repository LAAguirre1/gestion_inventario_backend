from sqlalchemy.orm import Session

from app.model.entrega import Entrega
from app.schema.entrega import EntregaCreate, EntregaUpdate

from app.service.base import CRUDBase
from app.service.impresora import impresora
from app.service.toner import toner
from typing import Optional


class CRUDEntrega(CRUDBase[Entrega, EntregaCreate, EntregaUpdate]):
    
    def create_entrega(self, db: Session, entrega_in: EntregaCreate, toner_id: int, impresora_id: int):
        impres = impresora.get(db=db, id=impresora_id)
        ton = toner.get(db, id=toner_id)
        ton.cantidad = ton.cantidad -1
        db.add(ton)
        dif = entrega_in.nuevo_contador - impres.contador_copia
        impres.contador_copia = entrega_in.nuevo_contador
        db_item = Entrega(**entrega_in.model_dump(), diferencia=dif, toner_id=toner_id, impresora_id=impresora_id)
        db.add(impres)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item


entrega = CRUDEntrega(Entrega)