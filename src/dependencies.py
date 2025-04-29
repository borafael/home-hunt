from fastapi import Depends

from db.db_agency_repository import DBAgencyRepository
from db.database import get_db
from db.db_listing_repository import DBListingRepository
from domain.agency_repository import AgencyRepository
from domain.agency_service import AgencyService
from domain.listing_repository import ListingRepository
from domain.listing_service import ListingService


def get_agency_repository(session = Depends(get_db)) -> AgencyRepository:
    return DBAgencyRepository(session)

def get_listing_repository(session = Depends(get_db)) -> ListingRepository:
    return DBListingRepository(session)

def get_agency_service(agency_repository: AgencyRepository = Depends(get_agency_repository)):
    return AgencyService(agency_repository)

def get_listing_service(listing_repository: ListingRepository = Depends(get_listing_repository)):
    return ListingService(listing_repository)