from datetime import date

from typing import Optional
from pydantic import BaseModel, ConfigDict, constr


class ImpresoraBase(BaseModel):
    impresora: Optional[constr(max_length=50)] = None
    num_serie: Optional[constr(max_length=20)] = None
    contador_copia: Optional[int] = None
    sucursal: Optional[constr(max_length=30)] = None
    seccion: Optional[constr(max_length=30)] = None
    ultimo_mantenimiento: Optional[date] = None
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "impresora": "HP LaserJet Pro M12w",
                    "num_serie": "VNCY614901",
                    "contador_copia": 23950,
                    "sucursal": "Alem",
                    "seccion": "Caja",
                    "ultimo_mantenimiento": "2023-04-12"
                }
            ]
        }
    }
    

class ImpresoraCreate(ImpresoraBase):
    pass


class ImpresoraUpdate(ImpresoraBase):
    pass
    
    
class ImpresoraInDBBase(ImpresoraBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    contador_copia: int


class Impresora(ImpresoraInDBBase):
    pass


class ImpresoraInDB(ImpresoraInDBBase):
    pass