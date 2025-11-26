# MusicVault

Sistema de gerenciamento de discografia desenvolvido em Django. Permite o cadastro, edição e exclusão de Artistas, Álbuns e Gêneros Musicais.

## Pré-requisitos

Certifique-se de ter instalado na máquina:
- Python 3.10 ou superior
- Git

## Guia de Instalação

Siga os passos abaixo no terminal para configurar o ambiente e executar o projeto.

### 1. Clonar o repositório

Baixe o código fonte e entre na pasta do projeto:

git clone https://github.com/Daabzin/musiclist-django.git
cd musiclist-django

### 2. Configurar o Ambiente Virtual

Crie e ative o ambiente virtual para isolar as dependências:

No Windows:
python -m venv .venv
.venv\Scripts\activate

No Linux/macOS:
python3 -m venv .venv
source .venv/bin/activate

### 3. Instalar Dependências

Instale o Django e o Selenium listados no arquivo de requisitos:

pip install -r requirements.txt

### 4. Configurar o Banco de Dados

Aplique as migrações para criar o arquivo do banco de dados SQLite local:

python manage.py migrate

### 5. Criar Administrador (Opcional)

Para acessar o painel administrativo do Django, crie um superusuário:

python manage.py createsuperuser

(Siga as instruções no terminal para definir usuário e senha)

### 6. Executar o Servidor

Inicie o servidor de desenvolvimento local:

python manage.py runserver

### 7. Acessar a Aplicação

Abra o navegador e acesse os seguintes endereços:

- Aplicação Principal: http://127.0.0.1:8000/
- Painel Administrativo: http://127.0.0.1:8000/admin/