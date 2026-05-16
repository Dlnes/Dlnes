from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

# Локальные импорты проекта
from app import schemas
from app.db.db import get_db
from app.db import crud

router = APIRouter(prefix="/categories", tags=["Категории"])


@router.get("/", response_model=list[schemas.CategoryOut], status_code=200)
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_categories(db=db, skip=skip, limit=limit)


@router.get("/{category_id}", response_model=schemas.CategoryOut, status_code=200)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db=db, category_id=category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return db_category


@router.post("/", response_model=schemas.CategoryOut, status_code=201)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, title=category.title)


@router.put("/{category_id}", response_model=schemas.CategoryOut, status_code=200)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.update_category(db=db, category_id=category_id, new_title=category.title)
    if not db_category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return db_category


@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    success = crud.delete_category(db=db, category_id=category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return Response(status_code=204)