# Backend API Project

## Features
- User Authentication (JWT)
- Role-Based Access Control
- Task CRUD APIs
- Secure Password Hashing

## Setup

```bash
npm install
npm run dev
```

## Environment Variables
Create a `.env` file:

```
MONGO_URI=your_mongodb_connection
JWT_SECRET=your_secret_key
```

## API Endpoints

### Auth
- POST /api/v1/auth/register
- POST /api/v1/auth/login

### Tasks
- GET /api/v1/tasks
- POST /api/v1/tasks
- PUT /api/v1/tasks/:id
- DELETE /api/v1/tasks/:id

## Scalability Notes
- Can be split into microservices
- Add Redis for caching
- Use load balancers like NGINX
- Database scaling via sharding/replication
