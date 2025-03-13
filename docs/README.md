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