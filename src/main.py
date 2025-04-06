from fastapi import FastAPI

app = FastAPI(
    title="Home Hunt API",
    description="A FastAPI application for home hunting",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to Home Hunt API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 