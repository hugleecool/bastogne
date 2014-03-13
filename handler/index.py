from urllib.parse import urlencode
from .base import BaseHandler


class MovieHandler(BaseHandler):
    def get(self):
        page = int(self.get_argument('page', 0))
        year = self.get_argument('year', '')
        directors = self.get_argument('directors', '')
        casts = self.get_argument('casts', '')
        genres = self.get_argument('genres', '')

        query = {}

        if year is not '':
            query['year'] = year
        if directors is not '':
            query['directors'] = directors
        if casts is not '':
            query['casts'] = casts
        if genres is not '':
            query['genres'] = genres

        posts = self.db.movie.find(query).skip(self.conf['MOVIE_NUM'] * page).limit(self.conf['MOVIE_NUM'])\
            .sort([('id', 1)])

        if not posts.count():
            self.send_error(404)
        else:
            page_nav = {
                'page': page,
                'count': posts.count(),
                'url': '/movie?' + urlencode(query)
            }
            self.render('index/index.html', posts=posts, side=self.get_side(), page_nav=page_nav)


class SearchHandler(BaseHandler):
    def get(self):
        q = self.get_argument('q', '')
        page = self.get_argument('page', 0)
        posts = self.db.movie.find({'$or': [{'title': q}, {'casts': q}, {'directors': q}]})\
            .skip(self.conf['MOVIE_NUM'] * page).limit(self.conf['MOVIE_NUM'])\
            .sort([('id', 1)])

        if not posts.count():
            self.send_error(404)
        else:
            page_nav = {
                'page': page,
                'count': posts.count(),
                'url': '/movie?' + urlencode({'q': q})
            }
            self.render('index/index.html', posts=posts, side=self.get_side(), page_nav=page_nav)


class LoginHandler(BaseHandler):
    def get(self):
        self.render('index/login.html', side=self.get_side())

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')


class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        pass