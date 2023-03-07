from app.models import Album, Song
# from app import appbuilder
from flask_appbuilder import ModelView
from flask_appbuilder.models.mongoengine.interface import MongoEngineInterface
from flask import Markup, url_for
# class SongsView(ModelView):
#     datamodel = MongoEngineInterface(Song)
class SongsView(ModelView):
    datamodel = MongoEngineInterface(Song)

    label_columns = {"file_name": "File Name", "download": "Download"}
    list_columns = ["title", "file_name", "download"]
    show_columns = ["title", "file_name", "download"]


class AlbumView(ModelView):
    datamodel = MongoEngineInterface(Album)

