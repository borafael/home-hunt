# src/db/db_listing_repository.py
from typing import List
from sqlalchemy.orm import Session
import uuid

from db.listing_record import ListingRecord
from domain.listing import Listing
from domain.listing_repository import ListingRepository

class DBListingRepository(ListingRepository):

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
    
    def create(self, listing: Listing) -> Listing:
        new_listing = ListingRecord(
            link=listing.link
        )
        self.__session.add(new_listing)
        self.__session.commit()
        return DBListingRepository.to_domain(new_listing)
    
    def delete(self, listing: Listing) -> None:
        listing_record = self.__session.query(ListingRecord).filter(ListingRecord.id == listing.id).first()
        if listing_record:
            self.__session.delete(listing_record)
            self.__session.commit()