# src/routers/listing_router.py
from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Response, status

from dependencies import get_listing_service
from domain.listing import Listing
from domain.listing_service import ListingService
from domain.agency import Agency  # Import Agency for request/response models

from pydantic import BaseModel

router = APIRouter(
    prefix="/listings",
    tags=["listings"]
)

class AgencyPayload(BaseModel):  # Re-use or create a common model if needed
    id: UUID
    name: str
    site: str

class ListingPayload(BaseModel):
    id: UUID
    name: str
    link: str
    agency: Optional[AgencyPayload] | None  # Agency details embedded in the response

class ListingCreatePayload(BaseModel):
    link: str

@router.get("/", response_model=List[ListingPayload], status_code=status.HTTP_200_OK)
def get_listings(listing_service: ListingService = Depends(get_listing_service)):
    listings = listing_service.find_all()
    return [
        ListingPayload(
            id=listing.id,
            name=listing.name,
            link=listing.link,
            agency=AgencyPayload(id=listing.agency.id, name=listing.agency.name, site=listing.agency.site) if listing.agency else None
        )
        for listing in listings
    ]

@router.get("/{listing_id}", response_model=ListingPayload, status_code=status.HTTP_200_OK)
def get_listing(listing_id: UUID, listing_service: ListingService = Depends(get_listing_service)):
    listing = listing_service.find_by_id(listing_id)
    if listing:
        return ListingPayload(
            id=listing.id,
            name=listing.name,
            link=listing.link,
            agency=AgencyPayload(id=listing.agency.id, name=listing.agency.name, site=listing.agency.site) if listing.agency else None
        )
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Listing not found")
    
@router.post("/", response_model=ListingPayload, status_code=status.HTTP_201_CREATED)
def create_listing(listing: ListingCreatePayload, listing_service: ListingService = Depends(get_listing_service)):
    new_listing = Listing(link=listing.link)
    created_listing = listing_service.create(new_listing)
    return ListingPayload(
        id=created_listing.id,
        name=created_listing.name,
        link=created_listing.link,
        agency=None
    )

@router.delete("/{listing_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_listing(listing_id: UUID, listing_service: ListingService = Depends(get_listing_service)):
    listing = listing_service.find_by_id(listing_id)
    if listing:
        listing_service.delete(listing)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Listing not found")

