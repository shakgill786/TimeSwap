from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

@router.get("/")
def view_cart(db: Session = Depends(get_db)):
    return db.query(models.Cart).all()

@router.post("/{product_id}")
def add_to_cart(product_id: int, db: Session = Depends(get_db)):
    new_cart_item = models.Cart(product_id=product_id)
    db.add(new_cart_item)
    db.commit()
    return {"message": f"Product {product_id} added to cart"}

@router.delete("/{product_id}")
def remove_from_cart(product_id: int, db: Session = Depends(get_db)):
    db.query(models.Cart).filter(models.Cart.product_id == product_id).delete()
    db.commit()
    return {"message": f"Product {product_id} removed from cart"}
