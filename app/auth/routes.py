from flask import render_template, redirect, flash, url_for, request
from app import db
from flask_login import logout_user, current_user, login_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from flask_babel import  _

#login form
@bp.route('/login', methods=['GET', 'POST'])
def login():
    #make sure the user cant login twice at once
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        #pull user from db
        user = User.query.filter_by(username=form.username.data).first()
        #ensure user exists & password is correct
        if user is None or not user.check_password(form.password.data):
            flash(_('Invalid username or password'))
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        #if the user was directed to login by another page, this redirects them
        #back to that page after login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth.login.html', title=_('Sign In'), form=form)

#logs user out
@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

#user creation
@bp.route('/register', methods = ['GET', 'POST'])
def register():
    #disallow user from registering while already logged in
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        #submit new user data to db
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('user registration complete')
        return redirect(url_for('auth.login'))
    return render_template('auth.registration.html', title = _('register'), form = form)
