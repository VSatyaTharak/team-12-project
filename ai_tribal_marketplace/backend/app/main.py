from fastapi import FastAPI
from .routes import router
from .database import engine, Base

app = FastAPI(title="AI Tribal Marketplace")

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "AI Tribal Arts Marketplace Running"}