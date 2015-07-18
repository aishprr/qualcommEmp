from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from app import db, models

class SettingForm(Form):
    
    first_name = StringField('org_id', validators=[DataRequired()])
    last_name = StringField('org_id', validators=[DataRequired()])
    org_id = StringField('org_id', validators=[DataRequired()])
    cell_id= StringField('cell_id', validators=[DataRequired()])
    email_id = StringField('email_id', validators=[DataRequired()])

    '''
    def save(self):
    	data = facebook.get('/me').data
    	
    	if 'id' in data: 
			user_id = data['id']

		#users = models.User.query.all()
		users = array()
		users = array()
		for user in users:
      		if (user.fb_email == user_id):
        		#means that we have found the matchign thing 
        		#save all the shit
        		user.first_name =  self.first_name
        		user.last_name =  self.last_name
        		user.org_id =  self.org_id
        		user.cell_id =  self.cell_id
        		user.email_id = self.email_id

    			db.session.update(user)
    			db.session.commit()
    			#cause we're done updating
    			break
   	'''

    
