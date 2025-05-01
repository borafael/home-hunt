import re
from fastapi import FastAPI
from common.http_client import HttpClient, HttpResponse
from routers import agency_router, listing_router

app = FastAPI(
    title="Home Hunt API",
    description="A FastAPI application for home hunting",
    version="1.0.0"
)

app.include_router(agency_router.router)
app.include_router(listing_router.router)