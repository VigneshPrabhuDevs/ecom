from fastapi import APIRouter

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.get("/")
def get_cart():
  return {"message": "Cart endpoint placeholder"}