# cadastro-livros-firebase

## Sobre o projeto

O projeto tem como objetivo implementar um sistema de cadastro de livros da biblioteca utilizando Python com interface gráfica (GUI) e armazenamento no Firebase.

### 📋 Requisitos Funcionais:

O sistema deve permitir as operações CRUD nos seguintes campos:
- Título do livro
- Autor principal
- Quantidade de páginas
- Ano de publicação

### ⚙ Requisitos Técnicos:

- A interface gráfica deve ser implementada com (Tkinter ou PyQt).
- O Firebase deve ser utilizado tanto para armazenamento dos livros quanto para autenticação do usuário.
- A autenticação pode ser feita via email/senha.
- O banco de dados pode ser Firestore ou Realtime Database.
- Implementar mensagens de erro/sucesso para operações do CRUD.
- As operações CRUD devem refletir as alterações no Firebase e ser demonstradas na apresentação do projeto.

### Clonando e acessando o repositório
```bash
git clone https://github.com/MarcosAndreLS/cadastro-livros-firebase.git
cd cadastro-livros-firebase
```

### Instalando as dependências
```bash
pip install -r requirements.txt
```

### Estrutura do projeto

```bash
cadastro-livros-firebase/
    |
    |--- docs/
    |    |--- README.md # documentação do projeto
    |
    |--- src/
    |    |
    |    |--- controllers/
    |    |   |--- library_controller.py # 
    |    |   |--- login_user_controller.py
    |    |   |--- signup_user_controller.py
    |    |
    |    |--- database/
    |    |   |--- auth.py # responsável pela autenticação
    |    |   |--- crud.py # responsável por fazer o CRUD           
    |    |   |--- firebase_config.py # credenciais do firebase
    |    |
    |    |--- gui/ # interfaces gráficas
    |        |--- ui/
    |        |
    |        |--- library.py
    |        |--- login_window.py
    |        |--- main_window.py
    |        |--- search_books_window.py
    |        |--- sign_up_books_window.py
    |        |--- sign_up_window.py
    |--- main.py
    |--- requirements.txt
```

### Executando a aplicação

```bash
python main.py
```

### Tecnologias utilizadas

- `Firebase`
    - `Realtime Database`
    - `Authentication`
- `PyQt5`

#### Realtime Database

<img src="../images/url-image-books.png"/>

#### Authentication

<img src="../images/autenticacao.png"/>

### Prints da interface

![Tela Principal](https://github.com/user-attachments/assets/26e31e67-edd3-4b76-abc3-208d4db4532a)


A tela principal contém opções de saída da aplicação, login de usuário e cadastro de usuário. 


![Tela de Login](https://github.com/user-attachments/assets/6f92ede2-c0b9-48be-ab85-941427c6b027)


A tela de login possui campos de inserção de dados como email e senha. E os botões para logar e voltar para tela principal. O seguintes "Messages Box" podem ser mostrados na tela de login.

- Caso não haja informações nos campos, será mostrado um "Message Box" pedindo para preencher o campo email.
- Caso não haja informação no campo ed senha, será mostrado um "Message Box" pedindo para preencher o campo senha.
- Caso seja inserido o email e senha corretos, será mostrado a tela principal da biblioteca com o "Message Box" de login bem sucedido.

![image](https://github.com/user-attachments/assets/db72b485-f94b-48ea-a2de-776c843fb39e)

![image](https://github.com/user-attachments/assets/5d7b2a1e-d01e-474c-b333-c821c19dae90)

![image](https://github.com/user-attachments/assets/806a9965-8291-4281-b597-5bc08d12c99c)
```
 
```
![image](https://github.com/user-attachments/assets/b07ac6f9-eb20-469b-9562-9a5c91209ad6)

A tela de cadastro contém opções de voltar para tela principal e finalizar o cadastro. Além disso, ela possui campos de inserção de dados como email, senha e confirmação de senha. O seguintes "Messages Box" podem ser mostrados na tela de cadastro.

- Caso não haja informações nos campos, será mostrado um "Message Box" pedindo para preencher o campo email.
- Caso não haja informação no campo de senha, será mostrado um "Message Box" pedindo para preencher o campo senha.
- Caso seja inserido um email com uma senha abaixo de 6 caracteres, será mostrado um "Message Box" infromando que a senha é fraca e é necessário pelo menos 6 caractes.
- Caso o email já esteja cadastrado, será mostrado um "Message Box" informando que o email já foi cadastrado.
- Caso seja inserido senhas diferentes, será mostrado um "Message Box" informando que as senhas são diferentes.

![image](https://github.com/user-attachments/assets/ecd3e0d4-9070-4eb6-9985-4df7fa4b4fec)
![image](https://github.com/user-attachments/assets/cefc0155-394a-4e44-9d8c-e1a99f24db0c)
![image](https://github.com/user-attachments/assets/597f4d8b-8037-4d59-9b9b-57c757a1f2f1)

```
```
![image](https://github.com/user-attachments/assets/33f02a4a-a987-49e2-878b-c521d1b3ce19)

A tela principal da biblioteca contém as opções de voltar para tela inicial, cadastrar livro e pesquisar os livros.

![image](https://github.com/user-attachments/assets/d5200e68-11f4-4d16-9579-1db1f60057a7)


A tela de cadastro de livro contém os campos de título do livro, nome do autor, quantidade de páginas e ano de publicação. Além disso, existe o botão de cadastro de livro e o botão de voltar. O seguintes "Messages Box" podem ser mostrados na tela de cadastro do livro.

- Caso não haja informações nos campos, será mostrado um "Message Box" pedindo para preencher todos os campos. Isso serve para todas as outras condições de campo preenchido.
- Caso haja um livro cadastrado com as mesmas informações de outro, será mostrado um "Message Box" informando que o livro já foi cadastrado.
- Caso o livro seja cadastrado com sucesso, será mostrado um "Message Box" informando que o livro foi cadastrado com sucesso.

![image](https://github.com/user-attachments/assets/e4be1b7c-2d29-4de1-9bd3-60a73cf0ed27)
![image](https://github.com/user-attachments/assets/8f9c8adf-44c9-4b29-9a58-a3d600a0f8c5)
![image](https://github.com/user-attachments/assets/28039bf3-97e0-4a96-8c2e-a02c295b0106)
```
```
![image](https://github.com/user-attachments/assets/239eb6c4-6bd7-498a-bd67-844bf08fe3e5)


A tela de pesquisar os livros, mostra todos os livros cadastrados juntamente com as opções de editar e excluir o livro correspondente. Além disso, existem campos de pesquisa, caso seja inserido algum dado, será pesquisado e retornado o resultado após apertar o botão de buscar.

- Caso queira excluir o livro, será mostrado um "Message Box" com as opções de sim e não. Caso seja escolhido a opção sim, o livro será excluído. Após isso, será mostrado um "Message Box" informando que o livro foi excluído com sucesso.

![image](https://github.com/user-attachments/assets/e55a709c-9e62-4033-a023-452ff1612530)

![image](https://github.com/user-attachments/assets/e93c337a-a2fc-42e0-88a6-6be45ad1b1c3)