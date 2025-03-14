from src.database.firebase_config import auth


def authenticate_user(email, password):
    """
    Verifica as credenciais do usuário no Firebase Realtime Database.

    :param email: Email do usuário
    :param password: Senha do usuário
    :return: True se o login for bem-sucedido, False caso contrário
    """
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return "SUCCESS"
    except Exception as e:
        error_message = str(e)
        print(e)
        if "INVALID_EMAIL" in error_message:
            return "EMAIL_INVÁLIDO"
        elif "MISSING_PASSWORD" in error_message:
            return "SENHA_AUSENTE"
        elif "INVALID_LOGIN_CREDENTIALS" in error_message:
            return "CREDENCIAIS_INVÁLIDAS"
        else:
            return "ERRO_DESCONHECIDO"


def create_user(email, password):
    """
    Cria um novo usuário no Firebase Realtime Database.

    :param email: Email do usuário
    :param password: Senha do usuário (deve ser criptografada em produção)
    :return: True se o usuário for criado com sucesso, False caso contrário
    """
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return "SUCCESS"  # Conta criada com sucesso
    except Exception as e:
        error_message = str(e)
        if "INVALID_EMAIL" in error_message:
            return "EMAIL_INVÁLIDO"
        elif "EMAIL_EXISTS" in error_message:
            return "EMAIL_JÁ_CADASTRADO"
        elif "WEAK_PASSWORD" in error_message:
            return "SENHA_FRACA"
        elif "MISSING_PASSWORD" in error_message:
            return "SENHA_AUSENTE"
        elif "MISSING_EMAIL" in error_message:
            return "EMAIL_AUSENTE"
        else:
            return "ERRO_DESCONHECIDO"
