from fastapi import FastAPI
from src.routers import agency_router

app = FastAPI(
    title="Home Hunt API",
    description="A FastAPI application for home hunting",
    version="1.0.0"
)

app.include_router(agency_router.router)

"""
@app.get("/")
async def root():
    return {"message": "Welcome to Home Hunt API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 
"""