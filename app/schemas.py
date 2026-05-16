from pydantic import BaseModel, ConfigDict

class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class BookBase(BaseModel):
    title: str
    description: str | None = None
    price: float
    url: str | None = None
    category_id: int 

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)