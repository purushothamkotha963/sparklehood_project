# sparklehood_project
This is a simple Incident Management System built with Flask, SQLAlchemy, and MySQL.
It allows users to Create, Read, Update, and Delete (CRUD) incident reports.

Features
Add new incidents

View all incidents or a specific incident by ID

Update existing incident details

Delete incidents

Frontend HTML forms for inserting and updating incidents

API endpoints returning JSON responses

Automatic database creation if it does not exist

Tech Stack
Python 3

Flask

SQLAlchemy ORM

MySQL (via mysql-connector)

HTML (templates)

Requests library for internal API hits

Setup Instructions
Prerequisites
Python installed

MySQL installed and running locally

Basic knowledge of Flask

Install required libraries
bash
Copy
Edit
pip install Flask Flask-SQLAlchemy mysql-connector-python requests
Database Configuration
Make sure MySQL is running.

The app uses these connection settings by default:

Username: root

Password: (empty)

Host: localhost

Database: Incident_db

You can change the SQLALCHEMY_DATABASE_URI in app.config if needed.

The app will automatically create the Incident_db database and the necessary tables on the first run.

How to Run
bash
Copy
Edit
python app.py
The app will start at:

cpp
Copy
Edit
http://127.0.0.1:5000/
API Endpoints

Method	Endpoint	Description
GET	/incidents	Fetch all incidents
GET	/incidents/<id>	Fetch a specific incident by ID
POST	/incidents	Add a new incident (via form)
PUT	/incidents	Update an incident (via JSON)
DELETE	/incidents/<id>	Delete an incident by ID
POST	/hit_update	Update incident via form (internally uses PUT)
POST	/delete	Delete incident via form (internally uses DELETE)
