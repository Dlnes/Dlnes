from db.db import engine, SessionLocal
from db.models import Base
from db.crud import create_category, create_book

def init_database():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        detective  = create_category(db, title="Detective")
        fantasy = create_category(db, title="Fantasy")
  
        create_book(
            db, 
            title="A Study in Scarlet", 
            description="Published in 1887, the story marks the first appearance of Sherlock Holmes and Dr. Watson, who would go on to become one of the most well-known detective duos in literature.",
            price=750.00, 
            category_id=detective.id,
        )
        create_book(
            db, 
            title="Murder on the Orient Express", 
            description="Mystery novel by English writer Agatha Christie featuring the Belgian detective Hercule Poirot.",
            price=680.50, 
            category_id=detective.id
        )

        create_book(
            db, 
            title="The Lord of the Rings", 
            description="Epic high fantasy novel written by the English author and scholar J.R.R.Tolkien",
            price=1200.00, 
            category_id=fantasy.id
        )
        create_book(
            db, 
            title="Harry Potter",
            description="The novels chronicle the lives of a young wizard, Harry Potter, and his friends, Ron Weasley and Hermione Granger, all of whom are students at Hogwarts School of Witchcraft and Wizardry.", 
            price=590.00, 
            category_id=fantasy.id 
        )
        create_book(
            db, 
            title="A Song of Ice and Fire", 
            description="A Song of Ice and Fire depicts a violent world dominated by political realism. What little supernatural power exists is confined to the margins of the known world.",
            price=2500.00, 
            category_id=fantasy.id 
        )
        create_book(
            db, 
            title="American Gods", 
            description="Fantasy novel by British author Neil Gaiman. The novel is a blend of Americana, fantasy, and various strands of ancient and modern mythology, all centering on the mysterious and taciturn Shadow.",
            price=560.00, 
            category_id=fantasy.id
        )

        print("Success")  
    except Exception as e:
        print(f"Произошла ошибка при заполнении БД: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_database()