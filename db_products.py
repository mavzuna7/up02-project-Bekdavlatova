"""Каталог электроники из PostgreSQL."""

import psycopg
from config import DB_CONFIG

def get_all_products():
    """Получить все товары."""
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, бренд, модель, озу,
                       цена, количество, изображение
                FROM "Товар"
                ORDER BY id
            """)
            return cur.fetchall()

def get_products_by_brand(brand):
    """Найти товары выбранного бренда."""
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, бренд, модель, озу,
                       цена, количество, изображение
                FROM "Товар"
                WHERE бренд = %s
                ORDER BY id
            """, (brand,))
            return cur.fetchall()

def get_products_low_stock():
    """Найти товары с остатком 3 штуки или меньше."""
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, бренд, модель, озу,
                       цена, количество, изображение
                FROM "Товар"
                WHERE количество <= %s
                ORDER BY количество
            """, (3,))
            return cur.fetchall()

def get_brands():
    """Получить список брендов."""
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT DISTINCT бренд
                FROM "Товар"
                ORDER BY бренд
            """)
            return [row[0] for row in cur.fetchall()]

def print_catalog(products):
    """Вывести каталог с остатками."""
    print("\n" + "=" * 55)
    print(f"КАТАЛОГ ЭЛЕКТРОНИКИ: {len(products)} товаров")
    print("=" * 55)

    for p in products:
        product_id, brand, model, ram, price, qty, image = p

        indicator = "много" if qty > 5 else "мало"
        warning = "ВНИМАНИЕ! " if qty <= 3 else ""

        print(f"{warning}{brand} {model}")
        print(f"Цена: {price:.0f} руб.")
        print(f"ОЗУ: {ram} ГБ")
        print(f"Остаток: {qty} шт. ({indicator})")
        print("-" * 40)

    print("=" * 55)

if __name__ == "__main__":
    print("1. Все товары")
    print_catalog(get_all_products())

    print("\n2. Бренды в каталоге:")
    for brand in get_brands():
        print("-", brand)

    print("\n3. Товары с низким остатком:")
    print_catalog(get_products_low_stock())

    print("\n4. Товары бренда Apple:")
    print_catalog(get_products_by_brand("Apple"))