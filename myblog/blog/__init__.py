from flask import Flask
from flask_mail import Mail, Message

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


from blog.home.views import hom
from blog.home.models import *
from blog.auth.views import login
#import flask.ext.whooshalchemy as whooshalchemy




from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy.exc import *
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
#import flask_whooshalchemy as wa


app=Flask(__name__)
app.config.from_pyfile('config.py')
app.config['WHOOSH_BASE'] = 'tmp/whoosh/base'
mail =Mail(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'
#login_manager = LoginManager()
migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#admin = Admin(app, name='Control Panel')
#admin.add_view(Blogpost, db.session)
admin = Admin(app,name='Control Panel')
admin.add_view(ControlBlogPost(Blogpost,db.session))
admin.add_view(LoadViews(Settings,db.session))
admin.add_view(LoadViews(Comment_System,db.session))
admin.add_view(LoadViews(User,db.session))
#whooshalchemy.whoosh_index(app, Blogpost)



db.init_app(app)

app.register_blueprint(home.views.hom)
app.register_blueprint(auth.views.login)