
import os
import sys

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

app = Flask(__name__)
app.config.from_object('config.ConfigDevelop')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

########################
# Configure Secret Key #
########################


def install_secret_key(app, filename='secret_key'):
    """Configure the SECRET_KEY from a file
       in the instance directory.
       If the file does not exist, print instructions
       to create it from a shell with a random key,
       then exit.
    """
    filename = os.path.join(app.instance_path, filename)
    try:
        app.config['SECRET_KEY'] = open(filename, 'rb').read()
    except IOError:
        print('Error: No secret key. Create it with:')
        full_path = os.path.dirname(filename)
        if not os.path.isdir(full_path):
            print('mkdir -p {filename}'.format(filename=full_path))
            print('head -c 24 /dev/urandom > {filename}'.format(
                filename=filename
            ))
            sys.exit(1)


if not app.config['DEBUG']:
    install_secret_key(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from .abstract_models import Base
from app.users.models import User
@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))
from app.users.views import mod_auth as usersModule
from app.main_module.views import main as mainModule
app.register_blueprint(mainModule)
app.register_blueprint(usersModule)

# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
# app.register_blueprint(commentsModule)
# app.register_blueprint(postsModule)
db.create_all()

print(app.config['SQLALCHEMY_DATABASE_URI'])
