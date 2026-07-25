from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from core.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(15), unique=True, index=True)
    email = Column(String, unique=True, nullable=True)
    hashed_password = Column(String)
    full_name = Column(String)
    role = Column(String, default="customer") # customer, supermarket_admin, super_admin, rider
    is_active = Column(Boolean, default=True)
    supermarket_id = Column(Integer, ForeignKey("supermarkets.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
