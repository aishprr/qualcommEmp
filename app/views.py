from flask import render_template, flash, redirect
from app import app
from .usersetting import SettingForm
from app import db, models

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home',
                           )


@app.route('/setting', methods=['GET', 'POST'])
def setting():
    form = SettingForm()
    if form.validate_on_submit():
#        flash('Login requested for orgID="%s", cellID=%s,emailID=%s,fb_ID=%s' %
#              (form.org_id.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('usersetting.html',
                           title='Setting',
                           form=form,
                           )


#----------------------------------------
# facebook authentication
#----------------------------------------

from flask import url_for, request, session, redirect
from flask_oauth import OAuth

FACEBOOK_APP_ID = '1384575695175324'
FACEBOOK_APP_SECRET = 'def52fafef36995c6e6b874df0b7df88'

oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': ('email, ')}
)

@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')

def pop_login_session():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)

@app.route("/facebook_login")
def facebook_login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next'), _external=True))

@app.route("/facebook_authorized")
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)

    session['logged_in'] = True
    session['facebook_token'] = (resp['access_token'], '')

    user_id = ''
    user_name = ''
    #Get the facebook email 
    data = facebook.get('/me').data
    if 'id' in data and 'name' in data:
      user_id = data['id']
      user_name = data['name']

    #if a user with this email already exists, then don't do anything 
    #else add him to the database with the facebook email id

    users = models.User.query.all()

    max_id = -1
    for user in users:
      if (user.id > max_id): max_id = user.id  
      if (user.fb_email == user_id):
        #means that we have a thing 
        return redirect(next_url)
        
    new_user = models.User(id=max_id+1)
    new_user.fb_email = user_id
    db.session.add(new_user)
    db.session.commit()

    return redirect(next_url)

@app.route("/logout")
def logout():
    pop_login_session()
    return redirect(url_for('index'))
