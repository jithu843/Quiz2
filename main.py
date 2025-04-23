from fastapi import FastAPI
from app.routers import employee
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Employee API")

app.include_router(employee.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
