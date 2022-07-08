from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String)
    is_public = db.Column(db.Boolean)

    # posts can be accessed due to line 30
    
    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'

class Post(db.Model):
    __tablename__ = "posts"
    
    post_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    post_subject = db.Column(db.Text)
    post_text = db.Column(db.Text)
    post_date = db.Column(db.DateTime)
    post_tag = db.Column(db.Text)

    user = db.relationship("User", backref="posts")
    # images can be accessed due to line 42
    def __repr__(self):
        return f"<Post post_id={self.post_id} post_text={self.post_text}>"

class Image(db.Model):
    __tablename__ = "images"

    image_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'))
    image_url = db.Column(db.String)

    post = db.relationship("Post", backref= "images")


def connect_to_db(flask_app, db_uri="postgresql:///posts", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
