"""Script to seed database"""

import os
import json
from datetime import datetime

import crud
import model
import server

os.system("dropdb posts")
os.system("createdb posts")
model.connect_to_db(server.app)
model.db.create_all()

with open('data/posts.json') as f:
    post_data = json.loads(f.read())

posts_in_db = []
for post in post_data:
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    post_title, post_text, post_date, tag = (
        post["post_title"],
        post["post_text"],
        post["post_date"],
        post["tag"]
    )
    date = datetime.strptime(post["date"], "%Y-%m-%d")
    # TODO: create a post here and append it to posts_in_db

    db_post = crud.create_post(post_title, post_text, post_date, tag)
    posts_in_db.append(db_post)

    model.db.session.add_all(posts_in_db)
    model.db.session.commit()
