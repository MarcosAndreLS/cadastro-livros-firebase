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
                self.main.QtStack.setCurrentIndex(0)  # Redireciona para a tela principal
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
            
        # if password == confirm_password:
        #     try:
        #         db.child("users").push({
        #             "email": email,
        #             "password": password  # Senha deve ser criptografada
        #         })

        #         print("Conta criada com sucesso!")
        #         self.main.QtStack.setCurrentIndex(0)  # Redireciona para a tela principal
        #     except Exception as e:
        #         print(f"Erro ao criar conta: {str(e)}")
        # else:
        #     self.main.signupWindow.senhas_diferentes.setVisible(True)