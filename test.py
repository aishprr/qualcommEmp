from app import db, models

#db.create_all()

#u = models.User(id=3)
#db.session.add(u)


#db.session.commit()

'''
user_id = "aish_premrenu@yahoo.co.in"
users = models.User.query.all()

print users

max_id = -1
for user in users:
    if (user.id > max_id): max_id = user.id  
    if (user.fb_email == user_id):
        #means that we have a thing 
    	print('FOUND IT');

new_user = models.User(id=max_id+1)
new_user.fb_email = user_id
db.session.add(new_user)
db.session.commit()
'''
users = models.User.query.all()
for user in users:
	print(user.fb_email)

print(users)
