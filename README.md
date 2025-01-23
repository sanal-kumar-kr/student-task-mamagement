# Student Management System API

This API serves as a backend for a Student Management System built with Django and Django Rest Framework (DRF). It provides an interface for admins and students to manage student data, tasks, and perform authentication using JWT (JSON Web Tokens).

## API URL

**Base URL**: `http://127.0.0.1:8000/`

### Available Endpoints:

- **Authentication**
  - `POST /auth/token/` – Obtain a JWT token.
  - `POST /auth/token/refresh/` – Refresh your JWT token.

- **Student Management (Admin Only)**
  - `GET /students/` – List all students.
  - `POST /students/` – Add a new student.
  - `GET /students/{id}/` – Get student details by ID.
  - `PUT /students/{id}/` – Update student details.
  - `DELETE /students/{id}/` – Delete student by ID.

- **Task Management (Admin Only)**
  - `POST /addtask/` – Create a new task.
  - `GET /viewtasks/` – View all tasks.
  - `GET /taskmanage/{id}/` – Get task details by ID.
  - `PUT /taskmanage/{id}/` – Update task details (Admin).
  - `DELETE /taskmanage/{id}/` – Delete task by ID.

- **Student Tasks**
  - `GET /student_tasks/` – View all tasks assigned to the logged-in student.
  - `GET /update_task/{id}/` – Get task details for the logged-in student.
  - `PUT /update_task/{id}/` – Update task status (Student).

---

## Setup Instructions

Follow the steps below to set up and run this project locally.

### 1. Clone the Repository

bash
  git clone <repository-url>
  cd <repository-folder>

### 2. Create a virtual environment to isolate your project dependencies:
bash 
  python -m venv venv
  Activate the virtual environment 
  cd <venv-name>
  cd <Scripts>
  venv\Scripts\activate
  cd..
  <!-- install requirement.text -->
  pip install -r requirements.txt

!!!make sure project folder inside the venv


### 3.make migration files and apply migrations
bash
  cd <project-folder>
  python manage.py makemigrations
  python manage.py migrate

### 4.create super user
bash
  python manage.py createsuperuser
  Username=admin@admin.com
  email=admin@admin.com
  password=admin
  confirmpassword=admin

### 5.Start the development server:
bash
  python manage.py runserver



