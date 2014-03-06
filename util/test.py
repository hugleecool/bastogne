from pymongo import MongoClient
from movie import Movie

client = MongoClient()
db = client.bastogne
collection = db.movie

douban_movie = Movie()

movies = collection.find().skip(12680).limit(5000)
# movies = collection.find({'id': 236})

for m in movies:
    print(m['id'], m['title'], end=' ')
    try:
        print(douban_movie.get_movie(m['title'])['id'])
    except IndexError:
        collection.remove({'id': m['id']})
        print('has remove')