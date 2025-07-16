from app.models.database import SessionLocal
from app.models.orm_models import Payment

def check_idempotency(key: str):
    db = SessionLocal()
    payment = db.query(Payment).filter(Payment.stripe_payment_id == key).first()
    db.close()
    return payment
