from typing import List

from fastapi import Depends
from src.db.agency import AgencyRecord
from src.domain.agency import Agency
from src.db.database import get_db

class AgencyRepository:
    
    def __init__(self, session):
        self.__session = session

    def get_by_id(self, agency_id: int) -> Agency:
        return self.__session.query(AgencyRecord).filter(AgencyRecord.id == agency_id).first()
    
    def get_all(self) -> List[Agency]:
        print(self.__session)
        print(type(self.__session))
        return [Agency(agency_record.id, agency_record.name, agency_record.site) for agency_record in self.__session.query(AgencyRecord).all()]
    
    def create(self, agency: Agency) -> Agency:
        agency_record = AgencyRecord(name=agency.name, site=agency.site)
        self.__session.add(agency_record)
        self.__session.commit()
        self.__session.refresh(agency_record)
        return Agency(agency_record.id, agency_record.name, agency_record.site)
    
    def update(self, agency: Agency):
        agency_record = self.get_by_id(agency_id=agency.id)

        if not agency_record:
            raise Exception(f"Agency with id {agency.id} not found")
        
        raise Exception("Update is not implemented yet")
    
    def delete(self, agency: Agency):
        agency_record = self.get_by_id(agency_id=agency.id)

        if not agency_record:
            raise Exception(f"Agency with id {agency.id} not found")
        
        raise Exception("Delete is not implemented yet")