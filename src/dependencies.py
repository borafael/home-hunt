from fastapi import Depends

from db.db_agency_repository import DBAgencyRepository
from db.database import get_db
from domain.agency_repository import AgencyRepository
from domain.agency_service import AgencyService


def get_agency_repository(session = Depends(get_db)) -> AgencyRepository:
    return DBAgencyRepository(session)

def get_agency_service(agency_repository: AgencyRepository = Depends(get_agency_repository)):
    return AgencyService(agency_repository)