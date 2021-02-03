import requests
from tmdb import URLMaker
from pprint import pprint


def vote_average_movies():
    # 발급받은 key
    key = 'c4ee76695f8af7078e89ed5b529516ff'
    # url 이라는 클래스 인스턴스를 만든다.
    url = URLMaker(key)
    # get_url 메서드를 사용해 popular url 을 가져온다.
    url = url.get_url(language='ko')
    # url 을 요청하고
    res = requests.get(url)
    # 딕셔너리 형태로 저장한다.
    movie_list = res.json()

    # 반환값을 담을 빈 리스트를 만든다.
    avg_above8 = []
    # movie_list 에서 result 키값을 movie20 변수에 담는다.
    movie20 = movie_list.get('results')
    # movie20 을 순회하면서
    for movie in movie20:
        # 각 원소(딕셔너리)의 vote_average 키값이 8 이상이라면
        if movie.get('vote_average') >= 8:
            # 해당 딕셔너리 정보를 movie 에 추가한다.
            avg_above8.append(movie)
    
    return avg_above8

    



if __name__ == '__main__':
    pprint(vote_average_movies())    
