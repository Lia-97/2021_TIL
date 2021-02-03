import requests
from tmdb import URLMaker
from pprint import pprint
from operator import itemgetter

def ranking():
    # 발급받은 key
    key = 'c4ee76695f8af7078e89ed5b529516ff'
    # url 이라는 클래스 인스턴스를 만든다.
    url = URLMaker(key)
    # popular url 불러오기
    url = url.get_url(language='ko')
    # url 요청
    res = requests.get(url)
    # 요청한 url 딕셔너리로 변환
    movie_list = res.json()
    
    # operator 모듈을 활용해 movie_list의 results 값을 vote_average 가 높은 순(reverse =  True)대로 정렬하고 반환.
    rank = sorted(movie_list.get('results'), key = itemgetter('vote_average'), reverse=True)
    
    # rank 에서 상위 5개 반환
    return rank[0:5]



if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())