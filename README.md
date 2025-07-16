# Retail Payment & Tax Compliance Service

FastAPI microservice simulating Stripe payment processing, tax calculation, and compliance logging.

## Setup
1. Copy `.env.example` to `.env` and update credentials.
2. Run locally:
```bash
docker-compose up --build
```
3. Visit [http://localhost:8000/docs](http://localhost:8000/docs).

## Flow
- Create Merchant → POST /merchants
- Add Product → POST /products
- Process Payment → POST /payments
