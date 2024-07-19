

# Django Chatbot Backend

This repository contains the backend code for a chatbot application built using Django. The backend provides endpoints for retrieving and updating chatbot settings, as well as handling user interactions.

## Features

- REST API for chatbot settings
- Support for file uploads (launcher icon, assistant image, send icon)
- Chat history storage and retrieval
- Integration with a Django admin panel

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python (v3.8 or later)
- pip (latest version)
- Django (v3.2 or later)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/django-chatbot-backend.git
   cd django-chatbot-backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install djangorestframework django-cors-headers
   ```

4. **Set up the database:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```
   
6. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

   This will start the development server at 'http://127.0.0.1:8000/'.


