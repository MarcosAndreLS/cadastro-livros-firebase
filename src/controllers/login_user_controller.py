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
            self.main.QtStack.setCurrentIndex(3)  # Redireciona para a tela principal
            QMessageBox.information(None, 'Sucesso', f'Login bem-sucedido! Bem-vindo, {email}')
        elif result == "EMAIL_INVÁLIDO":
            QMessageBox.warning(None, 'Erro', 'Por favor, digite um email')
        elif result == "SENHA_AUSENTE":
            QMessageBox.warning(None, 'Erro', 'Por favor, digite uma senha.')
        elif result == "SENHA_INVÁLIDA":
            QMessageBox.warning(None, 'Erro', 'Senha incorreta!')  
        else:
            QMessageBox.critical(None, 'Erro', 'Ocorreu um erro desconhecido')
        # try:
        #     users = db.child("users").get().val()  # Obtém todos os usuários cadastrados

        #     if users:
        #         for user_id, user_data in users.items():
        #             if user_data['email'] == email and user_data['password'] == password:
        #                 print(f"Login bem-sucedido! Bem-vindo, {email}")
        #                 self.main.QtStack.setCurrentIndex(3)  # Redireciona para a tela principal
        #                 return

        #     print("Erro: Usuário ou senha incorretos!")

        # except Exception as e:
        #     print(f"Erro no login: {str(e)}")