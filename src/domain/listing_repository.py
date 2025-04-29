# src/domain/listing_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.listing import Listing
import uuid

class ListingRepository(ABC):

    def get_by_id(self, listing_id: uuid.UUID) -> Listing:
        raise NotImplementedError

    def get_all(self) -> List[Listing]:
        raise NotImplementedError

    def create(self, listing: Listing) -> Listing:
        return NotImplementedError

    def update(self, listing: Listing):
        raise NotImplementedError

    def delete(self, listing: Listing):
        raise NotImplementedError