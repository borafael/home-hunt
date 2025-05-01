from enum import Enum
from typing import Optional
from uuid import UUID
from db.agency_record import AgencyRecord
from domain.agency import Agency

class Listing:

    class Status(Enum):
        PENDING = "PENDING"
        EXPIRED = "EXPIRED"
        
    def __init__(self, id: UUID, link: str, status: Status = None):
        self.__id = id
        self.__link = link
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