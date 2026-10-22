from datetime import date
from models import Product

p = Product(
    product_id=2,
    brand="Xiaomi",
    model="Redmi Note 13",
    ram=8,
    price=15000,
    quantity=3,
    image=""
)

calculation_date = date(2026, 10, 15)

print(f"Базовая цена: {p.price:.2f} руб.")
print(
    "Цена с автоматической скидкой: "
    f"{p.price_with_discount_auto(calculation_date):.2f} руб."
)