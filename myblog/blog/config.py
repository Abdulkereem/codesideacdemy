userpass = 'mysql://root:@'
basedir = '127.0.0.1'

#basedir = '192.168.1.139'
dbname = '/computer'


SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/blog.db' #userpass + basedir + dbname 

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'Abdulkereem_Halimat'

WHOOSH_BASE = 'whoosh'


MAIL_SERVER='smtp.gmail.com'
MAIL_USERNAME='codesideacademy@gmail.com'
MAIL_PASSWORD='Abdulkereem22'
MAIL_DEFAULT_SENDER = 'CodeSide Academy'
MAIL_PORT=465
MAIL_USE_SSL=True
MAIL_USE_TLS=False


#userpass = 'mysql://root:@'
#basedir = '127.0.0.1'

#basedir = '192.168.1.139'
#dbname = '/locker'


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////temp/test.db'#userpass + basedir + dbname  #userpass + basedir + dbname #