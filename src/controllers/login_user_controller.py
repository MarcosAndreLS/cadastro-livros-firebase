from src.database.firebase_config import db

class LoginController:
    def __init__(self, main):
        self.main = main
        self.main.loginWindow.logar.clicked.connect(self.login_function)

    def login_function(self):
        email = self.main.loginWindow.lineEdit.text()
        password = self.main.loginWindow.lineEdit_2.text()

        try:
            users = db.child("users").get().val()  # Obtém todos os usuários cadastrados

            if users:
                for user_id, user_data in users.items():
                    if user_data['email'] == email and user_data['password'] == password:
                        print(f"Login bem-sucedido! Bem-vindo, {email}")
                        self.main.QtStack.setCurrentIndex(3)  # Redireciona para a tela principal
                        return

            print("Erro: Usuário ou senha incorretos!")

        except Exception as e:
            print(f"Erro no login: {str(e)}")