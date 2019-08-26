from flask import request
import flask_login as login
from flask_admin.contrib.sqla import ModelView

class UserAdminView(ModelView):
    column_exclude_list = ['password', ]

    def is_accessible(self):
        return login.current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))

