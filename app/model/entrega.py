from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import List, TYPE_CHECKING

from app.utils.base_class import Base

if TYPE_CHECKING:
    from .toner import Toner  # noqa: F401
    from .impresora import Impresora  # noqa: F401

class Entrega(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    sucursal: Mapped[str] = mapped_column(String(25))
    seccion: Mapped[str] = mapped_column(String(25))
    nuevo_contador: Mapped[int]
    fecha: Mapped[date]
    diferencia: Mapped[int]
    impresora_id: Mapped[int] = mapped_column(ForeignKey("impresora.id"))
    toner_id: Mapped[int] = mapped_column(ForeignKey("toner.id"))
    
    impresora: Mapped["Impresora"] = relationship(back_populates="entregas")
    toner: Mapped["Toner"] = relationship(back_populates="tentregas")