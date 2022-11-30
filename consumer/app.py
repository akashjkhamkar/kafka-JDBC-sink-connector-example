from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from kafka import KafkaConsumer

import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localedev:password@localhost:7001/localedev'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

def create_entry(data):
    new_entry = Entry()
    new_entry.start_time = data['start_time']
    new_entry.end_time = data['end_time']
    new_entry.category = data['category']
    new_entry.start_location = data['start_location']
    new_entry.end_location = data['end_location']
    new_entry.miles = data['miles']
    new_entry.purpose = data['purpose']

    db.session.add(new_entry)
    db.session.commit()

class Entry(db.Model):
    def __init__(self, start_location='', end_location=''):
        self.start_location = start_location
        self.end_location = end_location

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.String(20))
    end_time = db.Column(db.String(20))
    category = db.Column(db.String(20))
    start_location = db.Column(db.String(20))
    end_location = db.Column(db.String(20))
    miles = db.Column(db.String(20))
    purpose = db.Column(db.String(20))
 
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        db.session.commit()

        consumer = KafkaConsumer('uber-rides', bootstrap_servers='localhost:9092')

        print('now waiting for msgs..')
        for msg in consumer:
            entry_data = json.loads(msg.value)
            create_entry(entry_data)
            print('added new entry', entry_data)