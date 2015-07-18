from app import db
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

class User(db.Model):
    id = db.Column((db.Integer), primary_key=True)
    fb_email = db.Column(db.String(80), index=True, unique=True)
    org_id = db.Column(db.String(80), index=True, unique=False)
    email_id = db.Column(db.String(80), index=True, unique=True)
    cell_id = db.Column(db.Integer, index=True, unique=True)

    def __init__(self, id):
        self.id = id
        #self.fb_email = fb_email
        #self.org_id = org_id
        #self.email_id = email_id
        #self.cell_id = cell_id


    def __repr__(self):
        return '<User %r>' % (self.id)
