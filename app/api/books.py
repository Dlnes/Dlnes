from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

# Локальные импорты проекта
from app import schemas
from app.db.db import get_db
from app.db import crud

router = APIRouter(prefix="/books", tags=["Книги"])


@router.get("/", response_model=list[schemas.BookOut], status_code=200)
def read_books(category_id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if category_id is not None:
        db_category = crud.get_category(db, category_id=category_id)
        if not db_category:
            raise HTTPException(status_code=404, detail="Указанная категория не найдена")
    
    db_books = crud.get_books(db=db, skip=skip, limit=limit)
    
    result = []
    for book in db_books:
        if book.category:
            book.category_name = book.category.title
            
        if category_id is not None:
            if book.category == category_id:
                result.append(book)
        else:
            result.append(book)
            
    return result


@router.get("/{book_id}", response_model=schemas.BookOut, status_code=200)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db=db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
        
    if db_book.category:
        book.category_name = db_book.category.title
    return db_book


@router.post("/", response_model=schemas.BookOut, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=book.category_id)
    if not db_category:
        raise HTTPException(status_code=400, detail=f"Категория с ID {book.category_id} не существует")

    db_book = crud.create_book(
        db=db,
        title=book.title,
        price=book.price,
        category_id=book.category_id,
        description=book.description,
        url=book.url
    )
    db_book.category_name = db_category.title
    return db_book


@router.put("/{book_id}", response_model=schemas.BookOut, status_code=200)
def update_book(book_id: int, book_data: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.get_book(db=db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
        
    db_category = crud.get_category(db, category_id=book_data.category_id)
    if not db_category:
        raise HTTPException(status_code=400, detail=f"Категория с ID {book_data.category_id} не существует")
        
    update_dict = book_data.model_dump()
    updated_book = crud.update_book(db=db, book_id=book_id, update_data=update_dict)
    updated_book.category_name = db_category.title
    return updated_book


@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    success = crud.delete_book(db=db, book_id=book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return Response(status_code=204)