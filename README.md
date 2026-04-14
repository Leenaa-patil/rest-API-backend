# FastAPI Backend Assignment

## Features
- JWT Authentication
- Role-based access
- Task CRUD APIs
- Built-in Swagger docs

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Docs
Open:
http://127.0.0.1:8000/docs

## Endpoints

### Auth
POST /api/v1/auth/register
POST /api/v1/auth/login

### Tasks
GET /api/v1/tasks
POST /api/v1/tasks
PUT /api/v1/tasks/{id}
DELETE /api/v1/tasks/{id}

## Scalability
- Can be extended to microservices
- Add Redis caching
- Use load balancing (NGINX)
