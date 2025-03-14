from src.database.firebase_config import db
import time


def add_book(title, author, pages, year):
    """
    Adiciona um novo livro ao Firebase Realtime Database.
    """
    try:
        book_data = {
            "title": title,
            "author": author,
            "pages": int(pages),
            "year": int(year)
        }
        db.child("books").push(book_data)
        return True
    except Exception as e:
        print(f"Erro ao adicionar livro: {str(e)}")
        return False


def get_books():
    """
    Retorna todos os livros cadastrados no Firebase e o tempo de consulta.
    """
    try:
        start_time = time.time()
        books = db.child("books").get().val()
        end_time = time.time()

        elapsed_time = end_time - start_time

        return {
            "books": books if books else {},
            "query_time": elapsed_time
        }
    except Exception as e:
        print(f"Erro ao buscar livros: {str(e)}")
        return {
            "books": {},
            "query_time": None
        }


def update_book(book_id, title, author, pages, year):
    try:
        db.child("books").child(book_id).update({
            "title": title,
            "author": author,
            "pages": int(pages),
            "year": int(year)
        })
        return True
    except Exception as e:
        print(f"Erro ao atualizar livro: {e}")
        return False


def delete_book(book_id):
    try:
        db.child("books").child(book_id).remove()
        return True
    except Exception as e:
        print(f"Erro ao excluir livro: {e}")
        return False
