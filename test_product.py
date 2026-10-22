"""Проверка класса Product."""

from models import Product

p = Product(
    product_id=1,
    brand="Xiaomi",
    model="Redmi Note 13",
    ram=8,
    price=25000,
    quantity=3,
    image=""
)

print(p.info())
print(f"Со скидкой 25%: {p.price_with_discount(25):.2f} руб.")
print(f"Есть в наличии: {p.is_available()}")


