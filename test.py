from app import db, models

#db.create_all()

#u = models.User(id=3)
#db.session.add(u)


#db.session.commit()
'''
user_id = "aish_premrenu@yahoo.co.in"

users = models.User.query.all()

print users

for user in users:
    print(user.id)
    print(user.first_name)
    print(user.last_name)
    print(user.fb_email)
    print(user.org_id)
    print(user.email_id)
    print(user.cell_id)
    if(user!=0 or user!=1):
    	user.first_name = input("first_name")
    	user.last_name = input("last_name")
    	user.fb_email = input("fb_email")
    	user.org_id = input("org_id")
    	user.email_id = input("email_id")
    	user.cell_id = int(input("cell_id"))
    
    #db.session.update(user)
    db.session.commit();
        
print(users)


new_user = models.User(id=max_id+1)
new_user.fb_email = user_id
db.session.add(new_user)
db.session.commit()

users = models.User.query.all()

for user in users:
	print(user.fb_email)
    print(user.first_name)

print(users)

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
events = models.Event.query.all()
for event in events: 
	print(event.event_name)

print(events)

'''
users = models.User.query.all()
for user in users:
	
    print(user.id)
    print(user.first_name)
    print(user.last_name)
    print(user.fb_email)
    print(user.org_id)
    print(user.email_id)
    print(user.cell_id)
    '''
	if(user.id == 6):

		(user.first_name = "wwwewe"
		user.last_name = "ewjeb"
		user.fb_email = "l23h23@gmail.com"
		user.org_id ="WinECE, UC Davis"
		user.email_id = "sdmnsld@gmail.com"
		user.cell_id = 2392929111
    
		db.session.commit();
	'''
'''
events = models.Event.query.all()
for event in events:
    if(event.id == 2):
        event.user_list = "[0,5,6,2]"
        db.session.commit()

'''