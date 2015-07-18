from app import db
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

class User(db.Model):
    id = db.Column((db.Integer), primary_key=True)
    first_name = db.Column(db.String(80), index=True, unique=False)
    last_name = db.Column(db.String(80), index=True, unique=False)
    fb_email = db.Column(db.String(80), index=True, unique=True)
    org_id = db.Column(db.String(80), index=True, unique=False)
    email_id = db.Column(db.String(80), index=True, unique=True)
    cell_id = db.Column(db.Integer, index=True, unique=True)

    def __init__(self, id):
        self.id = id
        
    def __repr__(self):
        return '<User %r>' % (self.id)

class Event(db.Model):
    
    id = db.Column((db.Integer), primary_key=True)
    event_name = db.Column(db.String(120), index=True, unique=False)
    event_date = db.Column(db.String(80), index=True, unique=False)
    event_location = db.Column(db.String(120), index=True, unique=False)
    event_hashtags = db.Column(db.String(120), index=True, unique=True)
    user_list = db.Column(db.String(120), index=True, unique=False)
