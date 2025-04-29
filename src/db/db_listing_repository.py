# src/db/db_listing_repository.py
from typing import List
from sqlalchemy.orm import Session
import uuid

from db.listing_record import ListingRecord
from domain.listing import Listing

class DBListingRepository:

    def __init__(self, session: Session):
        self.__session = session

    @staticmethod
    def to_domain(listing_record: ListingRecord) -> Listing:
        return Listing(
            id=listing_record.id,
            name=listing_record.name or listing_record.link,
            link=listing_record.link,
            agency=None
        )

    def get_by_id(self, listing_id: uuid.UUID) -> Listing:
        listing_record = self.__session.query(ListingRecord).filter(ListingRecord.id == listing_id).first()
        return DBListingRepository.to_domain(listing_record) if listing_record else None

    def get_all(self) -> List[Listing]:
        listing_records = self.__session.query(ListingRecord).all()
        return [DBListingRepository.to_domain(record) for record in listing_records]