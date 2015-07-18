from flask import render_template, flash, redirect
from app import app
from .usersetting import SettingForm


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
