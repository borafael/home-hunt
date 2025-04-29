from typing import Optional
from uuid import UUID
from db.agency_record import AgencyRecord
from domain.agency import Agency

class Listing:

    def __init__(self, link: str, id: Optional[UUID] = None, name: Optional[str] = None, agency: Optional[Agency] = None):
        self.__id = id
        self.__name = name
        self.__link = link
        self.__agency = agency

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def link(self) -> str:
        return self.__link
    
    @property
    def agency(self) -> Agency:
        return self.__agency