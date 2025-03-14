from src.database.auth import authenticate_user
from PyQt5.QtWidgets import QMessageBox


class LoginController:
    def __init__(self, main):
        self.main = main

    def login_function(self):
        email = self.main.loginWindow.line_email.text()
        password = self.main.loginWindow.line_senha.text()

        result = authenticate_user(email, password)

        if result == "SUCCESS":
            self.main.QtStack.setCurrentIndex(3)
            QMessageBox.information(None, 'Sucesso', f'Login bem-sucedido! Bem-vindo, {email}')
        elif result == "EMAIL_INVÁLIDO":
            QMessageBox.warning(None, 'Erro', 'Por favor, digite um email')
        elif result == "SENHA_AUSENTE":
            QMessageBox.warning(None, 'Erro', 'Por favor, digite uma senha.')
        elif result == "CREDENCIAIS_INVÁLIDAS":
            QMessageBox.warning(None, 'Erro', 'Credenciais de login inválidas')  
        else:
            QMessageBox.critical(None, 'Erro', 'Ocorreu um erro desconhecido')
