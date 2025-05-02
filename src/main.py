import re
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routers import agency_router, listing_router

app = FastAPI(
    title="Home Hunt API",
    description="A FastAPI application for home hunting",
    version="1.0.0"
)

# Define the origins that should be allowed to make requests
origins = [
#    "http://localhost",          # For local development (if your frontend is served on localhost)
    "http://localhost:8000"     # If your frontend is served on the same port as your API
 #   "https://your-deployed-frontend-domain.com", # If you deploy your frontend separately
 #   "*",                         # WARNING: Allows all origins - use with caution in production
]

# Add the CORSMiddleware to your application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],         # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],         # Allows all HTTP headers
)

app.include_router(agency_router.router)
app.include_router(listing_router.router)
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("../frontend/index.html", "r") as f:
        html_content = f.read()
    return html_content