import requests
from tmdb import URLMaker


def popular_count():
    key = 'c4ee76695f8af7078e89ed5b529516ff'
    url = URLMaker(key)
    url = url.get_url()
    res = requests.get(url)
    movie_list = res.json()
    return len(movie_list.get('results'))


if __name__ == '__main__':
    print(popular_count())