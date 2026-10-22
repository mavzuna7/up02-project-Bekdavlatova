"""Тестирование алгоритма скидки."""

from datetime import datetime
from discount import (
    calculate_price_with_discount,
    get_previous_month_range
)

def run_tests():
    test_cases = [
        # product_id, price, date, expected, comment
        (1, 8500, datetime(2026, 10, 15), 8500,
         "Заказы есть в сентябре"),
        (2, 15000, datetime(2026, 10, 15), 11250,
         "Заказов нет в сентябре"),
        (3, 12000, datetime(2026, 10, 15), 12000,
         "Заказы есть в сентябре"),
        (4, 4500, datetime(2026, 10, 15), 3375,
         "Заказов нет в сентябре"),
        (5, 6000, datetime(2026, 10, 15), 4500,
         "Заказов нет в сентябре"),

        # Дополнительные проверки
        (2, 15000, datetime(2026, 11, 15), 15000,
         "Проверка заказов за октябрь"),
        (1, 8500, datetime(2026, 11, 15), 8500,
         "Проверка заказов за октябрь"),
        (4, 4500, datetime(2026, 9, 1), 3375,
         "Проверка заказов за август"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ")
    print("=" * 70)

    passed = 0

    for product_id, price, calc_date, expected, comment in test_cases:
        try:
            result = calculate_price_with_discount(
                product_id, price, calc_date
            )

            if result == expected:
                status = "OK"
                passed += 1
            else:
                status = "ОШИБКА"

            print(
                f"{status}: товар {product_id}, "
                f"дата {calc_date.date()}, "
                f"{price} -> {result}, "
                f"ожидалось {expected}. {comment}"
            )

        except Exception as error:
            print(
                f"ОШИБКА: товар {product_id}, "
                f"дата {calc_date.date()}: {error}"
            )

    # Отдельно проверяем определение предыдущего месяца
    date_tests = [
        (datetime(2026, 10, 1), datetime(2026, 9, 1),
         datetime(2026, 9, 30)),
        (datetime(2026, 10, 31), datetime(2026, 9, 1),
         datetime(2026, 9, 30)),
        (datetime(2027, 1, 1), datetime(2026, 12, 1),
         datetime(2026, 12, 31)),
    ]

    for calc_date, expected_start, expected_end in date_tests:
        start, end = get_previous_month_range(calc_date)

        if start == expected_start.date() and end == expected_end.date():
            print(f"OK: диапазон дат для {calc_date.date()}")
            passed += 1
        else:
            print(
                f"ОШИБКА: для {calc_date.date()} "
                f"получен диапазон {start} — {end}"
            )

    total = len(test_cases) + len(date_tests)
    print("=" * 70)
    print(f"Пройдено: {passed} из {total}")

if __name__ == "__main__":
    run_tests()





