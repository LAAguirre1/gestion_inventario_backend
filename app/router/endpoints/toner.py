from typing import Any, Dict

from fastapi import APIRouter, Depends, HTTPException, Body, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import app.service as service
import app.model as model
import app.schema as schema
from app.utils import deps
from app.utils.config import settings
from typing import List

router = APIRouter()

@router.get("/", response_model=List[schema.Toner])
def read_toner(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: model.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Recuperar toners.
    """
    toners = service.toner.get_multi(db, skip=skip, limit=limit)
    return toners


@router.post(
        "/",
        status_code=status.HTTP_201_CREATED,
        response_model=schema.Toner
)
def create_toner(
    *,
    db: Session = Depends(deps.get_db),
    toner_in: schema.TonerCreate,
    current_user: model.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Crear toner.
    """
    toner = service.toner.get_by_name(db, name=toner_in.nombre)
    if toner:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El toner ya existe.",
        )
    
    toner = service.toner.create(db, obj_in=toner_in)
    return toner

@router.put("/{id}", response_model=schema.Toner)
def update_toner(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    toner_in: schema.TonerUpdate,
    current_user: model.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Actualizar toner.
    """
    toner = service.toner.get(db, id=id)
    if not toner:
        raise HTTPException(
            status_code=404,
            detail="El toner no existe.",
        )
    
    toner = service.toner.update(db, db_obj=toner, obj_in=toner_in)
    return toner