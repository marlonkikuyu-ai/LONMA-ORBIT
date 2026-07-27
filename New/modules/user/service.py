from sqlalchemy.orm import Session
from modules.user.model import User
from core.security import get_password_hash, verify_password

def get_user_by_phone(db: Session, phone: str):
    return db.query(User).filter(User.phone == phone).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, phone: str, password: str, full_name: str, role: str = "customer"):
    hashed_password = get_password_hash(password)
    db_user = User(phone=phone, hashed_password=hashed_password, full_name=full_name, role=role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, **kwargs):
    user = get_user_by_id(db, user_id)
    if not user: return None
    for key, value in kwargs.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def deactivate_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        user.is_active = False
        db.commit()
    return user
