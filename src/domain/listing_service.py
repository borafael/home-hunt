# src/domain/listing_service.py
from typing import List
import uuid

from common.http_client import HttpClient
from domain.listing import Listing
from domain.listing_repository import ListingRepository

class ListingService:

    def __init__(self, listing_repository: ListingRepository, http_client: HttpClient):
        self.__listing_repository = listing_repository
        self.__http_client = http_client

    def find_by_id(self, listing_id: uuid.UUID) -> Listing:
        return self.__listing_repository.get_by_id(listing_id)

    def find_all(self) -> List[Listing]:
        return self.__listing_repository.get_all()

    def create(self, listing: Listing) -> Listing:
        return self.__listing_repository.create(listing)

    def update(self, listing: Listing):
        return self.__listing_repository.update(listing)

    def delete(self, listing: Listing):
        return self.__listing_repository.delete(listing)