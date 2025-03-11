import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from src.gui.main_window import Main_window
from src.gui.login_window import Login_window
from src.gui.sign_up_window import Sign_up_window
from src.database.firebase_config import auth, db


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

        self.mainWindow.pushButton.clicked.connect(self.abrirLogin)
        self.mainWindow.pushButton_2.clicked.connect(self.abrirCadastro)
        self.loginWindow.pushButton.clicked.connect(self.voltar_main_window)
        self.signupWindow.pushButton_3.clicked.connect(self.voltar_main_window)
        self.loginWindow.pushButton_2.clicked.connect(self.loginfunction)
        self.signupWindow.pushButton_4.clicked.connect(self.createaccfunction)

    
    def abrirLogin(self):
        self.QtStack.setCurrentIndex(2)
    
    def abrirCadastro(self):
        self.QtStack.setCurrentIndex(1)
    
    def voltar_main_window(self):
        self.QtStack.setCurrentIndex(0)
    
    def loginfunction(self):
        email = self.loginWindow.lineEdit.text()
        password = self.loginWindow.lineEdit_2.text()

        try:
            users = db.child("users").get().val()  # Obtém todos os usuários cadastrados

            if users:
                for user_id, user_data in users.items():
                    if user_data['email'] == email and user_data['password'] == password:
                        print(f"Login bem-sucedido! Bem-vindo, {email}")
                        self.QtStack.setCurrentIndex(0)  # Redireciona para a tela principal
                        return

            print("Erro: Usuário ou senha incorretos!")

        except Exception as e:
            print(f"Erro no login: {str(e)}")

    def createaccfunction(self):
        email = self.signupWindow.lineEdit_5.text()
        password = self.signupWindow.lineEdit_6.text()
        confirm_password = self.signupWindow.lineEdit_4.text()

        if password == confirm_password:
            try:
                # Criando um ID único para o usuário
                new_user = db.child("users").push({
                    "email": email,
                    "password": password  # OBS: Senha armazenada sem hash (não recomendado para produção)
                })

                print("Conta criada com sucesso!")
                self.QtStack.setCurrentIndex(0)  # Redireciona para a tela principal

            except Exception as e:
                print(f"Erro ao criar conta: {str(e)}")
        else:
            print("Erro: As senhas não coincidem!")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())