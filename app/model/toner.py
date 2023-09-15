from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List, TYPE_CHECKING

from app.utils.base_class import Base

if TYPE_CHECKING:
    from .entrega import Entrega  # noqa: F401

class Toner(Base):
    id: Mapped[int]= mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    descripcion: Mapped[str] = mapped_column(String(100))
    cantidad: Mapped[int] = mapped_column(default=0)
    tentregas: Mapped[List["Entrega"]] = relationship(back_populates="toner", cascade="all, delete-orphan")
    
    
    def __repr__(self) -> str:
        return f"Toner(id={self.id!r}, nombre={self.nombre!r}, descripcion={self.descripcion!r}, cantidad={self.cantidad!r})"
