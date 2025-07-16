import stripe, os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_dummy")

def create_payment_intent(amount: float, currency="usd"):
    intent = stripe.PaymentIntent.create(
        amount=int(amount * 100),
        currency=currency,
        payment_method_types=["card"],
    )
    return intent
