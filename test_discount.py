from datetime import date

import psycopg
from config import DB_CONFIG
from discount import (
    get_previous_month_range,
    has_orders_in_previous_month,
    calculate_price_with_discount
)

def run_tests():
    calculation_date = date(2026, 10, 15)

    start, end = get_previous_month_range(calculation_date)

    print("=" * 65)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ")
    print(f"Проверяем период: {start} — {end}")
    print("=" * 65)

    passed = 0

    # Тест 1: проверяем границы предыдущего месяца.
    if start == date(2026, 9, 1) and end == date(2026, 9, 30):
        print("Тест 1: границы месяца — ПРОЙДЕН")
        passed += 1
    else:
        print("Тест 1: границы месяца — ОШИБКА")

    # Получаем первые пять товаров из настоящей базы.
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, бренд, модель, цена
                FROM "Товар"
                ORDER BY id
                LIMIT 5
            """)
            products = cur.fetchall()

    for product_id, brand, model, price in products:
        has_orders = has_orders_in_previous_month(
            product_id, calculation_date
        )

        expected = (
            round(float(price), 2)
            if has_orders
            else round(float(price) * 0.75, 2)
        )

        result = calculate_price_with_discount(
            product_id, price, calculation_date
        )

        if result == expected:
            passed += 1
            status = "ПРОЙДЕН"
        else:
            status = "ОШИБКА"

        print(
            f"Товар {product_id}: {brand} {model}; "
            f"цена {price}; результат {result}; {status}"
        )

    print("=" * 65)
    print(f"Пройдено проверок: {passed} из {1 + len(products)}")

if __name__ == "__main__":
    run_tests()


