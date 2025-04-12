from src.db.agency_record import AgencyRecord

class Listing:

    def __init_(self, name: str, link: str, agency: AgencyRecord):
        self.__name = name
        self.__link = link
        self.__agency = agency

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def link(self) -> str:
        return self.__link
    
    @property
    def agency(self) -> AgencyRecord:
        return self.__agency