from src.database.firebase_config import db

def add_book(title, author, pages, year):
    """
    Adiciona um novo livro ao Firebase Realtime Database.
    """
    try:
        book_data = {
            "title": title,
            "author": author,
            "pages": pages,
            "year": year
        }
        db.child("books").push(book_data)
        return True
    except Exception as e:
        print(f"Erro ao adicionar livro: {str(e)}")
        return False