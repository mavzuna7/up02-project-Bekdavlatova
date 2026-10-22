class Product:
    """Класс Товар."""

    def __init__(self, product_id, brand, model, ram, price, quantity, image):
        """Создаёт объект товара."""
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
        """Цена одной единицы товара со скидкой."""
        return self.price * (1 - discount_percent / 100)

    def indicator(self):
        """Показывает остаток товара на складе."""
        return "много" if self.quantity > 5 else "мало"

    def is_available(self):
        """Проверяет, есть ли товар в наличии."""
        return self.quantity > 0

    def info(self):
        """Возвращает информацию о товаре."""
        return (
            f"{self.brand} {self.model}, ОЗУ: {self.ram} ГБ, "
            f"цена: {self.price:.2f} руб., "
            f"количество: {self.quantity}, "
            f"общая стоимость: {self.total():.2f} руб., "
            f"остаток: {self.indicator()}"
        )