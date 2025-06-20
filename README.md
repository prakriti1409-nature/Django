# Django Backend Project with DRF, Celery, and Telegram Bot

This is a Django-based backend project that includes:

- Django REST Framework (DRF)
- Token-based Authentication (JWT or DRF token)
- Celery with Redis for background tasks
- Telegram bot integration
- Docker & Docker Compose setup

---

## 🚀 Features

- User registration & login APIs
- Protected & public API endpoints
- Telegram bot `/start` command integration
- Background email sending after registration
- Dockerized for easy deployment

---

## 🔧 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. Create .env File

```bash
SECRET_KEY=your_django_secret_key
DEBUG=True

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

### 3. Build and Start Containers
```bash
docker compose up --build
```

### api_endpoints:
  - method: POST
    endpoint: /users/register/
    description: Register a new user
  - method: POST
    endpoint: /users/login/
    description: Login (returns auth token)
  - method: GET
    endpoint: /users/profile/
    description: Authenticated user profile
  - method: GET
    endpoint: /api/public/
    description: Public endpoint (no authentication required)

### authentication:
  token_header: "Authorization: Token your_token_here"

### telegram_bot:
  create_bot: "@BotFather"
  env_variable: "TELEGRAM_BOT_TOKEN=your_bot_token"
  integration_steps:
    - Create bot using BotFather
    - Add bot token to .env file
    - Start bot and send /start command
    - Telegram username is saved to database

### background_tasks:
  task_name: Send Welcome Email
  tool: Celery + Redis
  trigger_code: send_welcome_email.delay(user.email, user.username)

### technologies:
  - Python: "3.10"
  - Django: "5.x"
  - Django REST Framework
  - Celery
  - Redis
  - Docker
  - Docker Compose
  - Telegram Bot API

### project_structure:
  backend/:
    - settings.py: Environment-based config
    - celery.py: Celery setup
    - urls.py: URL routing
  api/: General API app (public/protected views)
  users/:
    - models.py: CustomUser model
    - views.py: Register/Login/Profile views
    - tasks.py: Celery email task
  files:
    - docker-compose.yml
    - Dockerfile
    - requirements.txt
    - .env.example

### contributing:
  - Pull requests welcome
  - For major changes, open an issue first


![image](https://github.com/user-attachments/assets/a1d7f99e-0795-4383-b47b-93a8c4277c22)
![image](https://github.com/user-attachments/assets/17fc5842-d807-4108-875d-02a7cc4b94e3)
![image](https://github.com/user-attachments/assets/ecab95cf-0f02-407e-b251-a47576abb082)
![image](https://github.com/user-attachments/assets/a925eecc-1016-4cad-b784-932364ccdc00)
![image](https://github.com/user-attachments/assets/76f4c0df-73e3-40ce-8040-5dd9b64af4d5)


