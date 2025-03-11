from src.database.crud import add_book
from PyQt5.QtWidgets import QMessageBox

class LibraryController:
    def __init__(self, main):
        self.main = main

        self.main.signupBooksWindow.cadastrar.clicked.connect(self.add_book)

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