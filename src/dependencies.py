from fastapi import Depends

from src.db.agency_repository import DBAgencyRepository
from src.db.database import get_db
from src.domain.agency_repository import AgencyRepository
from src.domain.agency_service import AgencyService


def get_agency_repository(session = Depends(get_db)) -> AgencyRepository:
    return DBAgencyRepository(session)

def get_agency_service(agency_repository: AgencyRepository = Depends(get_agency_repository)):
    return AgencyService(agency_repository)