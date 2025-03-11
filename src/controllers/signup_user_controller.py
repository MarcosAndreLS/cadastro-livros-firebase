from src.database.firebase_config import db

class SignupController:
    def __init__(self, main):
        self.main = main
        self.main.signupWindow.finalizar.clicked.connect(self.create_acc_function)
        self.main.signupWindow.senhas_diferentes.setVisible(False)
    def create_acc_function(self):
        email = self.main.signupWindow.line_email.text()
        password = self.main.signupWindow.line_senha.text()
        confirm_password = self.main.signupWindow.line_csenha.text()

        if password == confirm_password:
            try:
                db.child("users").push({
                    "email": email,
                    "password": password  # Senha deve ser criptografada
                })

                print("Conta criada com sucesso!")
                self.main.QtStack.setCurrentIndex(0)  # Redireciona para a tela principal
            except Exception as e:
                print(f"Erro ao criar conta: {str(e)}")
        else:
            self.main.signupWindow.senhas_diferentes.setVisible(True)