from sqlalchemy import UUID, Column, ForeignKey, Integer, String, DateTime
import sqlalchemy
from sqlalchemy.sql import func
from db.database import Base

class ListingRecord(Base):
    __tablename__ = "listings"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, server_default=sqlalchemy.text("gen_random_uuid()"))
    name = Column(String, index=True)
    link = Column(String)
    agency_id = Column(UUID, ForeignKey("agencies.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())