from flask import Blueprint , render_template,request,flash,jsonify,redirect,url_for
from models import *
#import flask.ext.whooshalchemy as whooshalchemy
import random
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import mailer
from flask_mail import Mail, Message
from sqlalchemy.exc import *
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

code = uuid.uuid4().hex

print(code)

login=Blueprint('login',__name__)

@login.route('/siginup',methods=['POST'])
def signup():
	fname = request.form['fname']
	uname=request.form['uname']
	email=request.form['email']
	password=request.form['psw']
	hashed_password = generate_password_hash(password, method='sha256')
	new_user=User(fullname=fname,
		username=uname,email=email,
		password=hashed_password)
	try:
		db.session.add(new_user)
		db.session.commit()
		htmlMSG='<p>Thank you for signin up with Codeside Academy your password is<p>'+str(password)+'<p>Keep it safe</p>'
		mailer.sendMsg('CodeSide Academy','CodeSide Academy',email,"Thank you for signin up with Codeside Academy",htmlMSG)
		flash("Registration Completed!!!")
		return redirect(url_for('homepage.index'))
	except IntegrityError:
		flash("Sorry user already exist")
		return redirect(url_for('homepage.index'))

@login.route('/signin',methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	user=User.query.filter_by(username=username).first()
	if user:
		if check_password_hash(user.password,password):
			login_user(user)
			return redirect(url_for('homepage.index'))
	else:
		flash("invalid username or password")
		return redirect(url_for('homepage.index'))


@login.route('/logout')
def logout():
	logout_user()
	flash("sign out successful")
	return redirect(url_for('homepage.index'))




