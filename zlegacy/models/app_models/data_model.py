
import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.database import Base


class DataModel(Base):
    __tablename__ = 'data'

    id: Mapped[uuid.UUID]  = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)

