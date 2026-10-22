from datetime import datetime
from discount import calculate_price_with_discount

class Product:
    """Класс Товар."""

    def __init__(self, product_id, brand, model, ram, price, quantity, image):
        self.id = product_id
        self.brand = brand
        self.model = model
        self.ram = ram
        self.price = price
        self.quantity = quantity
        self.image = image

    def total(self):
        """Общая стоимость всех единиц товара."""
        return self.price * self.quantity

    def price_with_discount(self, discount_percent):
        """Цена со скидкой в процентах."""
        return self.price * (1 - discount_percent / 100)

    def price_with_discount_auto(self, calculation_date=None):
        """Цена с автоматической скидкой по истории заказов."""
        if calculation_date is None:
            calculation_date = datetime.now()

        return calculate_price_with_discount(
            self.id, self.price, calculation_date
        )

    def indicator(self):
        """Оценка остатка товара."""
        return "много" if self.quantity > 5 else "мало"

    def is_available(self):
        """Есть ли товар в наличии."""
        return self.quantity > 0

    def info(self):
        """Информация о товаре."""
        return (
            f"{self.brand} {self.model}, ОЗУ: {self.ram} ГБ, "
            f"цена: {self.price:.2f} руб., "
            f"количество: {self.quantity}, "
            f"общая стоимость: {self.total():.2f} руб., "
            f"остаток: {self.indicator()}"
        )

class Order:
    """Класс Заказ."""

    def __init__(self, order_id, date, client, product, quantity):
        self.id = order_id
        self.date = date
        self.client = client
        self.product = product
        self.quantity = quantity

    def total(self):
        """Стоимость заказа."""
        return self.product.price * self.quantity

    def info(self):
        """Информация о заказе."""
        return (
            f"Заказ №{self.id} от {self.date}: "
            f"{self.client} — {self.product.brand} "
            f"{self.product.model} × {self.quantity}; "
            f"сумма: {self.total():.2f} руб."
        )


