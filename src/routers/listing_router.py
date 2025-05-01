# src/routers/listing_router.py
from typing import List, Optional
from uuid import UUID
import uuid
from fastapi import APIRouter, Depends, HTTPException, Response, status

from dependencies import get_listing_service
from domain.listing import Listing
from domain.listing_service import ListingCreationException, ListingService

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
    link: str
    status: str
    bedrooms: Optional[int]
    bathrooms: Optional[int]
    size: Optional[int]
    price: int
    coordinates: dict

class ListingCreatePayload(BaseModel):
    link: str

def domain_to_payload(listing: Listing) -> ListingPayload:
    return ListingPayload(
        id=listing.id,
        link=listing.link,
        status=listing.status.value,
        bedrooms=listing.bedrooms,
        bathrooms=listing.bathrooms,
        size=listing.size,
        price=listing.price,
        coordinates={
            "latitude": listing.coordinates.latitude,
            "longitude": listing.coordinates.longitude
        }
    )

@router.get("/", response_model=List[ListingPayload], status_code=status.HTTP_200_OK)
def get_listings(listing_service: ListingService = Depends(get_listing_service)):
    listings = listing_service.find_all()
    return [domain_to_payload(listing) for listing in listings]

@router.get("/{listing_id}", response_model=ListingPayload, status_code=status.HTTP_200_OK)
def get_listing(listing_id: UUID, listing_service: ListingService = Depends(get_listing_service)):
    listing = listing_service.find_by_id(listing_id)
    if listing:
        return domain_to_payload(listing)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Listing not found")
    
@router.post("/", response_model=ListingPayload, status_code=status.HTTP_201_CREATED)
async def create_listing(listing: ListingCreatePayload, listing_service: ListingService = Depends(get_listing_service)):

    try:
        created_listing = await listing_service.create(listing.link)
    except ListingCreationException as e:
        #not sure raising an HTTPException is right here, i am only using it to return a custom status and message
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))

    return domain_to_payload(created_listing)

@router.delete("/{listing_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_listing(listing_id: UUID, listing_service: ListingService = Depends(get_listing_service)):
    listing = listing_service.find_by_id(listing_id)
    if listing:
        listing_service.delete(listing)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Listing not found")

