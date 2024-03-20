# Task Management System

This is a Task Management System built using Django and Django Rest Framework (DRF). It allows users to create, update, delete, and assign tasks, with support for asynchronous task processing using Celery.

## Features

- User Authentication: Users can register, login, and logout.
- Task Management: Users can create tasks with title, description, due date, priority, and assign them to other users. They can also view, edit, and delete tasks.
- Asynchronous Task Processing: Email notifications are sent asynchronously using Celery when tasks are created or updated.
- RESTful API: Implements CRUD operations on tasks via a RESTful API using DRF.
- Unit Tests: Comprehensive unit tests ensure reliability and correctness of functionalities.

## Requirements

- Python 3.x
- Django
- Django Rest Framework
- Celery
- Redis (for Celery broker)
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task-management-system.git
   cd task-management-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Django settings:
   - Set up database settings, Celery settings, and other configurations in `settings.py`.

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start Celery worker:
   ```bash
   celery -A task_management_system worker --loglevel=info
   ```

6. Run Django server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at http://localhost:8000/

## Usage

- Register a new user or login with existing credentials.
- Create tasks, assign them to users, and manage tasks.
- Access the API endpoints for CRUD operations on tasks.
- Explore different functionalities and features of the application.

## API Endpoints

- **GET /api/tasks/**
  - List all tasks.

- **POST /api/tasks/**
  - Create a new task.

- **GET /api/tasks/{task_id}/**
  - Retrieve details of a specific task.

- **PUT /api/tasks/{task_id}/**
  - Update details of a specific task.

- **DELETE /api/tasks/{task_id}/**
  - Delete a specific task.

- Other endpoints for user authentication and management.

## Testing

- Run unit tests using:
  ```bash
  python manage.py test
  ```
  
