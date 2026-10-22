"""Проверка подключения к PostgreSQL"""

import psycopg
from config import DB_CONFIG

def test_connection():
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT COUNT(*) FROM "Товар"')
                count = cur.fetchone()[0]

                print("ПОдключение к PostgreSQL установлено!")
                print(f"Товаров в базе: {count}")
            print("Соединение закрыто.")
        
    except psycopg.Error as error:
        print(f"Ошибка Подключения к БД: {error}")

if __name__ == "__main__":
    test_connection()
