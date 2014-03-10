"""豆瓣电影
"""

import json
from urllib.request import urlopen
from urllib.error import HTTPError
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
            if movie.get('alt'):
                pass
            else:
                try:
                    douban_movie = self.get_subject_by_id(movie['db_id'])
                    mv = dict()
                    mv['alt'] = douban_movie['alt']
                    mv['rating'] = douban_movie['rating']['average']
                    mv['image'] = douban_movie['images']['large']
                    mv['year'] = douban_movie['year']
                    mv['countries'] = douban_movie['countries']
                    mv['genres'] = douban_movie['genres']

                    mv['directors'] = []

                    for director in douban_movie['directors']:
                        mv['directors'].append(director['name'])

                    mv['casts'] = []

                    for cast in douban_movie['casts']:
                        mv['casts'].append(cast['name'])

                    mv['summary'] = douban_movie['summary']

                    self.db.movie.update({'id': movie['id']}, {'$set': mv})

                    print(movie['id'], end=' ')
                    print(mv)
                except HTTPError as e:
                    self.db.movie.remove({'id': movie['id']})
                    print(movie['id'], e, 'has remove')


if __name__ == '__main__':
    Movie().get_movie()