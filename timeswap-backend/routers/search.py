from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

@router.get("/")
def search_products(query: str, db: Session = Depends(get_db)):
    return db.query(models.Product).filter(models.Product.title.contains(query)).all()
