from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

@router.get("/")
def get_products(db: Session = Depends(get_db), query: str = None):
    if query:
        return db.query(models.Product).filter(models.Product.title.contains(query)).all()
    return db.query(models.Product).all()
