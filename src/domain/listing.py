from datetime import date
from enum import Enum
from typing import Optional
from uuid import UUID

class Listing:

    class Status(Enum):
        PENDING = "PENDING"
        EXPIRED = "EXPIRED"
        RESERVED = "RESERVED"
        REJECTED = "REJECTED"

    class Coordinates:

        def __init__(self, latitude: float, longitude: float):
            self.__latitude = latitude
            self.__longitude = longitude

        @property
        def latitude(self):
            return self.__latitude
        
        @property
        def longitude(self):
            return self.__longitude
        
    class Availability:

        def __init__(self, start: date, end: date):
            self.__start = start
            self.__end = end

        @property
        def start(self) -> date:
            return self.__start

        @property
        def end(self) -> date:
            return self.__end

    def __init__(self, coordinates: Coordinates, availability: Availability, bedrooms: int, bathrooms: int, size: int, price: int, status: Status = None, id: UUID = None, link: str = None):
        self.__id = id
        self.__link = link
        self.__coordinates = coordinates
        self.__availability = availability
        self.__bedrooms = bedrooms
        self.__bathrooms = bathrooms
        self.__size = size
        self.__price = price
        self.__status = status or Listing.Status.PENDING

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def link(self) -> str:
        return self.__link
    
    @property
    def status(self) -> Status:
        return self.__status
    
    @property
    def bedrooms(self) -> int:
        return self.__bedrooms

    @property
    def bathrooms(self) -> int:
        return self.__bathrooms

    @property
    def size(self) -> int:
        return self.__size

    @property
    def price(self) -> int:
        return self.__price

    @property
    def coordinates(self) -> Coordinates:
        return self.__coordinates
    
    @property
    def availability(self) -> Availability:
        return self.__availability
    
    def with_link(self, link: str) -> "Listing":
        return Listing(
            id=self.id,
            link=link,
            coordinates=self.coordinates,
            availability=self.availability,
            bedrooms=self.bedrooms,
            bathrooms=self.bathrooms,
            size=self.size,
            price=self.price,
            status=self.status
        )