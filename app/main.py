import os
import sys

from db.db import SessionLocal
from db.models import Category, Book
from db.crud import get_categories, get_books

def display_store_data():
    db = SessionLocal()
    try:
        print("Категории книг")
        categories = get_categories(db)
        if not categories:
            print("  Категории отсутствуют.")
        else:
            for cat in categories:
                print(f"  • ID: {cat.id} | Название: {cat.title}")

        print("Книги")
        books = get_books(db)
        if not books:
            print("Нет книг")
        else:
            for book in books:
                print(f"ID: {book.id}")
                print(f"  Название:  {book.title}")
                print(f"  Описание:  {book.description}")
                print(f"  Цена:      {book.price} руб.")
                print(f"  Ссылка:    {book.url}")
                print(f"  Категория: {book.categories.title}")
                print("-" * 40)

    except Exception as e:
        print(f"Read error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    display_store_data()