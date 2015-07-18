from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from app import db, models

class SettingForm(Form):
    
    facebook_id = StringField('fb_id', validators=[DataRequired()]) 
    first_name = StringField('org_id', validators=[DataRequired()])
    last_name = StringField('org_id', validators=[DataRequired()])
    org_id = StringField('org_id', validators=[DataRequired()])
    cell_id= StringField('cell_id', validators=[DataRequired()])
    email_id = StringField('email_id', validators=[DataRequired()])

    
    def save(self):
        
        users = models.User.query.all()
        for user in users:
            if (user.fb_email == self.facebook_id):
        		#means that we have found the matchign thing 
        		#save all the shit
        	    user.first_name =  self.first_name
        	    user.last_name =  self.last_name
        	    user.org_id =  self.org_id
        	    user.cell_id =  self.cell_id
        	    user.email_id = self.email_id
        	    db.session.commit()
                #cause we're done updating

   	
    
