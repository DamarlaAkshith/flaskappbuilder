import os
import logging
from flask import Flask
from flask_appbuilder.security.mongoengine.manager import SecurityManager
from flask_appbuilder import AppBuilder
from flask_mongoengine import MongoEngine
from .views import AlbumView,SongsView
# from config import RECAPTCHA_PRIVATE_KEY,RECAPTCHA_PUBLIC_KEY
# from app import views
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
app.config['RECAPTCHA_PUBLIC_KEY'] = os.environ.get('SITE_KEY')
app.config['RECAPTCHA_PRIVATE_KEY'] = os.environ.get('SECRET_KEY')
db = MongoEngine(app)
appbuilder = AppBuilder(app, security_manager_class=SecurityManager)

appbuilder.add_view(AlbumView, "Album View", category="Model Views")
appbuilder.add_view(SongsView, "Song View", category="Model Views")



