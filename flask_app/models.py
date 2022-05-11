from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager
from . import config
from .utils import current_time
import base64

@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()

class User(db.Document, UserMixin):
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    profile_pic = db.ImageField()
    format_pic = db.StringField()

    # Returns unique string identifying our object
    def get_id(self):
        return self.username

class Review(db.Document):
    commenter = db.ReferenceField(User, required=True)
    content = db.StringField(required=True, min_length=5, max_length=500)
    date = db.StringField(required=True)
    imdb_id = db.StringField(required=True, min_length=9, max_length=9)
    movie_title = db.StringField(required=True, min_length=1, max_length=100)

class Thread(db.Document):
    original = db.ReferenceField(User, require=True)
    topic = db.StringField(required=True, min_length=5, max_length=100)
    description = db.StringField(min_length=5, max_length=200)
    thread_image = db.ImageField()
    format_pic = db.StringField()
    genre = db.StringField(required=True)

class Post(db.Document):
    commenter = db.ReferenceField(User, required=True)
    content = db.StringField(required=True, min_length=5, max_length=500)
    date = db.StringField(required=True)
    topic = db.StringField(required=True)
    post_image = db.ImageField()

