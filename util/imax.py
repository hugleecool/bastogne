""" Fork IMax

@date 2014-03-1
"""


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from pymongo import MongoClient


class IMax():
    url = 'http://imax.im/movies/'
    error_number = 0

    def __init__(self, start=1, end=16097):
        self.start = start
        self.end = end
        self.movie = MongoClient().bastogne.movie

    def fork(self):
        for i in range(self.start, self.end):
            movie = dict()
            try:
                response = urlopen(self.url + str(i))
                restlt = BeautifulSoup(response.read())
                title = restlt.title.string
                #title[:title.find('|')]
                movie['id'] = i
                movie['title'] = title.strip('| 高清 BT下载,电驴下载,迅雷下载,在线观看 | IMAX.im')
                table = restlt.find('table', class_='table table-striped table-condensed')
                trs = table.select('tbody tr')
                download = list()
                for tr in trs:
                    tds = tr.find_all('td')
                    li = dict()
                    for td in tds:
                        if td['class'][0] == 'qu':
                            li['format'] = td.string.strip()
                        elif td['class'][0] == 'size':
                            li['size'] = td.span.string
                        elif td['class'][0] == 'name':
                            li['name'] = td.a.string
                            li['href'] = td.a['href']
                    download.append(li)
                movie['download'] = download
                self.movie.insert(movie)
                print(movie)
            except AttributeError as attrerr:
                self.error_number += 1
                print(i, attrerr)
            except HTTPError as e:
                self.error_number += 1
                print(i, e)
        print('*'*100)
        print('发生错误:', self.error_number, '条')
        print('*'*100)


if __name__ == '__main__':
    imax = IMax(27100, 27500)
    imax.fork()