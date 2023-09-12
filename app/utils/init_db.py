from sqlalchemy.orm import Session

from app.utils.base_class import Base
from app import service, schema
from app.utils import base
from app.utils.config import settings
from app.utils.session import engine


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)

    user = service.user.get_by_email(db, email=settings.first_superuser)
    if not user:
        user_in = schema.UserCreate(
            full_name=settings.first_superuser,
            email=settings.first_superuser_mail,
            password=settings.first_superuser_password,
            is_superuser=True,
        )
        user = service.user.create(db, obj_in=user_in)
