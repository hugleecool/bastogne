import json
from urllib.parse import urlencode
import tornado.web
from tornado import httpclient
from tornado import gen


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    @property
    def get_douban_movie(self):
        return self.get_movie

    def get_movie(self, name):
        url = 'https://api.douban.com/v2/movie/'
        client = httpclient.AsyncHTTPClient()

        search_data = {
            'q': name,
            'start': 0,
            'count': 1,
        }
        search_url = url + 'search?' + urlencode(search_data)
        search_response = yield gen.Task(client.fetch, search_url)
        search_result = json.loads(search_response.body.decode())

        movie_id = search_result['subjects'][0]['id']

        subject_url = url + 'subject/' + movie_id
        response = yield gen.Task(client.fetch, subject_url)
        result = json.loads(response.body.decode())
        return result

