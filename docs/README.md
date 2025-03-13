# cadastro-livros-firebase


### Baixando e acessando o repositório
```bash
git clone https://github.com/MarcosAndreLS/cadastro-livros-firebase.git
cd cadastro-livros-firebase
```

### Instalando as dependências
```bash
pip install requirements.txt
```

### Estrutura do projeto

```bash
cadastro-livros-firebase/
    |
    |--- docs/
        README.md # documentação do projeto
    |
    |--- src/
        |
        |--- controllers/
            library_controller.py # 
            login_user_controller.py
            signup_user_controller.py
        |--- database/
            auth.py
            crud.py            
            firebase_config.py # credenciais do firebase
        |
        |--- gui/
            |
            |--- ui/
            library.py
            login_window.py
            main_window.py
            search_books_window.py
            sign_up_books_window.py
            sign_up_window.py
    main.py
    requirements.txt
```

### Executando a aplicação

```bash
python main.py
```
### Prints da interface

![Tela Principal](https://github.com/user-attachments/assets/26e31e67-edd3-4b76-abc3-208d4db4532a)

```
A tela principal contém opções de saída da aplicação, login de usuário e cadastro de usuário. 
```

![Tela de Login](https://github.com/user-attachments/assets/6f92ede2-c0b9-48be-ab85-941427c6b027)

```
A tela de login possui campos de inserção de dados como email e senha. E os botões para logar e voltar para tela principal. O seguintes "Messages Box" podem ser mostrados na tela de login.
|
|--- Caso não haja informações nos campos, será mostrado um "Message Box" pedindo para preencher o campo email.
|--- Caso não haja informação no campo ed senha, será mostrado um "Message Box" pedindo para preencher o campo senha.
|--- Caso seja inserido o email e senha corretos, será mostrado a tela principal da biblioteca com o "Message Box" de login bem sucedido.
```
![image](https://github.com/user-attachments/assets/db72b485-f94b-48ea-a2de-776c843fb39e)

![image](https://github.com/user-attachments/assets/5d7b2a1e-d01e-474c-b333-c821c19dae90)

![image](https://github.com/user-attachments/assets/806a9965-8291-4281-b597-5bc08d12c99c)
```
 
```
![image](https://github.com/user-attachments/assets/b07ac6f9-eb20-469b-9562-9a5c91209ad6)
```
A tela de cadastro contém opções de voltar para tela principal e finalizar o cadastro. Além disso, ela possui campos de inserção de dados como email, senha e confirmação de senha.  O seguintes "Messages Box" podem ser mostrados na tela de login.
|
|--- Caso não haja informações nos campos, será mostrado um "Message Box" pedindo para preencher o campo email.
|--- Caso não haja informação no campo de senha, será mostrado um "Message Box" pedindo para preencher o campo senha.
|--- Caso seja inserido o email e senha corretos, será mostrado a tela principal da biblioteca com o "Message Box" de login bem sucedido.
```





