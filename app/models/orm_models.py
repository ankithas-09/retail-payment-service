from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.models.database import Base

class Merchant(Base):
    __tablename__ = "merchants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    tax_id = Column(String, nullable=False)
    country = Column(String, nullable=False)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    merchant_id = Column(Integer, ForeignKey("merchants.id"))

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    merchant_id = Column(Integer, ForeignKey("merchants.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    amount = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)
    status = Column(String, default="PENDING")
    stripe_payment_id = Column(String, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    action = Column(String)
    details = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
