import sqlalchemy
from sqlalchemy import UUID, Column, String, DateTime
from sqlalchemy.sql import func
from db.database import Base

class AgencyRecord(Base):
    __tablename__ = "agencies"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, server_default=sqlalchemy.text("gen_random_uuid()"))
    name = Column(String, index=True)
    site = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 