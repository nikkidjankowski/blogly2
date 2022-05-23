"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)


    first_name = db.Column(db.String(50),
                    nullable=False,
                    unique=True) 

    last_name = db.Column(db.String(50),
                    nullable=False,
                    unique=True) 

    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)


    title = db.Column(db.String(50),
                    nullable=False,
                    unique=True) 

    content = db.Column(db.String(50),
                    nullable=False,
                    unique=True) 

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def friendly_date(self):
        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")




def connect_db(app):
    db.app = app
    db.init_app(app)