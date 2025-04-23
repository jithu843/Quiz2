# Quiz2

Employee Data Generator API (FastAPI)

This project is a 3-hour backend challenge to simulate employee data, store it in PostgreSQL, and visualize it via APIs.

## Setup Instructions

1. **Clone Repo**
git clone <https://github.com/jithu843/Quiz2>

2. Install Dependencies
pip install -r requirements.txt

3. Configure .env
DATABASE_URL=postgresql://user:password@localhost:5432/employee_db

4. Run the App
uvicorn app.main:app --reload
