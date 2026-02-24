# Task Management API

A RESTful API built with Django and Django REST Framework that allows users to manage their tasks.

## Features
- User registration and login (JWT authentication)
- Create, read, update, and delete tasks
- Mark tasks as complete or incomplete
- Filter tasks by status (completed/pending)
- Users can only see their own tasks

## Tech Stack
- Python 3.x
- Django 4.2
- Django REST Framework
- JWT Authentication
- SQLite (development)

## API Endpoints

### User Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and get token |

### Task Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/` | Get all my tasks |
| POST | `/api/tasks/` | Create a new task |
| GET | `/api/tasks/{id}/` | Get one task |
| PUT | `/api/tasks/{id}/` | Update a task |
| DELETE | `/api/tasks/{id}/` | Delete a task |
| POST | `/api/tasks/{id}/complete/` | Mark task as complete |
| POST | `/api/tasks/{id}/incomplete/` | Mark task as incomplete |

## Getting Started

### 1. Create a virtual environment
bash
python -m venv venv
venv\Scripts\activate

### 2. Install dependencies
bash
pip install -r requirements.txt

### 3. Run migrations
bash
python manage.py migrate

### 4. Start the server
bash
python manage.py runserver

## Author
Your Name Here