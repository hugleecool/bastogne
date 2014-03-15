import tornado.web
from config.config import conf


class Genres(tornado.web.UIModule):
    def render(self, genres, show=True):
        if show:
            return self.render_string('uimodule/genres.html', genres=genres)
        else:
            return ''


class Year(tornado.web.UIModule):
    def render(self, year=conf['YEAR'], show=True):
        if show:
            return self.render_string('uimodule/year.html', year=year)
        else:
            return ''


class PageNav(tornado.web.UIModule):
    def render(self, page_nav):
        page_nav['num'] = page_nav['count'] // conf['MOVIE_NUM'] if page_nav['count'] % conf['MOVIE_NUM'] == 0 \
            else page_nav['count'] // conf['MOVIE_NUM'] + 1
        return self.render_string('uimodule/page-nav.html', **page_nav)


class SameKindMovie(tornado.web.UIModule):
    """同类型影片
    """
    def render(self, posts, show=True):
        return self.render_string('uimodule/same-kind-movie.html', posts=posts)


class HotMovie(tornado.web.UIModule):
    """热门影片
    """
    def render(self, posts):
        return self.render_string('uimodule/hot-movie.html', posts=posts)


class ChangYan(tornado.web.UIModule):
    """热门影片
    """
    def render(self):
        return self.render_string('uimodule/changyan.html')