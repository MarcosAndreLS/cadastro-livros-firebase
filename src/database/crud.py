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
        start_time = time.time()  # Captura o tempo inicial
        books = db.child("books").get().val()
        end_time = time.time()  # Captura o tempo final
        
        elapsed_time = end_time - start_time  # Calcula o tempo decorrido
        
        return {
            "books": books if books else {},
            "query_time": elapsed_time  # Tempo da consulta em segundos
        }
    except Exception as e:
        print(f"Erro ao buscar livros: {str(e)}")
        return {
            "books": {},
            "query_time": None  # Indica falha na consulta
        }

def search_books(title_query="", author_query="", year_query="", pages_query=""):
    """
    Filtra os livros dinamicamente com base nos campos preenchidos.
    """
    books = get_books()
    results = {}

    for book_id, book_data in books.items():
        title = str(book_data.get("title", "")).strip().lower()
        author = str(book_data.get("author", "")).strip().lower()
        year = str(book_data.get("year", "")).strip()
        pages = str(book_data.get("pages", "")).strip()

        matches = (
            (not title_query or title_query in title) and
            (not author_query or author_query in author) and
            (not year_query or year_query == year) and
            (not pages_query or pages_query == pages)
        )

        if matches:
            results[book_id] = book_data

    return results

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