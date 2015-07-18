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

users = models.User.query.all()

for user in users:
	print(user.fb_email)
    print(user.first_name)

print(users)
'''
'''
db.create_all()

u0 = models.Event(id=1)
u0.event_name = 'Grace Hopper'
u0.date = '24th Aug 2015'
u0.location = '175 5th Avenue NYC'
u0.hashtags = '#grace15'

db.session.add(u0)

db.session.commit()
events = models.Event.query.all()
print(events)



u0 = models.Event(id=1)
u0.event_name = 'Gap Jumpers'
u0.date = '29th Aug 2015'
u0.location = '42 East 42 St, Madison Avenue NYC'
u0.hashtags = '#GapJumpers15'

db.session.add(u0)

db.session.commit()
events = models.Event.query.all()
print(events)


u0 = models.Event(id=2)
u0.event_name = 'AndyToronto'
u0.date = '3rd Sep 2015'
u0.location = '42 East 42 St, Madison Avenue NYC'
u0.hashtags = '#AndyToronto15'

db.session.add(u0)

db.session.commit()
events = models.Event.query.all()
print(events)
'''