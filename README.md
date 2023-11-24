# django-demo-lab
Week 5 - Lab: Build "Hello World" Django App 

Overview

This Django exercise means to create a simple web app that returns a JSON response with a "Hello World" message. It's designed as a basic example of a Django project setup and response handling.

Requirements

    Python 3.x
    Django (latest version recommended)

Installation and Setup

    Clone the Repository:

    bash

git clone [Your-Repository-URL]

Navigate to the project directory:

bash

cd [Your-Project-Directory]

Install Django:

        pip install django

Running the Application

    Start the Django server from the directory with the manage.py file:

    python manage.py runserver

    The server will start on http://127.0.0.1:8000/.

Accessing the Hello World JSON Response

    Open your browser and go to http://127.0.0.1:8000/. You can reach this by entering "http://localhost:8000/polls/" as well.
    You should see a JSON response: {"Message": "Hello World!"}.

Additional Notes

    Ensure that Python and Django are correctly installed on your system.
    For any changes in the URL patterns or views, update the corresponding urls.py and views.py files in the project.
