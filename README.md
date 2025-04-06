# Home Hunt

A FastAPI application for home hunting.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the database:
   - Create a PostgreSQL database named `homehunt`
   - Create a `.env` file with your database URL:
     ```
     DATABASE_URL=postgresql://user:password@localhost:5432/homehunt
     ```
   - Initialize the database migrations:
     ```bash
     alembic init alembic
     alembic revision --autogenerate -m "Initial migration"
     alembic upgrade head
     ```

## Running the Application

To run the application in development mode:
```bash
uvicorn src.main:app --reload
```

The API will be available at http://localhost:8000
API documentation will be available at http://localhost:8000/docs

## Running Tests

To run the tests, make sure to include the project root in the Python path:
```bash
PYTHONPATH=$PYTHONPATH:. pytest
```

## Database Migrations

To create a new migration:
```bash
alembic revision --autogenerate -m "Description of changes"
```

To apply migrations:
```bash
alembic upgrade head
```

To rollback the last migration:
```bash
alembic downgrade -1
```
