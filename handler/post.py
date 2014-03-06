from tornado import gen
from .base import BaseHandler
import json
from urllib.parse import urlencode
import tornado.web
from tornado import httpclient
from tornado import gen


class PostHandler(BaseHandler):
    @gen.coroutine
    def get(self, pid):
        post = self.db.movie.find_one({'id': int(pid)})

        url = 'https://api.douban.com/v2/movie/'
        client = httpclient.AsyncHTTPClient()

        search_data = {
            'q': post['title'],
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

        douban_movie = result
        self.render('post/index.html', post=post, douban_movie=douban_movie)
        self.finish()