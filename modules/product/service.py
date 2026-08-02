from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.db import get_db
from modules.order.service import create_order

router = APIRouter()

@router.post("/checkout")
def checkout(user_id: int, supermarket_id: int, items: list, address: str, phone: str, db: Session = Depends(get_db)):
    return create_order(db, user_id, supermarket_id, items, address, phone)
