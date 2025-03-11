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
        self.mainWindow.Cadastrar.clicked.connect(self.abrirCadastro)
        self.loginWindow.voltar.clicked.connect(self.voltar_main_window)
        self.signupWindow.voltar.clicked.connect(self.voltar_main_window)
        self.libraryWindow.cadastrar.clicked.connect(self.abrirCadastroLivro)
        self.libraryWindow.pesquisar.clicked.connect(self.abrirPesquisarLivro)
        self.signupBooksWindow.voltar_2.clicked.connect(self.voltar_library)
        self.searchBooksWindow.voltar_2.clicked.connect(self.voltar_library)

    def fecharPrograma(self):
        sys.exit(app.exec_())

    def abrirLogin(self):
        self.QtStack.setCurrentIndex(1)
    
    def abrirCadastro(self):
        self.QtStack.setCurrentIndex(2)
    
    def voltar_library(self):
        self.QtStack.setCurrentIndex(3)

    def abrirPesquisarLivro(self):
        self.QtStack.setCurrentIndex(5)
        self.library_controller.load_books()

    def abrirCadastroLivro(self):
        self.QtStack.setCurrentIndex(4)

    def voltar_main_window(self):
        self.QtStack.setCurrentIndex(0)
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())