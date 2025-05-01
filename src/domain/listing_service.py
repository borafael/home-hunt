import uuid

from httpx import HTTPError, InvalidURL
from common.http_client import HttpClient, HttpResponse
from domain.listing import Listing
from domain.listing_repository import ListingRepository
from crawl4ai import *
from typing import List

class ListingCreationException(Exception):

    def __init__(self, message: str):
        super().__init__(message)


class ListingService:

    def __init__(self, listing_repository: ListingRepository, http_client: HttpClient):
        self.__listing_repository = listing_repository
        self.__http_client = http_client

    def find_by_id(self, listing_id: uuid.UUID) -> Listing:
        return self.__listing_repository.get_by_id(listing_id)

    def find_all(self) -> List[Listing]:
        return self.__listing_repository.get_all()
    
    async def create(self, listing: Listing) -> Listing:
        status: Listing.Status = Listing.Status.PENDING

        try:
            response: HttpResponse = await self.__http_client.get(listing.link)
            if response.status < 200 or response.status >= 300:
                status = Listing.Status.EXPIRED

        except HTTPError as e:
            raise ListingCreationException(f"There was a problem with the URL {e}")
        except InvalidURL as e:
            raise ListingCreationException(f"Invalid URL {e}")

#        return self.__listing_repository.create(Listing(id=None, link=listing.link, status=status))
        return listing

    def update(self, listing: Listing):
        return self.__listing_repository.update(listing)

    def delete(self, listing: Listing):
        return self.__listing_repository.delete(listing)