from fastapi import FastAPI
from app.routers import payments, merchants, products
from app.models.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Retail Payment & Tax Compliance Service")

app.include_router(merchants.router, prefix="/merchants", tags=["Merchants"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}
