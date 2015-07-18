from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class SettingForm(Form):
    org_id = StringField('org_id', validators=[DataRequired()])
    cell_id= StringField('cell_id', validators=[DataRequired()])
    email_id = StringField('email_id', validators=[DataRequired()])
    
