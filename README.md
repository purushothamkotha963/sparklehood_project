# Incident Management System using Flask and MySQL
This is a simple Incident Management System built with Flask, SQLAlchemy, and MySQL.
It allows users to Create, Read, Update, and Delete (CRUD) incident reports.

## Features
Add new incidents

View all incidents or a specific incident by ID

Update existing incident details

Delete incidents

Frontend HTML forms for inserting and updating incidents

API endpoints returning JSON responses

Automatic database creation if it does not exist

## Tech Stack
Python 3

Flask

SQLAlchemy ORM

MySQL (via mysql-connector)

HTML (templates)

Requests library for internal API hits

## Setup Instructions
Prerequisites
Python installed
MySQL installed and running locally
Basic knowledge of Flask

Install required libraries
bash
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

python app.py

The app will start at:
http://127.0.0.1:5000/
