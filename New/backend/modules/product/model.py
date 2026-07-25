from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from core.db import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    supermarket_id = Column(Integer, ForeignKey("supermarkets.id"))
    rider_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    total_amount = Column(Float)
    delivery_fee = Column(Float, default=150)
    status = Column(String, default="pending")
    delivery_address = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    price = Column(Float)
