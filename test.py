from app import db, models

#db.create_all()
u = models.User(id=3)
db.session.add(u)


db.session.commit()

users = models.User.query.all()
print(users)
