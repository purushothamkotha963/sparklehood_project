from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import datetime
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/Incident_db'
db = SQLAlchemy(app)


class Incident(db.Model):
    id = db.Column(db.Integer,nullable = False,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable = False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(20), nullable=False)
    reported_at = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)

def create_database():
    engine = create_engine('mysql+mysqlconnector://root:@localhost/')
    con = engine.connect()

    cursor = con.connection.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS Incident_db')
    cursor.close()
    con.close()




@app.route("/")
def root():
    return render_template('main.html')


@app.route("/incidents",methods=["GET"])
def fetch_all():
    ans = Incident.query.all()
    all_incidents = {}
    for incidents in ans:
        all_incidents[incidents.id]={
            'title': incidents.title,
            'description': incidents.description,
            'severity': incidents.severity,
            'reported_at': incidents.reported_at
        }
    return jsonify(all_incidents)

@app.route("/incidents/<int:id>",methods=["GET"])
def incidentById(id):
    incidents = Incident.query.get(id)  # Fetch the user by ID using the primary key
    if incidents:
        return jsonify({
            'title': incidents.title,
            'description': incidents.description,
            'severity': incidents.severity,
            'reported_at': incidents.reported_at
        })
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/incidents', methods=["PUT"])
def update_incident():
    # Get the incident ID and new data from the request
    data = request.get_json() 

    incident_id = data.get('id')  # Getting ID from form data (can be from JSON as well)
    title = data.get('title')
    description = data.get('description')
    severity = data.get('severity')

    print(incident_id)

    # Find the incident in the database by ID
    incident = Incident.query.get(incident_id)  # Use get() to find by primary key (id)

    # If the incident is not found, return 'not found'
    if not incident:
        return jsonify({'message': 'Incident not found'}), 404

    # Update the incident details
    if title:
        incident.title = title
    if description:
        incident.description = description
    if severity:
        incident.severity = severity

    # Commit the changes to the database
    db.session.commit()

    return jsonify({
        'message': 'Incident updated successfully',
        'updated_data':{
        'id': incident.id,
        'title': incident.title,
        'description': incident.description,
        'severity': incident.severity
    }}), 200

@app.route('/hit_update', methods=["POST"])
def hit_update():
    incident_id = request.form.get('id')
    title = request.form.get('title')
    description = request.form.get('description')
    severity = request.form.get('severity')

    # Create a dictionary with the form data
    data = {
        'id': incident_id,
        'title': title,
        'description': description,
        'severity': severity
    }

    url = f'http://127.0.0.1:5000/incidents'

    response = requests.put(url, json=data)

    return jsonify(response.json()), response.status_code



@app.route("/incidents",methods=["POST"])
def add_incident():
    title = request.form.get('title')
    description = request.form.get('description')
    severity = request.form.get('severity')

    new_incident =Incident(title=title,description=description,severity=severity)
    db.session.add(new_incident)
    db.session.commit()
    return f'successfully inserted with id = {new_incident.id}'


@app.route('/incidents/<int:id>', methods=["DELETE"])
def delete_incident(id):
    incident = Incident.query.get(id)
    if incident:
        db.session.delete(incident)
        db.session.commit()
        return jsonify({'message': 'Incident deleted successfully'}), 200
    else:
        return jsonify({'message': 'Incident not found'}), 404


@app.route('/delete', methods=["POST"])
def hit_del():
    id = request.form.get('id')
    url = f'http://127.0.0.1:5000/incidents/{id}'
    response = requests.delete(url)

    return jsonify(response.json()),response.status_code

if __name__ == '__main__':
    create_database()
    with app.app_context():
        db.create_all()

    app.run(debug=True)
