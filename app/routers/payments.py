from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import schemas, orm_models
from app.models.database import get_db
from app.services import stripe_service, tax_service, audit_logger
from app.utils.idempotency import check_idempotency

router = APIRouter()

@router.post("/")
def process_payment(request: schemas.PaymentCreate, db: Session = Depends(get_db)):
    if check_idempotency(request.idempotency_key):
        raise HTTPException(status_code=400, detail="Duplicate payment attempt.")

    product = db.query(orm_models.Product).filter(orm_models.Product.id == request.product_id).first()
    merchant = db.query(orm_models.Merchant).filter(orm_models.Merchant.id == request.merchant_id).first()

    if not product or not merchant:
        raise HTTPException(status_code=404, detail="Product or Merchant not found.")

    tax = tax_service.calculate_tax(product.price, merchant.country)
    total = product.price + tax

    intent = stripe_service.create_payment_intent(total)
    payment = orm_models.Payment(
        merchant_id=merchant.id,
        product_id=product.id,
        amount=product.price,
        tax=tax,
        status="PENDING",
        stripe_payment_id=intent["id"],
    )
    db.add(payment)
    db.commit()

    audit_logger.log_action("PAYMENT_INITIATED", f"Payment ID: {intent['id']}, Total: {total}")
    return {"payment_id": intent["id"], "client_secret": intent["client_secret"], "amount": total}
