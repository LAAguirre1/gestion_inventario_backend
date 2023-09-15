from datetime import date

from typing import Optional
from pydantic import BaseModel, ConfigDict, constr


class EntregaBase(BaseModel):
    sucursal: Optional[constr(max_length=25)] = None
    seccion: Optional[constr(max_length=25)] = None
    nuevo_contador: Optional[int] = None
    fecha: Optional[date] = None
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "sucursal": "Concepción",
                    "seccion": "Salón",
                    "nuevo_contador": 25250,
                    "fecha": "2023-09-04",
                }
            ]
        }
    }
    

class EntregaCreate(EntregaBase):
    sucursal: constr(max_length=25)
    seccion: constr(max_length=25)
    nuevo_contador: int
    fecha: date


class EntregaUpdate(EntregaBase):
    pass


class EntregaInDBBase(EntregaBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    sucursal: constr(max_length=25)
    seccion: constr(max_length=25)
    nuevo_contador: int
    fecha: date
    diferencia: int
    toner_id: int
    impresora_id: int


class Entrega(EntregaInDBBase):
    pass


class EntregaInDB(EntregaInDBBase):
    pass

