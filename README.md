# Django To-Do App

A simple, user-friendly To-Do application built with Django, enabling users to add, update, and delete tasks. This app can be used as a personal productivity tool or as a foundation for more complex task management applications.

## Features

- **User Authentication**: Login and logout functionality.
- **CRUD Functionality**: Users can create, read, update, and delete tasks.
- **Task Completion Status**: Mark tasks as complete or incomplete.
- **Search Functionality**: Search tasks by keywords.
- **Responsive UI**: Styled with HTML and CSS for a clean and responsive design.

## Prerequisites

- Python 3.7+
- Django 3.2+
- Git
- (Optional) A PostgreSQL database for production

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **Create a Virtual Environment**:
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install Dependencies**:
    pip install -r requirements.txt

4. **Set Up Environment Variables**:

    Create a .env file in the root directory and add a SECRET_KEY for Django.
    Example .env:
        plaintext
        Copy code
        SECRET_KEY=your_secret_key
        DEBUG=True

5. **Run Migrations**:

        bash
        Copy code
        python manage.py migrate

6. **Create a Superuser (to access Django admin)**:

        bash
        Copy code
        python manage.py createsuperuser

7. **Run the Development Server**:

    bash
    Copy code
    python manage.py runserver


Open http://127.0.0.1:8000 in your browser to access the app.

**Project Structure**
1) base/ - Main app folder containing views, models, and templates.
2) templates/ - HTML templates for the app’s UI.
3) static/ - Static files like CSS and JavaScript.
4) manage.py - Django’s command-line utility for administrative tasks.

**Usage**
1) Register for a new account or login if you already have one.
2) Add tasks using the "Add Task" button.
3) Update or delete tasks as needed.
4) Search tasks using keywords.

