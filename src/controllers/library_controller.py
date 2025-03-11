from src.database.crud import add_book, get_books, search_books
from PyQt5.QtWidgets import QMessageBox, QWidget, QLabel, QPushButton, QListWidgetItem, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QSize


class LibraryController:
    def __init__(self, main):
        self.main = main #isso pode estar deixando a aplicação lenta para abrir

        self.main.signupBooksWindow.cadastrar.clicked.connect(self.add_book)
        self.main.searchBooksWindow.buscar.clicked.connect(self.search_books)

    def add_book(self):
        """
        Obtém os dados da interface e adiciona um livro no Firebase.
        """
        title = self.main.signupBooksWindow.line_titulo.text()
        author = self.main.signupBooksWindow.line_autor.text()
        pages = self.main.signupBooksWindow.line_Qpaginas.text()
        year = self.main.signupBooksWindow.line_publicacao.text()

        if add_book(title, author, pages, year):
            QMessageBox.information(None, 'Sucesso', 'Livro adicionado com sucesso')
            self.main.signupBooksWindow.line_titulo.setText('')
            self.main.signupBooksWindow.line_autor.setText('')
            self.main.signupBooksWindow.line_Qpaginas.setText('')
            self.main.signupBooksWindow.line_publicacao.setText('')
        else:
            QMessageBox.information(None, 'Erro', 'Erro ao adiconar livro')

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
            # Criando o widget que conterá as informações e os botões
            book_widget = QWidget()
            main_layout = QVBoxLayout()  # Layout vertical para melhor espaçamento
            info_layout = QVBoxLayout()  # Layout separado para os textos
            buttons_layout = QHBoxLayout()  # Layout horizontal para os botões
            
            # Rótulo com informações do livro
            book_info = QLabel(
                f"Título: {book_data['title']}\n"
                f"Autor: {book_data['author']}\n"
                f"Ano: {book_data['year']}\n"
                f"Páginas: {book_data['pages']}"
            )

            # Botão de editar
            edit_button = QPushButton("✏️ Editar")
            edit_button.clicked.connect(lambda _, bid=book_id: self.edit_book(bid))

            # Botão de excluir
            delete_button = QPushButton("🗑️ Excluir")
            delete_button.clicked.connect(lambda _, bid=book_id: self.delete_book(bid))

            # Adiciona os elementos aos layouts
            info_layout.addWidget(book_info)
            buttons_layout.addWidget(edit_button)
            buttons_layout.addWidget(delete_button)

            main_layout.addLayout(info_layout)
            main_layout.addLayout(buttons_layout)

            book_widget.setLayout(main_layout)

            # Adiciona ao QListWidget
            item = QListWidgetItem(self.main.searchBooksWindow.listWidget)
            altura = book_widget.sizeHint().height() + 20  # Ajuste fino para evitar cortes
            largura = book_widget.sizeHint().width()
            item.setSizeHint(QSize(largura, altura))
            self.main.searchBooksWindow.listWidget.addItem(item)
            self.main.searchBooksWindow.listWidget.setItemWidget(item, book_widget)
