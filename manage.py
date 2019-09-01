import os
from flask_script import Manager
from app import app
manager = Manager(app)

def create_module_file(path,content):
    with open(path,'w', encoding='utf-8') as f:
        print(content,file=f)

@manager.command
def start_app(filename):
    path = os.path.join(app.config['PROJECT_DIR'], filename)
    os.mkdir(path)
    create_module_file(path+"/models.py","""from app import db,Base""")
    create_module_file(
        path+"/admin.py",
        """from flask import request 
import flask_login as login
from flask_admin.contrib.sqla import ModelView""")
    create_module_file(
        path+"/forms.py",
        """from flask_wtf import FlaskForm 
from wtforms.validators import Required""")
    create_module_file(
        path+"/views.py",
        """# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
# Import password / encryption helper tools
from flask_login import login_required, current_user, login_user,logout_user""")

if __name__ == "__main__":
    manager.run()