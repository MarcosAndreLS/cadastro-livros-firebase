import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from src.gui.main_window import Main_window
from src.gui.login_window import Login_window
from src.gui.sign_up_window import Sign_up_window

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

        self.mainWindow = Main_window()
        self.mainWindow.setupUi(self.stack0)

        self.loginWindow = Login_window()
        self.loginWindow.setupUi(self.stack1)

        self.signupWindow = Sign_up_window()
        self.signupWindow.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())