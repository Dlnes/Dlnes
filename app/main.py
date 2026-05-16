import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import Depends, FastAPI, Request, HTTPException
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager

from app.api.categories import router as categories
from app.api.books import router as books
from app.db.db import SessionLocal, engine
from app.db import models, crud
from app import schemas
import logging

logger = logging.getLogger("uvicorn.error")

app = FastAPI()

app.include_router(categories)
app.include_router(books)

@app.get("/health", tags=["Статус сервера"])
def health_check():
    return {
        "status": "healthy",
        "database": "connected",
    }

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001, reload=True)

# def display_store_data():
#     db = SessionLocal()
#     try:
#         print("Категории книг")
#         categories = get_categories(db)
#         if not categories:
#             print("  Категории отсутствуют.")
#         else:
#             for cat in categories:
#                 print(f"  • ID: {cat.id} | Название: {cat.title}")

#         print("Книги")
#         books = get_books(db)
#         if not books:
#             print("Нет книг")
#         else:
#             for book in books:
#                 print(f"ID: {book.id}")
#                 print(f"  Название:  {book.title}")
#                 print(f"  Описание:  {book.description}")
#                 print(f"  Цена:      {book.price} руб.")
#                 print(f"  Ссылка:    {book.url}")
#                 print(f"  Категория: {book.categories.title}")
#                 print("-" * 40)

#     except Exception as e:
#         print(f"Read error: {e}")
#     finally:
#         db.close()

# if __name__ == "__main__":
#     display_store_data()