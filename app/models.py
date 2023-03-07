from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, IntField
class Album(Document):
    name = StringField(unique=True, required=True, max_lenth=100)   
 
def __str__(self):
        return self.name
 
# class Song(Document):
#     title = StringField(max_lenth=200, required=True, unique=True)
#     rating = IntField(default=0,max_lenth=1) # 1 to 9
#     album = ReferenceField(Album)
 
#     def __str__(self):
#         return self.title
from flask import Markup, url_for
from mongoengine import Document, fields
 
class Song(Document):
    title = fields.StringField(required=True, max_length=200)
    rating = fields.IntField()
    album = fields.ReferenceField('Album')
    # for storing MP3 file of the song
    song_file = fields.FileField(required=True)
 
    def __str__(self):
        return self.title

    def download(self):
        return Markup(
                '<a href="' +
               url_for("SongsView.download", filename=str(self.song_file)) +
                '">Download</a>'
        )

    def file_name(self):
        return self.song_file.filename
