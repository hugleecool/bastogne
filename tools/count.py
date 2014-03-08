from pymongo import MongoClient


client = MongoClient()
db = client.bastogne
collection = db.movie
movies = collection.find()

genres = {}

for movie in movies:
    for genre in movie['genres']:
        try:
            genres[genre] += 1
        except KeyError:
            genres[genre] = 1

print(genres)
db.genres.insert(genres)
