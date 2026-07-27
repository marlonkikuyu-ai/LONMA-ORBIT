from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.db import get_db
from core.security import oauth2_scheme
from modules.user import service as user_service
from modules.user.model import User

router = APIRouter()

@router.get("/")
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_service.get_all_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
def update_user(user_id: int, full_name: str = None, address: str = None, db: Session = Depends(get_db)):
    update_data = {k: v for k, v in {"full_name": full_name, "address": address}.items() if v is not None}
    user = user_service.update_user(db, user_id, **update_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.deactivate_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"msg": "User deactivated"}
