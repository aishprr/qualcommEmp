from app import db
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

class User(db.Model):
    id = db.Column((db.Integer), primary_key=True)
    fb_email = db.Column(db.String(80), index=True, unique=True)
    org_id = db.Column(db.String(80), index=True, unique=False)
    email_id = db.Column(db.String(80), index=True, unique=True)
    cell_id = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.fb_email)