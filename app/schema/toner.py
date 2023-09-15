from typing import Optional
from pydantic import BaseModel, ConfigDict, constr


class TonerBase(BaseModel):
    nombre: Optional[constr(max_length=30)] = None
    descripcion: Optional[constr(max_length=100)] = None
    cantidad: Optional[int] = None
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nombre": "CF279A",
                    "descripcion": "Proveedor Basla para impresoras HP LaserJet Pro M12w",
                    "cantidad": 50,
                }
            ]
        }
    }


class TonerCreate(TonerBase):
    nombre: constr(max_length=30)


class TonerUpdate(TonerBase):
    pass

class TonerInDBBase(TonerBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class Toner(TonerInDBBase):
    pass


class TonerInDB(TonerInDBBase):
    pass
    
