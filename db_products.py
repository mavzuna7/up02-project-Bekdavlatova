"""Каталог электроники из PostgreSQL."""

import psycopg
from config import DB_CONFIG
from models import Product

def get_all_products():
    """Возвращает список всех товаров."""

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, бренд, модель, озу, цена, количество, изображение
                FROM "Товар"
                ORDER BY id
            """)
            rows = cur.fetchall()

    products = []

    for row in rows:
        product = Product(
            product_id=row[0],
            brand=row[1],
            model=row[2],
            ram=row[3],
            price=float(row[4]),
            quantity=row[5],
            image=row[6]
        )
        products.append(product)

    return products

def get_products_by_brand(brand):
    """Возвращает товары указанного бренда."""

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, бренд, модель, озу, цена, количество, изображение
                FROM "Товар"
                WHERE бренд = %s
                ORDER BY id
            """, (brand,))
            rows = cur.fetchall()

    return [
        Product(
            product_id=row[0],
            brand=row[1],
            model=row[2],
            ram=row[3],
            price=float(row[4]),
            quantity=row[5],
            image=row[6]
        )
        for row in rows
    ]

def get_products_low_stock():
    """Возвращает товары, которых осталось не больше трёх."""

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, бренд, модель, озу, цена, количество, изображение
                FROM "Товар"
                WHERE количество <= 3
                ORDER BY количество ASC
            """)
            rows = cur.fetchall()

    return [
        Product(
            product_id=row[0],
            brand=row[1],
            model=row[2],
            ram=row[3],
            price=float(row[4]),
            quantity=row[5],
            image=row[6]
        )
        for row in rows
    ]

def print_catalog(products):
    """Выводит каталог товаров."""

    print(f"\nКАТАЛОГ: {len(products)} товаров")
    print("=" * 90)

    for product in products:
        highlight = "ВНИМАНИЕ!" if product.quantity <= 3 else ""
        print(f"{highlight} {product.info()}")

    print("=" * 90)

if __name__ == "__main__":
    print("1. Все товары:")
    print_catalog(get_all_products())

    print("\n2. Товары бренда Samsung:")
    print_catalog(get_products_by_brand("Samsung"))

    print("\n3. Товары с низким остатком:")
    print_catalog(get_products_low_stock())





