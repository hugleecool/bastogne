from .base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, page=0):
        page = int(page)
        posts = self.db.movie.find().skip(self.conf['POST_NUM'] * page).limit(self.conf['POST_NUM'])
        posts_count = posts.count()
        page_number = posts_count / self.conf['POST_NUM'] if posts_count % self.conf['POST_NUM'] == 0 \
            else posts_count // self.conf['POST_NUM'] + 1
        if page > page_number:
            self.write_error(404)
        else:
            self.render('index/index.html', posts=posts, side=self.get_side(), page=page)


class MovieHandler(BaseHandler):
    def get(self):
        page = int(self.get_argument('page', 0))
        year = self.get_argument('year', '')
        director = self.get_argument('director', '')
        cast = self.get_argument('cast', '')
        genre = self.get_argument('genre', '')

        query = {}

        if year is not '':
            query['year'] = year
        if director is not '':
            query['directors'] = director
        if cast is not '':
            query['casts'] = cast
        if genre is not '':
            query['genres'] = genre

        posts = self.db.movie.find(query).skip(10*page).limit(10)
        self.render('index/index.html', posts=posts, side=self.get_side(), page=page)


class SearchHandler(BaseHandler):
    def get(self):
        self.render('index/search.html')