from src.database.crud import add_book, get_books, update_book, delete_book
from PyQt5.QtWidgets import QMessageBox, QWidget, QLabel, QPushButton, QListWidgetItem, QHBoxLayout, QVBoxLayout, QInputDialog
from PyQt5.QtCore import QSize


class LibraryController:
    def __init__(self, main):
        self.main = main

    def add_book(self):
        """
        Obtém os dados da interface e adiciona um livro no Firebase.
        """
        title = self.main.signupBooksWindow.line_titulo.text().strip()
        author = self.main.signupBooksWindow.line_autor.text().strip()
        pages = self.main.signupBooksWindow.line_Qpaginas.text().strip()
        year = self.main.signupBooksWindow.line_publicacao.text().strip()

        if not (title == '' or author == '' or pages == '' or year == ''):
            if pages.isdigit() and year.isdigit():
                books_data = get_books()
                books = books_data.get("books", {})

                for book_id, book_data in books.items():
                    if (
                        book_data.get("title", "").strip().lower() == title.lower() and
                        book_data.get("author", "").strip().lower() == author.lower() and
                        str(book_data.get("pages", "")).strip() == str(pages) and
                        str(book_data.get("year", "")).strip() == str(year)
                    ):
                        QMessageBox.warning(None, 'Erro', 'Este livro já está cadastrado.')
                        return
                if add_book(title, author, int(pages), int(year)):
                    QMessageBox.information(None, 'Sucesso', 'Livro adicionado com sucesso')
                    self.main.signupBooksWindow.line_titulo.setText('')
                    self.main.signupBooksWindow.line_autor.setText('')
                    self.main.signupBooksWindow.line_Qpaginas.setText('')
                    self.main.signupBooksWindow.line_publicacao.setText('')
                else:
                    QMessageBox.warning(None, 'Erro', 'Erro ao adiconar livro')
            else:
                QMessageBox.warning(None, 'Erro', 'Os campos "Ano" e "Quantidade de Páginas" devem conter apenas números inteiros.')
        else:
            QMessageBox.warning(None, 'Erro', 'Todos os dados devem estar preenchidos!')

    def load_books(self):
        """
        Carrega os livros na interface com rolagem e adiciona botões de edição e exclusão.
        """
        books_data = get_books()
        books = books_data.get("books", {})
        query_time = books_data.get("query_time", None)

        QMessageBox.information(None, 'Sucesso', f'A consulta para carregar todos os livros levou {query_time:.4f} segundos.')
        self.main.searchBooksWindow.listWidget.clear()
        self._populate_book_list(books)

    def search_books(self):
        """
        Realiza a pesquisa diretamente no controller com base nos campos preenchidos.
        """
        title_query = self.main.searchBooksWindow.line_titulo.text().strip().lower()
        author_query = self.main.searchBooksWindow.line_autor.text().strip().lower()
        year_query = self.main.searchBooksWindow.line_publicacao.text().strip()
        pages_query = self.main.searchBooksWindow.line_Qpaginas.text().strip()

        books_data = get_books()
        books = books_data.get("books", {})

        results = {}

        for book_id, book_data in books.items():
            title = str(book_data.get("title", "")).strip().lower()
            author = str(book_data.get("author", "")).strip().lower()
            year = str(book_data.get("year", "")).strip()
            pages = str(book_data.get("pages", "")).strip()

            if (
                (not title_query or title_query in title) and
                (not author_query or author_query in author) and
                (not year_query or year_query == year) and
                (not pages_query or pages_query == pages)
            ):
                results[book_id] = book_data

        self.main.searchBooksWindow.listWidget.clear()
        self._populate_book_list(results)

    def _populate_book_list(self, books):
        """
        Popula a lista de livros com botões de edição e exclusão.
        """
        for book_id, book_data in books.items():
            book_widget = QWidget()
            main_layout = QVBoxLayout()
            info_layout = QVBoxLayout()
            buttons_layout = QHBoxLayout()

            book_info = QLabel(
                f"Título: {book_data['title']}\n"
                f"Autor: {book_data['author']}\n"
                f"Ano: {book_data['year']}\n"
                f"Páginas: {book_data['pages']}"
            )

            edit_button = QPushButton("✏️ Editar")
            edit_button.clicked.connect(lambda _, bid=book_id: self.edit_book(bid))

            delete_button = QPushButton("🗑️ Excluir")
            delete_button.clicked.connect(lambda _, bid=book_id: self.delete_book(bid))

            info_layout.addWidget(book_info)
            buttons_layout.addWidget(edit_button)
            buttons_layout.addWidget(delete_button)

            main_layout.addLayout(info_layout)
            main_layout.addLayout(buttons_layout)

            book_widget.setLayout(main_layout)

            item = QListWidgetItem(self.main.searchBooksWindow.listWidget)
            altura = book_widget.sizeHint().height() + 20
            largura = book_widget.sizeHint().width()
            item.setSizeHint(QSize(largura, altura))
            self.main.searchBooksWindow.listWidget.addItem(item)
            self.main.searchBooksWindow.listWidget.setItemWidget(item, book_widget)

    def edit_book(self, book_id):
        """
        Edita um livro existente.
        """
        books_data = get_books()
        books = books_data.get("books", {})
        book_data = books.get(book_id, None)
        if not book_data:
            QMessageBox.warning(None, 'Erro', 'Não foi possível carregar os dados atualizados do livro.')
            return

        while True:
            new_title, ok1 = QInputDialog.getText(None, "Editar Livro", "Novo título:", text=book_data['title'])
            if ok1:
                if new_title == '':
                    QMessageBox.warning(None, 'Erro', 'O título não pode estar em branco.')
                else:
                    break
            else:
                return

        while True:
            new_author, ok2 = QInputDialog.getText(None, "Editar Livro", "Novo autor:", text=book_data['author'])
            if ok2:
                if new_author == '':
                    QMessageBox.warning(None, 'Erro', 'O autor não pode estar em branco.')
                else:
                    break
            else:
                return

        while True:
            new_year, ok3 = QInputDialog.getText(None, "Editar Livro", "Novo ano de publicação:", text=str(book_data['year']))
            if ok3:
                if new_year == '':
                    QMessageBox.warning(None, 'Erro', 'O ano de publicação não pode estar em branco.')
                else:
                    break
            else:
                return
        while True:
            new_pages, ok4 = QInputDialog.getText(None, "Editar Livro", "Nova quantidade de páginas:", text=str(book_data['pages']))
            if ok4:
                if new_pages == '':
                    QMessageBox.warning(None, 'Erro', 'A quantidade de páginas não pode estar em branco.')
                else:  
                    break
            else:
                return

        new_title = new_title.strip()
        new_author = new_author.strip()
        new_year = new_year.strip()
        new_pages = new_pages.strip()

        if new_year.isdigit() and new_pages.isdigit():
            success = update_book(book_id, new_title, new_author, int(new_pages), int(new_year))
            if success:
                QMessageBox.information(None, 'Sucesso', 'Livro atualizado com sucesso')
                self.load_books()
            else:
                QMessageBox.warning(None, 'Erro', 'Erro ao atualizar livro')
        else:
            QMessageBox.warning(None, 'Erro', 'Os campos "Ano" e "Quantidade de Páginas" devem conter apenas números inteiros.')

    def delete_book(self, book_id):
        """
        Exclui um livro do Firebase.
        """
        reply = QMessageBox.question(None, 'Confirmar Exclusão', 'Tem certeza que deseja excluir este livro?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            success = delete_book(book_id)
            if success:
                QMessageBox.information(None, 'Sucesso', 'Livro excluído com sucesso')
                self.load_books()
            else:
                QMessageBox.warning(None, 'Erro', 'Erro ao excluir livro')
