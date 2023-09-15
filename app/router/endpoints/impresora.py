from typing import Any, Dict, List

from fastapi import APIRouter, Depends, HTTPException, Body, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import service, model, schema
from app.utils import deps

router = APIRouter()

@router.get("/", response_model=List[schema.Impresora])
def read_impresoras(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: model.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Recuperar impresoras.
    """
    impresoras = service.impresora.get_multi(db, skip=skip, limit=limit)
    return impresoras


@router.get(
        "{/{id_impresora}", 
        response_model=schema.Impresora,
)
def read_impresora(
        db: Session = Depends(deps.get_db),
        id_impresora: int = 1,
        current_user: model.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    
    Recuperar impresora por id.
    """
    impresora = service.impresora.get(db, id_impresora=id_impresora)
    if not impresora:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El impresora no existe.",
        )
    return impresora


@router.post(
        "/", 
        status_code=status.HTTP_201_CREATED,
        response_model=schema.Impresora
)
def create_impresora(
    *,
    db: Session = Depends(deps.get_db),
    impresora_in: schema.ImpresoraCreate,
    current_user: model.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Crear impresora.
    """
    # Check if impresora already exists
    impresora = service.impresora.get_by_num_serie(db, num_serie=impresora_in.num_serie)
    if impresora:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El impresora ya existe.",
        )
    impresora = service.impresora.create_impresora(db, impresora=impresora_in)
    return impresora

