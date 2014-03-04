"""豆瓣电影
"""

import json
from urllib.request import urlopen
from urllib.parse import urlencode


class Movie():
    url = 'https://api.douban.com/v2/movie/'

    def __init__(self):
        pass

    def get_subject_by_id(self, movie_id):
        url = self.url + 'subject/' + movie_id
        response = urlopen(url)
        return json.loads(response.read().decode())

    def search_by_name(self, name):
        """只返回一个条目
        """
        data = {
            'q': name,
            'start': 0,
            'count': 1,
        }
        url = self.url + 'search?' + urlencode(data)

        response = urlopen(url)
        return json.loads(response.read().decode())

    def get_movie(self, name):
        movie_id = self.search_by_name(name)['subjects'][0]['id']
        result = self.get_subject_by_id(movie_id)
        return result


if __name__ == '__main__':
    movie = Movie()
    m = movie.get_movie('色,戒')
    print(m)
