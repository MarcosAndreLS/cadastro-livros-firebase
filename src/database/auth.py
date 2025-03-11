from src.database.firebase_config import db

def authenticate_user(email, password):
    """
    Verifica as credenciais do usuário no Firebase Realtime Database.

    :param email: Email do usuário
    :param password: Senha do usuário
    :return: True se o login for bem-sucedido, False caso contrário
    """
    try:
        users = db.child("users").get().val()  # Obtém todos os usuários cadastrados

        if users:
            for user_id, user_data in users.items():
                if user_data.get('email') == email and user_data.get('password') == password:
                    return True  # Usuário autenticado com sucesso

        return False  # Credenciais incorretas

    except Exception as e:
        print(f"Erro ao autenticar usuário: {str(e)}")
        return False


def create_user(email, password):
    """
    Cria um novo usuário no Firebase Realtime Database.

    :param email: Email do usuário
    :param password: Senha do usuário (deve ser criptografada em produção)
    :return: True se o usuário for criado com sucesso, False caso contrário
    """
    try:
        db.child("users").push({
            "email": email,
            "password": password  # Senha deve ser criptografada em produção
        })

        return True  # Conta criada com sucesso
    except Exception as e:
        print(f"Erro ao criar conta: {str(e)}")
        return False