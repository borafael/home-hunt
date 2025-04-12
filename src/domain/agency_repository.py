from abc import ABC, abstractmethod
from typing import List
from domain.agency import Agency

class AgencyRepository(ABC):
    
    @abstractmethod
    def get_by_id(self, agency_id: int) -> Agency:
        raise Exception("Method not implemented")
    
    @abstractmethod
    def get_all(self) -> List[Agency]:
        raise Exception("Method not implemented")
    
    @abstractmethod
    def create(self, agency: Agency) -> Agency:
        raise Exception("Method not implemented")
    
    @abstractmethod
    def update(self, agency: Agency):
        raise Exception("Method not implemented")
    
    @abstractmethod
    def delete(self, agency: Agency):
        raise Exception("Method not implemented")