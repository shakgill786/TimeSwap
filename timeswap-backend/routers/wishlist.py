from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

@router.get("/")
def view_wishlist(db: Session = Depends(get_db)):
    return db.query(models.Wishlist).all()

@router.post("/{product_id}")
def add_to_wishlist(product_id: int, db: Session = Depends(get_db)):
    new_wishlist_item = models.Wishlist(product_id=product_id)
    db.add(new_wishlist_item)
    db.commit()
    return {"message": f"Product {product_id} added to wishlist"}

@router.delete("/{product_id}")
def remove_from_wishlist(product_id: int, db: Session = Depends(get_db)):
    db.query(models.Wishlist).filter(models.Wishlist.product_id == product_id).delete()
    db.commit()
    return {"message": f"Product {product_id} removed from wishlist"}
