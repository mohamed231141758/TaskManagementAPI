# Task Management API

A RESTful API built with Django and Django REST Framework that allows users to manage their daily tasks efficiently.

## What problem does it solve?
People struggle to keep track of their tasks. This API provides a simple and secure way for users to create, manage, and track their tasks from any device.

## Features
- User registration and login with JWT authentication
- Create, read, update, and delete tasks
- Mark tasks as complete or incomplete
- Add due dates to tasks
- Filter tasks by status (completed/pending)
- Users can only see their own tasks (secure)
- 14 automated tests all passing

## Tech Stack
- Python 3.x
- Django 4.2
- Django REST Framework
- JWT Authentication (djangorestframework-simplejwt)
- SQLite (development)

## Project Structure
```
TaskManagementAPI/
├── task_manager/        
│   ├── settings.py      
│   ├── urls.py          
│   └── wsgi.py          
├── users/               
│   ├── models.py        
│   ├── views.py         
│   ├── serializers.py   
│   └── urls.py          
├── tasks/               
│   ├── models.py        
│   ├── views.py         
│   ├── serializers.py   
│   ├── tests.py         
│   └── urls.py          
├── requirements.txt     
├── manage.py            
└── README.md            
```

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

### 1. Clone the repository
```bash
git clone https://github.com/mohamed231141758/TaskManagementAPI.git
cd TaskManagementAPI
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the server
```bash
python manage.py runserver
```

### 6. Run tests
```bash
python manage.py test tasks
```

## Example API Usage

### Register a new user
```json
POST /api/auth/register/
{
    "username": "john",
    "email": "john@example.com",
    "password": "mypassword"
}
```

### Login
```json
POST /api/auth/login/
{
    "username": "john",
    "password": "mypassword"
}
```

### Create a task
```json
POST /api/tasks/
{
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "due_date": "2026-03-01"
}
```

## Testing
This project includes 14 automated tests covering:
- User registration
- User login
- Creating tasks
- Viewing tasks
- Updating tasks
- Deleting tasks
- Marking tasks complete/incomplete
- Filtering tasks by status
- Security (users cannot see other users tasks)

Run tests with:
```bash
python manage.py test tasks
```

## Author
Mohamed
GitHub: https://github.com/mohamed231141758