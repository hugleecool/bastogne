from pymongo import MongoClient
from movie import Movie

client = MongoClient()
db = client.bastogne
collection = db.movie

douban_movie = Movie()

movies = collection.find({'id': {'$gt': 16640}})
# movies = collection.find()

for m in movies:
    print(m['id'], m['title'], end=' ')
    try:
        mv = douban_movie.get_movie(m['title'])
        print(mv['id'], end=' ')

        directors = list()
        for director in mv['directors']:
            directors.append(director['name'])

        casts = list()
        for cast in mv['casts']:
            casts.append(cast['name'])

        data = {
            'douban_id': mv['id'],
            'alt': mv['alt'],
            'rating': mv['rating']['average'],
            'image': mv['images']['large'],
            'year': mv['year'],
            'genres': mv['genres'],
            'countries': mv['countries'],
            'summary': mv['summary'],
            'directors': directors,
            'casts': casts,
        }
        print(data)
        collection.update({'id': m['id']}, {'$set': data})
    except IndexError:
        collection.remove({'id': m['id']})
        print('has remove')