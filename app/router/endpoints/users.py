from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Body, status
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session


import app.service as service
import app.model as model
import app.schema as schema
from app.utils import deps
from app.utils.config import settings


router = APIRouter()

@router.get("/", response_model=List[schema.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: model.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Recuperar ususarios.
    """
    users = service.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post(
        "/",
        response_model=schema.User,
        status_code=status.HTTP_201_CREATED,
)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schema.UserCreate,
    current_user: model.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Crear un usuario.
    """
    user = service.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="El usuario ya existe.",
        )
    user = service.user.create(db, obj_in=user_in)
    return user


@router.put("/me", response_model=schema.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: model.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Actualizar usuario.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schema.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    user = service.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/me", response_model=schema.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: model.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Recuperar usuario actual.
    """
    return current_user


@router.post("/open", response_model=schema.User)
def create_user_open(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
Ç) -> Any:
    """
    Crear un usuario sin necesidad de iniciar sesión.
    """
    if not settings.user_open_registration:
        raise HTTPException(
            status_code=403,
            detail="El registro abierto de usuarios está prohibido en este servidor.",
        )
    user = service.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="El usuario ya existe.",
        )
    user_in = schema.UserCreate(password=password, email=email, full_name=full_name)
    user = service.user.create(db, obj_in=user_in)
    return user


@router.get("/{user_id}", response_model=schema.User)
def read_user_by_id(
    user_id: int,
    current_user: model.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Recuperar usuario por id.
    """
    user = service.user.get(db, id=user_id)
    if user == current_user:
        return user
    if not service.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="No tiene permisos para acceder a este usuario."
        )
    return user


@router.put("/{user_id}", response_model=schema.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: schema.UserUpdate,
    current_user: model.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Actualizar usuario.
    """
    user = service.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="El usuario no existe.",
        )
    user = service.user.update(db, db_obj=user, obj_in=user_in)
    return user