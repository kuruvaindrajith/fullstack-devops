# Full Stack DevOps Project

Deployed a full stack application using Docker Compose on AWS EC2.

## Tech Stack
- Frontend: Nginx
- Backend: Python Flask API
- Database: MySQL
- Orchestration: Docker Compose
- Cloud: AWS EC2

## Architecture
Frontend (port 80) → Nginx Proxy → Backend (port 5000) → MySQL Database

## How to Run
```bash
docker-compose up -d --build
```
