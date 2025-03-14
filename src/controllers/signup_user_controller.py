from src.database.auth import create_user
from PyQt5.QtWidgets import QMessageBox


class SignupController:
    def __init__(self, main):
        self.main = main

    def create_acc_function(self):
        email = self.main.signupWindow.line_email.text()
        password = self.main.signupWindow.line_senha.text()
        confirm_password = self.main.signupWindow.line_csenha.text()

        if password == confirm_password:
            result = create_user(email, password)

            if result == "SUCCESS":
                QMessageBox.information(None, 'Sucesso', 'Conta criada com sucesso!')
                self.main.QtStack.setCurrentIndex(0)
            elif result == "EMAIL_INVÁLIDO":
                QMessageBox.warning(None, 'Erro', 'O e-mail fornecido não é válido.')
            elif result == "EMAIL_JÁ_CADASTRADO":
                QMessageBox.warning(None, 'Erro', 'Este e-mail já está cadastrado.')
            elif result == "SENHA_FRACA":
                QMessageBox.warning(None, 'Erro', 'A senha é muito fraca. Use pelo menos 6 caracteres.')
            elif result == "SENHA_AUSENTE":
                QMessageBox.warning(None, 'Erro', 'Por favor, digite uma senha.')
            elif result == "EMAIL_AUSENTE":
                QMessageBox.warning(None, 'Erro', 'Por favor, digite uma email.')
            else:
                QMessageBox.critical(None, 'Erro', 'Ocorreu um erro desconhecido ao criar a conta.')
        else:
            QMessageBox.information(None, 'Erro', 'Senhas diferentes')
