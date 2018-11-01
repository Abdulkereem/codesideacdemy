from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_admin.form import SecureForm
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from flask import abort
#import flask_whooshalchemy as wa
import random
#import flask.ext.whooshalchemy as whooshalchemy

db = SQLAlchemy()

prettyfy="<pre class='prettyprint'></pre>"
class Blogpost(db.Model,UserMixin):
    __searchable__ = ['title', 'content']
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(500))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    image_url = db.Column(db.String(20000000000000))
    content = db.Column(db.Text, default=prettyfy)
    total_read = db.Column(db.Integer, default=0)

class Settings(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    blogname = db.Column(db.String(50))
    slogan = db.Column(db.String(500))
    myurl = db.Column(db.String(2000))
    about_me = db.Column(db.Text)
    about_blog = db.Column(db.Text)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname=db.Column(db.String(500))
    username = db.Column(db.String(222),unique=True)
    email=db.Column(db.String(300),unique=True)
    password=db.Column(db.String(500))
    role=db.Column(db.String(10),default=0)

class Comment_System(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    api_name = db.Column(db.String(50))
    purpose = db.Column(db.String(500))
    code = db.Column(db.Text)

class Coin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    api_name = db.Column(db.String(50))
    purpose = db.Column(db.String(500))
    code = db.Column(db.Text)





class LoadViews(ModelView):
    def is_accessible(self):
        try:

            if current_user.role ==1:
                return current_user.is_authenticated
            else:
                return self.inaccessible_callback(abort(404)) #redirect(url_for('member.dashbaoord'))
        except AttributeError:
            return self.inaccessible_callback(abort(404))




    def inaccessible_callback(self, name, **kwargs):
        if current_user.AnonymousUserMixin:
            return redirect(url_for('homepage.index'))
        # redirect to login page if user doesn't have access
    #column_searchable_list = ['first_name','last_name','username']




class ControlBlogPost(ModelView):
    def BlogpostControl(self):
        try:

            if current_user.role ==1:
                return current_user.is_authenticated
            else:
                return self.inaccessible_callback(abort(404))
        except AttributeError:
            return self.inaccessible_callback(abort(404))



    create_modal = True
    edit_modal = True
    can_create = True
    can_edit = True
    can_delete = True
    can_export = True
    can_view_details = True
    column_exclude_list = ['content']
    form_base_class = SecureForm
    column_searchable_list = ['title','content']

