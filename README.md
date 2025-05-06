# Airline Reservation API

Este projeto implementa um sistema de gerenciamento de companhias aéreas, aeroportos, voos e reservas, baseado em Django e Django REST Framework. Inclui autenticação de usuários, endpoints para CRUD de entidades e funcionalidades adicionais como destinos disponíveis e voos mais baratos.

---

## Pré-requisitos

* Docker e Docker Compose
* Git

---

## Instalação local (sem Docker)

1. Clone o repositório:

   ```bash
   git clone https://github.com/JotahIvo/Airport-API.git
   cd Airport-API
   ```
2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. Aplique as migrações:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```
6. Acesse a API em: `http://localhost:8000/`

---

## Usando com Docker

1. Certifique-se de que Docker e Docker Compose estão instalados.
2. Construa e suba os containers:

   ```bash
   docker-compose up --build -d
   ```
3. Aplique as migrações dentro do container:

   ```bash
   docker-compose exec web python manage.py migrate
   ```
4. Acesse a API em: `http://localhost:8000/`

> Se encontrar erros de porta em uso, ajuste a seção `ports` no `docker-compose.yml` para liberar a porta desejada.

---

## Endpoints da API

### Usuários e Autenticação

| Método | Endpoint       | Descrição                    | Autenticação     |
| ------ | -------------- | ---------------------------- | ---------------- |
| POST   | `/register/`   | Cadastro de usuário          | Public           |
| POST   | `/super-user/` | Cadastro de superusuário     | Public           |
| POST   | `/login/`      | Login (session auth)         | Public           |
| POST   | `/logout/`     | Logout                       | Sessão requerida |
| GET    | `/user/`       | Dados do usuário autenticado | Sessão requerida |

### Companhias Aéreas (Airline)

| Método | Endpoint         | Descrição                         | Autenticação        |
| ------ | ---------------- | --------------------------------- | ------------------- |
| GET    | `/airline/`      | Listar todas as companhias        | Public              |
| POST   | `/airline/`      | Criar nova companhia              | Public              |
| GET    | `/airline/{id}/` | Detalhar companhia por ID         | Public              |
| PUT    | `/airline/{id}/` | Atualizar companhia (autenticado) | Usuário autenticado |
| DELETE | `/airline/{id}/` | Remover companhia (autenticado)   | Usuário autenticado |

### Aeroportos (Airports)

| Método | Endpoint                                      | Descrição                                       | Autenticação        |
| ------ | --------------------------------------------- | ----------------------------------------------- | ------------------- |
| GET    | `/airports/`                                  | Listar aeroportos                               | Public              |
| POST   | `/airports/`                                  | Criar novo aeroporto                            | Public              |
| GET    | `/airports/{id}/`                             | Detalhar aeroporto por ID                       | Public              |
| PUT    | `/airports/{id}/`                             | Atualizar aeroporto (autenticado)               | Usuário autenticado |
| DELETE | `/airports/{id}/`                             | Remover aeroporto (autenticado)                 | Usuário autenticado |
| GET    | `/airlines/airports/`                         | Listar aeroportos agrupados por companhia aérea | Public              |
| GET    | `/airports/{origin_airport_id}/destinations/` | Destinos disponíveis a partir de um aeroporto   | Public              |

### Voos (Flights)

| Método | Endpoint                              | Descrição                                                  | Autenticação        |
| ------ | ------------------------------------- | ---------------------------------------------------------- | ------------------- |
| GET    | `/flights/`                           | Listar voos                                                | Public              |
| POST   | `/flights/`                           | Criar novo voo                                             | Public              |
| GET    | `/flights/{id}/`                      | Detalhar voo por ID                                        | Public              |
| PUT    | `/flights/{id}/`                      | Atualizar voo (autenticado)                                | Usuário autenticado |
| DELETE | `/flights/{id}/`                      | Remover voo (autenticado)                                  | Usuário autenticado |
| GET    | `/flights/{flight_date}/`             | Voos disponíveis em data (`YYYY-MM-DD`)                    | Public              |
| GET    | `/flights/cheapest/{num_passengers}/` | Voos ordenados por preço para `num_passengers` passageiros | Public              |

### Reserva de Passagens (Reservation)

| Método | Endpoint            | Descrição                                  | Autenticação        |
| ------ | ------------------- | ------------------------------------------ | ------------------- |
| POST   | `/purchase-ticket/` | Comprar passagem (gera locator e e-ticket) | Usuário autenticado |

---

## Variáveis de ambiente

* `DEBUG`: 1 ou 0 (padrão 1 no docker-compose)

---

## Boas práticas

* Sempre execute migrações antes de iniciar o servidor.
* Use um `.env` para segredos em produção.
* Ajuste `ALLOWED_HOSTS` em `settings.py` para seu domínio/prod.

---

## Contribuição

1. Fork do projeto
2. Crie uma branch feature: `git checkout -b feature/nova-funcionalidade`
3. Commit suas alterações: `git commit -m 'Adiciona nova funcionalidade'`
4. Push na branch: `git push origin feature/nova-funcionalidade`
5. Abra Pull Request

---

© 2025 Airline Reservation API. Todos os direitos reservados.
