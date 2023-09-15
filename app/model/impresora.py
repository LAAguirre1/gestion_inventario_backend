from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List, TYPE_CHECKING, Optional

from app.utils.base_class import Base

if TYPE_CHECKING:
    from .entrega import Entrega  # noqa: F401

class Impresora(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    impresora: Mapped[str] = mapped_column(String(50))
    num_serie: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    contador_copia: Mapped[int]
    sucursal: Mapped[str] = mapped_column(String(30))
    seccion: Mapped[str] = mapped_column(String(30))
    ultimo_mantenimiento: Mapped[Optional[date]]
    entregas: Mapped[List["Entrega"]] = relationship(back_populates="impresora", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Impresora(id={self.id!r}, num_serie={self.num_serie!r})"

