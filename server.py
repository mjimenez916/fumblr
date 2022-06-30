"""Server for blog app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from datetime import datetime
import re
import os
import cloudinary.uploader

CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME = "dmz6h4ain"

app = Flask(__name__)
app.secret_key = "mango"
app.jinja_env.undefined = StrictUndefined

app = Flask(__name__)

@app.route('/index')
def show_text_editor():

    return render_template('index.html')

@app.route('/')
def homepage():

    return render_template('homepage.html')

# TODO: add feature to check if user is already logged in so they dont have to login again

@app.route('/')
def check_if_user_logged_in():

    if 'current_user' in session:
        return render_template("profile.html")
    
    if 'current_user' not in session:
        redirect("/")

@app.route('/users', methods=["POST"])
def register_user():
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = crud.get_user_by_username(username)

    if user:
        flash("Cannot create an account with that username. Try again.")
    else:
        user = crud.create_user(username, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")

@app.route('/posts', methods=["POST"])
def create_post():
    post_subject = request.form.get('post_subject')
    post_text = request.form.get('post_text')
    post_date = datetime.now()
    post_tag = request.form.get('post_tag')

    post = crud.create_post(post_subject, post_text, post_date, post_tag)
    db.session.add(post)
    db.session.commit()

    return redirect("/posts")

@app.route("/posts")
def show_posts():

    posts = crud.get_all_posts()

    return render_template("posts.html", posts=posts)

@app.route("/archive")
def show_posts_by_date():

    posts = crud.get_posts_ordered_by_date()

    return render_template("archive.html", posts=posts)

@app.route("/posts/<post_id>")
def show_post_detail(post_id):
    """Show details on a particular post."""

    post = crud.get_post_by_id(post_id)

    return render_template("post_details.html", post=post)

@app.route('/login', methods = ["POST"])
def process_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = crud.get_user_by_username(username)

    if user.password == password:
        session['current_user'] = user.username
        flash("Login success!")
        return redirect("/profile")
    
    if user.password != password:
        flash("Cannot find an account with those credentials. Please try again.")
        return redirect("/")


@app.route("/logout")
def process_logout():
    """Log user out."""

    del session['current_user']
    flash("Logged out.")
    return redirect("/")

@app.route('/users')
def show_user():
    users = crud.get_all_users()
    return render_template("users.html", users=users)

@app.route('/profile')
def show_user_profile():

    return render_template("profile.html")

@app.route('/create-post')
def create_blog_post_page():

    return render_template("create-post.html")

@app.route('/query', methods =["GET"])
def search_post_by_tag():

    query = request.args.get('query')

    posts = crud.get_posts_by_tag(query)

    return render_template("query.html", query=query, posts=posts)

@app.route('/images')
def show_image():
    #Grabs images from database.
    images = crud.show_all_images()

    return render_template("images.html", images=images)


@app.route('/upload-image', methods=["POST"])
def upload_image():

    uploaded_image = request.files['uploaded-image']

    result = cloudinary.uploader.upload(uploaded_image,
            api_key=CLOUDINARY_KEY,
            api_secret=CLOUDINARY_SECRET,
            cloud_name=CLOUD_NAME)
    print(result)
    print()
    print()
    img_url = result['secure_url']
    print()
    print()
    print(img_url)

    image = crud.create_image(img_url)
    db.session.add(image)
    db.session.commit()

    return render_template("upload-image.html", uploaded_image=uploaded_image, result=result, img_url=img_url, image=image)


@app.route('/upload-image', methods=["GET"])
def show_upload_image_page():

    return render_template("upload-image.html")

@app.route('/delete-post/<post_id>', methods=["POST"])
def delete_blog_post(post_id):
    
     post = crud.delete_blog_post(post_id)
     db.session.commit()
     return redirect("/archive")

@app.route('/edit-post/<post_id>', methods=["POST"])
def edit_blog_post(post_id):
    
     post = crud.edit_blog_post(post_id)
     db.session.commit()
     return redirect("/archive")

if __name__ == "__main__":
    app.secret_key = "mango"
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)