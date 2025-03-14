import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from src.gui.main_window import Main_window
from src.gui.login_window import Login_window
from src.gui.sign_up_window import Sign_up_window
from src.gui.library import Library_window
from src.gui.sign_up_books import Sign_up_books_window
from src.gui.search_books_window import Search_books_window
from src.controllers.login_user_controller import LoginController
from src.controllers.signup_user_controller import SignupController
from src.controllers.library_controller import LibraryController


class Ui_Main(QtWidgets.QWidget):
    """
    Classe Ui_Main responsável pela configuração da interface gráfica.
    """

    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()

        self.mainWindow = Main_window()
        self.mainWindow.setupUi(self.stack0)

        self.loginWindow = Login_window()
        self.loginWindow.setupUi(self.stack1)

        self.signupWindow = Sign_up_window()
        self.signupWindow.setupUi(self.stack2)

        self.libraryWindow = Library_window()
        self.libraryWindow.setupUi(self.stack3)

        self.signupBooksWindow = Sign_up_books_window()
        self.signupBooksWindow.setupUi(self.stack4)

        self.searchBooksWindow = Search_books_window()
        self.searchBooksWindow.setupUi(self.stack5)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

        self.login_controller = LoginController(self)
        self.signup_controller = SignupController(self)
        self.library_controller = LibraryController(self)

        self.mainWindow.Sair.clicked.connect(self.fecharPrograma)
        self.mainWindow.Login.clicked.connect(self.abrirLogin)
        self.mainWindow.Cadastrar.clicked.connect(self.abrirCadastroUser)
        self.loginWindow.voltar.clicked.connect(self.abrirMainWindow)
        self.signupWindow.voltar.clicked.connect(self.abrirMainWindow)
        self.libraryWindow.cadastrar.clicked.connect(self.abrirCadastroLivro)
        self.libraryWindow.pesquisar.clicked.connect(self.abrirPesquisarLivro)
        self.libraryWindow.sair.clicked.connect(self.abrirMainWindow)
        self.signupBooksWindow.voltar_2.clicked.connect(self.abrirLibrary)
        self.searchBooksWindow.voltar_2.clicked.connect(self.abrirLibrary)
        self.loginWindow.logar.clicked.connect(self.login_controller.login_function)
        self.signupWindow.finalizar.clicked.connect(self.signup_controller.create_acc_function)
        self.signupBooksWindow.cadastrar.clicked.connect(self.library_controller.add_book)
        self.searchBooksWindow.buscar.clicked.connect(self.library_controller.search_books)

    def fecharPrograma(self):
        sys.exit(app.exec_())

    def abrirMainWindow(self):
        self.QtStack.setCurrentIndex(0)

    def abrirLogin(self):
        self.loginWindow.line_email.setText('')
        self.loginWindow.line_senha.setText('')
        self.QtStack.setCurrentIndex(1)

    def abrirCadastroUser(self):
        self.signupWindow.line_email.setText('')
        self.signupWindow.line_senha.setText('')
        self.signupWindow.line_csenha.setText('')
        self.QtStack.setCurrentIndex(2)

    def abrirLibrary(self):
        self.QtStack.setCurrentIndex(3)

    def abrirCadastroLivro(self):
        self.signupBooksWindow.line_titulo.setText('')
        self.signupBooksWindow.line_autor.setText('')
        self.signupBooksWindow.line_Qpaginas.setText('')
        self.signupBooksWindow.line_publicacao.setText('')
        self.QtStack.setCurrentIndex(4)

    def abrirPesquisarLivro(self):
        self.searchBooksWindow.line_titulo.setText('')
        self.searchBooksWindow.line_autor.setText('')
        self.searchBooksWindow.line_Qpaginas.setText('')
        self.searchBooksWindow.line_publicacao.setText('')
        self.library_controller.load_books()
        self.QtStack.setCurrentIndex(5)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
