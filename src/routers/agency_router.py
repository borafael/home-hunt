from uuid import UUID
from fastapi import APIRouter, Depends, Response, status
from dependencies import get_agency_service
from domain.agency_service import AgencyService

from pydantic import BaseModel

router = APIRouter(
    prefix="/agencies",
    tags=["agencies"]
)

class AgencyPayload(BaseModel):
    id: UUID
    name: str
    site: str


@router.get("/", status_code=status.HTTP_200_OK)
def get_agencies(response: Response, agency_service: AgencyService = Depends(get_agency_service)):

    try:
        agencies = agency_service.find_all()
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return str(e)
        
    return [AgencyPayload(id=agency.id, name=agency.name, site=agency.site) for agency in agencies]