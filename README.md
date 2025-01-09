# 📽️ API RESTful de Filmes com Django REST Framework

Esta API RESTful foi construída com Django e Django REST Framework. Ela oferece funcionalidades completas para manipulação de filmes, atores, gêneros e reviews, além de autenticação utilizando JSON Web Tokens (JWT).

## 🚀 Endpoints da API

### 🔑 Autenticação

- **`POST /authentication/token/`**
  - **Descrição**: Obtém o token de acesso JWT para autenticação.
  - **Parâmetros**: `username`, `password`

- **`POST /authentication/token/refresh/`**
  - **Descrição**: Atualiza o token de acesso JWT usando o refresh token.
  - **Parâmetros**: `refresh_token`

- **`POST /authentication/token/verify/`**
  - **Descrição**: Verifica se o token JWT é válido.
  - **Parâmetros**: `token`

### 🎭 Atores

- **`GET /actors/`**
  - **Descrição**: Lista todos os atores cadastrados na API.
  - **Parâmetros**: Nenhum

- **`POST /actors/`**
  - **Descrição**: Cria um novo ator.
  - **Parâmetros**: `name`, `birthdate`, outros campos relevantes

- **`GET /actors/{id}/`**
  - **Descrição**: Recupera os detalhes de um ator específico pelo seu ID.
  - **Parâmetros**: `id` (ID do ator)

- **`PUT /actors/{id}/`**
  - **Descrição**: Atualiza as informações de um ator existente.
  - **Parâmetros**: `id` (ID do ator), `name`, `birthdate`, outros campos relevantes

- **`DELETE /actors/{id}/`**
  - **Descrição**: Exclui um ator da base de dados.
  - **Parâmetros**: `id` (ID do ator)

### 🎬 Gêneros

- **`GET /genres/`**
  - **Descrição**: Lista todos os gêneros de filmes cadastrados.
  - **Parâmetros**: Nenhum

- **`POST /genres/`**
  - **Descrição**: Cria um novo gênero de filme.
  - **Parâmetros**: `name`

- **`GET /genres/{id}/`**
  - **Descrição**: Recupera os detalhes de um gênero específico pelo seu ID.
  - **Parâmetros**: `id` (ID do gênero)

- **`PUT /genres/{id}/`**
  - **Descrição**: Atualiza as informações de um gênero existente.
  - **Parâmetros**: `id` (ID do gênero), `name`

- **`DELETE /genres/{id}/`**
  - **Descrição**: Exclui um gênero de filme.
  - **Parâmetros**: `id` (ID do gênero)

### 🍿 Filmes

- **`GET /movies/`**
  - **Descrição**: Lista todos os filmes cadastrados.
  - **Parâmetros**: Nenhum

- **`POST /movies/`**
  - **Descrição**: Cria um novo filme.
  - **Parâmetros**: `title`, `release_date`, `genre`, `actors`, outros campos relevantes

- **`GET /movies/{id}/`**
  - **Descrição**: Recupera os detalhes de um filme específico pelo seu ID.
  - **Parâmetros**: `id` (ID do filme)

- **`PUT /movies/{id}/`**
  - **Descrição**: Atualiza as informações de um filme existente.
  - **Parâmetros**: `id` (ID do filme), `title`, `release_date`, outros campos relevantes

- **`DELETE /movies/{id}/`**
  - **Descrição**: Exclui um filme da base de dados.
  - **Parâmetros**: `id` (ID do filme)

- **`GET /movies/stats/`**
  - **Descrição**: Recupera estatísticas sobre os filmes (como média de avaliações, número de filmes por gênero, etc.)
  - **Parâmetros**: Nenhum

### 📝 Reviews

- **`GET /reviews/`**
  - **Descrição**: Lista todas as avaliações de filmes.
  - **Parâmetros**: Nenhum

- **`POST /reviews/`**
  - **Descrição**: Cria uma nova avaliação para um filme.
  - **Parâmetros**: `movie_id`, `review_text`, `rating`, outros campos relevantes

- **`GET /reviews/{id}/`**
  - **Descrição**: Recupera os detalhes de uma avaliação específica pelo seu ID.
  - **Parâmetros**: `id` (ID da avaliação)

- **`PUT /reviews/{id}/`**
  - **Descrição**: Atualiza uma avaliação existente.
  - **Parâmetros**: `id` (ID da avaliação), `review_text`, `rating`

- **`DELETE /reviews/{id}/`**
  - **Descrição**: Exclui uma avaliação.
  - **Parâmetros**: `id` (ID da avaliação)


## 🛠️ Tecnologias Utilizadas

- **Django** - Framework web para Python
- **Django REST Framework** - Framework para criação de APIs RESTful
- **Django JWT** - Autenticação usando JWT (JSON Web Token)
- **CSV** - Importação de dados através de arquivos CSV

## 💻 Como Rodar a API Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Rode as migrações:
   ```bash
   python manage.py migrate
   ```

4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
Acesse a API localmente em `http://127.0.0.1:8000/`.
