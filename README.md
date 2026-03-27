# Portfólio Pessoal - Projeto Django

## 📌 Sobre o Projeto

Este projeto consiste no desenvolvimento de um portfólio pessoal utilizando Django, com o objetivo de apresentar informações sobre um membro da equipe, incluindo suas habilidades, projetos e formas de contato.

O sistema foi desenvolvido como parte de uma atividade acadêmica, com foco em boas práticas de desenvolvimento web, organização de código e uso de banco de dados relacional.

---

## 🎯 Funcionalidades

* Seção de apresentação do usuário
* Listagem de habilidades
* Exibição de projetos
* Carousel para destaque de projetos
* Modal para detalhes dos projetos
* Formulário de contato com validação em JavaScript
* CRUD completo para gerenciamento de dados

---

## 🛠️ Tecnologias Utilizadas

* Python
* Django framework
* PostgreSQL
* HTML
* CSS
* JavaScript

---

## 🗂️ Estrutura do Projeto

O projeto foi dividido em apps para melhor organização:

* core: configurações gerais do sistema
* usuario: dados do portfólio
* projetos: gerenciamento dos projetos
* contato: formulário de contato

---

## 🧱 Modelagem do Banco de Dados

O sistema utiliza um banco de dados relacional com as seguintes entidades principais:

* Usuario
* Habilidade
* Projeto
* Contato

Relacionamentos:

* Um usuário pode possuir várias habilidades
* Um usuário pode possuir vários projetos

---

## ⚙️ Como Executar o Projeto

1. Clonar o repositório:
   git clone <url-do-repositorio>

2. Acessar a pasta do projeto:
   cd nome-do-projeto

3. Criar e ativar o ambiente virtual:
   python -m venv venv
   venv\Scripts\activate (Windows)

4. Instalar as dependências:
   pip install -r requirements.txt

5. Configurar o banco de dados PostgreSQL no arquivo settings.py

6. Executar as migrações:
   python manage.py makemigrations
   python manage.py migrate

7. Criar superusuário:
   python manage.py createsuperuser

8. Rodar o servidor:
   python manage.py runserver

---

## 👥 Equipe

* Emilly — Modelagem de dados e backend principal
* John — Backend e integração
* Pablo — Frontend e interatividade

---

## ✅ Status do Projeto

Concluído.

---

## 📌 Observações

Este projeto foi desenvolvido com foco em funcionalidade, organização e aplicação prática dos conceitos de desenvolvimento web com Django.

---

## 📄 Licença

Este projeto é de uso acadêmico.
