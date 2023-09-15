from typing import Any, Dict, List

from fastapi import APIRouter, Depends, HTTPException, Body, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import service, model, schema
from app.utils import deps

router = APIRouter()


@router.get("/", response_model=List[schema.Entrega])
def read_entregas(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: model.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Recuperar entregas.
    """
    entregas = service.entrega.get_multi(db, skip=skip, limit=limit)
    return entregas


@router.post("/", response_model=schema.Entrega, status_code=status.HTTP_201_CREATED)
def create_entrega(
    *,
    db: Session = Depends(deps.get_db),
    entrega_in: schema.EntregaCreate,
    id_impresora: int = 1,
    id_toner: int = 1,
    current_user: model.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Crear entrega.
    """
    entrega = service.entrega.create_entrega(
        db,
        entrega_in,
        toner_id=id_toner,
        impresora_id=id_impresora
    )
    return entrega