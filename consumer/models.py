from app import db

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

