# Biblioteca Online

## Descrição
A **Livraria Online** é um sistema que oferece acesso a um catálogo de livros acadêmicos focados em Ciência da Computação. O projeto integra uma API externa para fornecer dados dos livros e outras funcionalidades essenciais para os usuários.

## Estrutura do Projeto
Este projeto consiste em dois repositórios principais que trabalham em conjunto:

1. **books-api** ([repositório API externa](https://github.com/vicct0r/books-api-service)):
   - API que armazena e organiza o catálogo de livros.
   - Focado em livros acadêmicos específicos para Ciência da Computação.
   - Responsável por fornecer dados para o site da livraria.

2. **library**:
   - Interface de usuário para navegação e visualização dos livros.
   - Gerencia o cadastro, autenticação e autorização dos usuários.
   - Integra-se com a API para exibir o catálogo e permitir o download de livros para usuários autenticados.

## Objetivo
O objetivo principal do projeto é disponibilizar uma plataforma onde usuários possam:
- Acessar e navegar em um catálogo de livros acadêmicos.
- Baixar livros após realizar login e validação de e-mail.
- Beneficiar-se de uma experiência de usuário intuitiva e simplificada.

## Funcionalidades
O site da Livraria Online oferece as seguintes funcionalidades:

- **Autenticação e Autorização**: Controle de acesso ao catálogo de livros.
- **Confirmação de E-mail**: Requer validação de e-mail para ativação de conta, garantindo a segurança.
- **Integração com API**: Os dados dos livros são obtidos a partir da `books-api`, que mantém um repositório atualizado dos títulos disponíveis.

## Diagrama de Processo
![Livraria](https://github.com/user-attachments/assets/2159e52b-35ef-457f-8e16-5dd13990068d)

## Observações
- **Status do Projeto**: Ambos os repositórios (`books-api` e `library`) estão em fase inicial de desenvolvimento, portanto a estrutura e a lógica ainda podem passar por mudanças significativas.
- **Dependência**: Este projeto (`library`) depende da `books-api` para obter os dados dos livros. 

*OBS.: Os dois repositórios são partes do mesmo projeto*.
