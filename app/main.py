from fastapi import APIRouter, FastAPI

from app.cart.router import router as cart_router
from app.payments.router import router as payments_router
from app.products.router import router as products_router
from app.users.router import router as users_router

app = FastAPI(
    title="E-Commerce API Service",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Central API Router for versioning
api_router = APIRouter(prefix="/api/v1")

# Mount Domain Routers
api_router.include_router(users_router)
api_router.include_router(products_router)
api_router.include_router(cart_router)
api_router.include_router(payments_router)

# Mount Central Router into the App
app.include_router(api_router)


@app.get("/health", tags=["Health"])
def health_check():
  return {"status": "healthy"}


if __name__ == "__main__":
  import uvicorn

  uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)