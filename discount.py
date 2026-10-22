"""Алгоритм расчёта скидки для каталога электроники."""

from datetime import date, datetime, timedelta

import psycopg
from config import DB_CONFIG

def get_previous_month_range(calculation_date):
    """Возвращает первый и последний день предыдущего месяца."""

    first_day = calculation_date.replace(day=1)
    last_day = first_day - timedelta(days=1)
    start_day = last_day.replace(day=1)

    return start_day, last_day

def has_orders_in_previous_month(product_id, calculation_date):
    """Проверяет, были ли заказы товара в предыдущем месяце."""

    start_date, end_date = get_previous_month_range(calculation_date)

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT EXISTS (
                    SELECT 1
                    FROM "Заказ"
                    WHERE товар_id = %s
                      AND "дата"::date BETWEEN %s AND %s
                )
            """, (product_id, start_date, end_date))

            return cur.fetchone()[0]

def calculate_price_with_discount(product_id, price, calculation_date):
    """Возвращает цену с учётом скидки 25%."""

    if has_orders_in_previous_month(product_id, calculation_date):
        return round(float(price), 2)

    return round(float(price) * 0.75, 2)



