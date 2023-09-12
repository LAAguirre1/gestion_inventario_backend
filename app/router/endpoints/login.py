from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from ... import service, model, schema
from ...utils import deps, security
from ...utils.config import settings
from ...utils.security import get_password_hash

router = APIRouter()


@router.post("/login/access-token", response_model=schema.Token)
def login_access_token(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    Inicio de sesión con token compatible con OAuth2, obtenga un token de acceso para futuras solicitudes
    """
    user = service.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    elif not service.user.is_active(user):
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    return{
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

@router.post("/login/test-token", response_model=schema.User)
def test_token(current_user: model.User = Depends(deps.get_current_user)) -> Any:
    """
    Testear el token de acceso
    """
    return current_user

 
