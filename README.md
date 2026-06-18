# backend-app Effective Mobile

Тестовое задание на DevOps. Nginx снаружи, python-бэкенд внутри docker-сети.

Нужен Docker и docker compose (на Windows ставил Docker Desktop).

## Структура проекта

```
├── backend/
│   ├── Dockerfile
│   └── app.py
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
└── README.md
```

## Запуск

```bash
git clone https://github.com/p1xolinux/backend-app-Effective-Mobile.git
cd backend-app-Effective-Mobile
docker compose up -d --build
```

## Проверка

```bash
curl http://localhost
```

Ожидаемый ответ:

```
Hello from Effective Mobile!
```

Остановить:

```bash
docker compose down
```

## Как работает

Запрос идёт nginx (порт 80) → backend (порт 8080 внутри docker-сети).

На хост проброшен только 80 порт nginx. Backend наружу не открыт — только `expose`, без `ports`. Nginx ходит на backend по имени сервиса из compose.

Стек: python 3.11 alpine, nginx alpine, docker compose.
