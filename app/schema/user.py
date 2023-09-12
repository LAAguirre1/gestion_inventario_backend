from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "mimail@mail.com",
                    "full_name": "Mi nombre",
                    "password": "mi_contraseña",
                }
            ]
        }
    }


class UserCreate(UserBase):
    full_name: str
    email: EmailStr
    password: str
    
class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDBBase(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None


class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    hashed_password: str