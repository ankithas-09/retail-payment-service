from pydantic import BaseModel

class MerchantCreate(BaseModel):
    name: str
    tax_id: str
    country: str

class ProductCreate(BaseModel):
    name: str
    price: float
    merchant_id: int

class PaymentCreate(BaseModel):
    merchant_id: int
    product_id: int
    idempotency_key: str
