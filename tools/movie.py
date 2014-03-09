"""豆瓣电影
"""

import json
from urllib.request import urlopen
from pymongo import MongoClient


class Movie():
    url = 'https://api.douban.com/v2/movie/'

    def __init__(self):
        self.db = MongoClient().bastogne

    def get_subject_by_id(self, movie_id):
        url = self.url + 'subject/' + movie_id
        response = urlopen(url)
        return json.loads(response.read().decode())

    def get_movie(self):
        movies = self.db.movie.find()

        for movie in movies:
            print(movie['id'], movie['db_id'])


if __name__ == '__main__':
    Movie().get_movie()