"""Script to seed database."""

import os  
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []

for movie in movie_data:
    title = movie["title"]
    overview = movie["overview"]
    poster_path = movie["poster_path"]
   
    # We aren't actually using release_date since datetime was causing us problems,
    # the stuff below is just for practice, but won't be passed.
    not_release_date = movie["release_date"]
    # "2020-03-13"
    format = "%Y-%m-%d"
    release_date = datetime.strptime(not_release_date, format)

    # db_movie is the movie we create using CRUD for each of the json dictionaries
    db_movie = crud.create_movie(title, overview, poster_path)

    movies_in_db.append(db_movie)

users_in_db = []
ratings_in_db = []

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    db_user = crud.create_user(email, password)

    users_in_db.append(db_user)

    # each of these loops will make a new rating (10 total).
    for i in range(10):
        random_movie = choice(movies_in_db)
        random_score = randint(1, 5)

        rating = crud.create_rating(db_user, random_movie, random_score)
        ratings_in_db.append(rating)
    #print(rating)









  