import uuid
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List, Optional

from src.db.agency_repository import DBAgencyRepository
from src.db.database import get_db
from src.dependencies import get_agency_service
from src.domain.agency_service import AgencyService

from pydantic import BaseModel

router = APIRouter(
    prefix="/agencies",
    tags=["agencies"]
)

class AgencyPayload(BaseModel):
    id: int
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