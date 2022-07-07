from model import db, User, Post, Image, connect_to_db
from flask_sqlalchemy import SQLAlchemy


def create_user(username, password):

    user = User(username=username, password=password)

    return user

def create_post(post_subject, post_text, post_date, post_tag):

    post = Post(post_subject=post_subject, post_text=post_text, post_date=post_date, post_tag=post_tag)

    return post

def get_user_by_username(username):

    return User.query.filter(User.username == username).first()

def get_all_users():

    return User.query.all()

def get_all_posts():

    return Post.query.all()

def get_posts_ordered_by_date():

    return Post.query.order_by(Post.post_date).all()

def get_post_by_id(post_id):

    return Post.query.get(post_id)

def get_posts_by_tag(tag_name):

    return Post.query.filter(Post.post_tag == tag_name ).all()

def show_all_images():

    return Image.query.all()

def create_image(image_url):
    
    image = Image(image_url=image_url)

    return image

def delete_blog_post(post_id):

    post = Post.query.filter_by(post_id=post_id).delete()

    return post    

def edit_blog_post(post_id):

    post = Post.query.get(post_id)

    return

#TODO: pass in arguments: subject, post, tags


if __name__ == '__main__':
    from server import app
    connect_to_db(app)