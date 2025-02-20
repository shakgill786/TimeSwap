from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from database import Base, engine
from routers import products, reviews, cart, wishlist, search, auth

# Initialize FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Define OAuth2 security scheme for Swagger UI authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])
app.include_router(cart.router, prefix="/cart", tags=["Shopping Cart"])
app.include_router(wishlist.router, prefix="/wishlist", tags=["Wishlist"])
app.include_router(search.router, prefix="/search", tags=["Search"])

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to TimeSwap - The Barter Marketplace!"}
