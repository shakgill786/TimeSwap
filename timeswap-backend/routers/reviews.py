from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter()

@router.get("/{product_id}/")
def get_reviews(product_id: int, db: Session = Depends(get_db)):
    return db.query(models.Review).filter(models.Review.product_id == product_id).all()

@router.post("/{product_id}/")
def create_review(product_id: int, review: schemas.ReviewBase, db: Session = Depends(get_db)):
    new_review = models.Review(product_id=product_id, **review.dict())
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review
