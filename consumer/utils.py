from models import Entry
from app import db

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
