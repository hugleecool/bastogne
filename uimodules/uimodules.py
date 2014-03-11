import tornado.web
from config.config import conf


class RandomMovie(tornado.web.UIModule):
    """随机显示
    用于侧边栏显示
    """
    def render(self, posts, show=conf['RANDOM_MOVIE_NUM']):
        if show:
            return self.render_string("uimodule/random-movie.html", posts=posts)
        else:
            #返回空，否则会显示NaN,下同
            return ''


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
    """分页导航
    只有一页时不显示分页
    当分页过多时应该只显示部分，但似乎这不是问题，是我多虑了，哈哈！
    """
    def render(self, nav):
        return self.render_string('uimodule/page-nav.html', page=nav)


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