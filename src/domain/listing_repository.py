# src/domain/listing_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.listing import Listing
import uuid

class ListingRepository(ABC):

    @abstractmethod
    def get_by_id(self, listing_id: uuid.UUID) -> Listing:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[Listing]:
        raise NotImplementedError

    @abstractmethod
    def create(self, listing: Listing) -> Listing:
        raise NotImplementedError

    @abstractmethod
    def update(self, listing: Listing):
        raise NotImplementedError

    @abstractmethod
    def delete(self, listing: Listing):
        raise NotImplementedError