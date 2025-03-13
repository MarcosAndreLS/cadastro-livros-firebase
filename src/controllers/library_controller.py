from src.database.crud import add_book, get_books, search_books, update_book, delete_book
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
        books = get_books()
        self.main.searchBooksWindow.listWidget.clear()
        self._populate_book_list(books)
    
    def search_books(self):
        """
        Realiza uma pesquisa dinâmica com base nos campos preenchidos.
        """
        title_query = self.main.searchBooksWindow.line_titulo.text().strip().lower()
        author_query = self.main.searchBooksWindow.line_autor.text().strip().lower()
        year_query = self.main.searchBooksWindow.line_publicacao.text().strip()
        pages_query = self.main.searchBooksWindow.line_Qpaginas.text().strip()

        results = search_books(title_query, author_query, year_query, pages_query)
    
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
        books = get_books()
        book_data = books.get(book_id, None)

        if not book_data:
            QMessageBox.warning(None, 'Erro', 'Não foi possível carregar os dados atualizados do livro.')
            return

        new_title, ok1 = QInputDialog.getText(None, "Editar Livro", "Novo título:", text=book_data['title'])
        if not ok1:  # Se o usuário cancelar, interrompe a função
            return

        new_author, ok2 = QInputDialog.getText(None, "Editar Livro", "Novo autor:", text=book_data['author'])
        if not ok2:
            return

        new_year, ok3 = QInputDialog.getText(None, "Editar Livro", "Novo ano de publicação:", text=str(book_data['year']))
        if not ok3:
            return

        new_pages, ok4 = QInputDialog.getText(None, "Editar Livro", "Nova quantidade de páginas:", text=str(book_data['pages']))
        if not ok4:
            return

        new_title = new_title.strip()
        new_author = new_author.strip()
        new_year = new_year.strip()
        new_pages = new_pages.strip()

        # Agora podemos validar os campos numéricos
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
