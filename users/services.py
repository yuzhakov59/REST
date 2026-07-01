import stripe
from config.settings import STRIPE_KEY

stripe.api_key = STRIPE_KEY


def create_stripe_price(amount):

    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name": "Amount_lesson"},
    )

def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")