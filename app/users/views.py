# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
# Import password / encryption helper tools
from flask_login import login_required, current_user, login_user,logout_user
from werkzeug import check_password_hash, generate_password_hash
# Import the database object from the main app module
from app import db
# Import module forms
from app.users.forms import LoginForm, RegisterForm
# Import module models (i.e. User)
from app.users.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')
# Set the route and accepted methods
def auth_in_server(user,**kwargs):
    login_user(user=user,**kwargs)
    return redirect(url_for('auth.profile'))

@mod_auth.route('/login/', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user=user,remember=request.form.get("remember"))
            return redirect(url_for('auth.profile'))
    return render_template("auth/sign_in.html",form=form)

@mod_auth.route('/profile/', methods=['GET'])
@login_required
def profile():
    return render_template('auth/profile.html', name=current_user.name)

@mod_auth.route('/signup/', methods=['GET','POST'])
def signup():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))
        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = User(email=form.email.data, name=form.name.data, password=generate_password_hash(form.password.data, method='sha256'))
        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/sign_up.html', form=form)

@mod_auth.route('/logout/', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))