from pymongo import MongoClient

client = MongoClient()

db = client.bastogne

movie = db.movie

m = movie.find({'title': '美国往事'})

for i in m:
    print(i['title'])
    for download in i['download']:
        print(download['format'], download['size'], download['href'])