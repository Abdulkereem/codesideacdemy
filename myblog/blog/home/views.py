from flask import Blueprint , render_template,request,flash,jsonify
from models import *
#import flask.ext.whooshalchemy as whooshalchemy
import random
import uuid
code = uuid.uuid4().hex
print(code)

hom=Blueprint('homepage',__name__)



@hom.route('/')
@hom.route('/home')
def index():
	config=Settings.query.first()
	page = request.args.get('page',1,type=int)
	#post = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
	#post = Blogpost.query.paginate(per_page=5,page=page,error_out=True)
	post = Blogpost.query.order_by(Blogpost.date_posted.desc()).paginate(per_page=5,page=page,error_out=True)
	#threads = Blogpost.query.paginate(per_page=5,page=1,error_out=True)
	#threads=Blogpost.query.order_by(Blogpost.date_posted.desc()).paginate(per_page=5,page=1,error_out=True)
	return render_template('home/index.html',config=config,post=post)

@hom.route('/article/<int:post_id>')
def article(post_id):
	config=Settings.query.first()
	poster = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
	#threads = Blogpost.query.paginate(per_page=5,page=post_id,error_out=True)
	config=Settings.query.first()
	post = Blogpost.query.filter_by(id=post_id).one()
	comment_api=Comment_System.query.first()
	#threads=Blogpost.query.order_by(Blogpost.date_posted.desc()).paginate(per_page=5,page=post_id,error_out=True)
	return render_template('home/single.html',
		post=post,config=config,
		comment_api=comment_api,poster=poster)
"""

@hom.route('/search')
def search():
	threads=Blogpost.query.whoosh_search(request.args.get('query'))
	config=Settings.query.first()
	post = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
	return render_template('home/test.html',threads=threads,
		post=post,config=config)
"""






@hom.route('/post/<int:post_id>')
def post(post_id):
	config=Settings.query.first()
	post = Blogpost.query.filter_by(id=post_id).one()
	comment_api=Comment_System.query.first()

	return render_template('home/single.html',post=post,
		config=config,
		comment_api=comment_api)

@hom.route('/golive')
def golive():
	config=Settings.query.first()
	return redirect(url_for('homepage.live',code=code,config=config))
@hom.route('/live/<code>')
def live(code):
	config=Settings.query.first()
	comment_api=Comment_System.query.first()
	return render_template('./home/live.html',
		config=config,
		comment_api=comment_api)





@hom.route('/createdb')
def createdb():
	db.create_all()
	return("done")

@hom.route('/emptydb')
def emptydb():
	db.drop_all()
	return("Deleted")