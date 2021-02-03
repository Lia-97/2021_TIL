import json
from pprint import pprint

def max_revenue(movies):
    # high_revenue 0으로 초기화
    high_revenue = 0
    # high_revenue 인 movie title 을 넣을 high_movie 초기화
    high_movie = ''
    # movies의 각 id 를 파일명으로 하는 json 파일 open
    for movie in movies:
        revenue_json = open('data/movies/' + str(movie.get('id')) + '.json', encoding='UTF8')
        revenue = json.load(revenue_json)
        # 각 영화의 revenue 가 high_revenue 보다 높다면 새로운 high_revenue 로 지정
        # high_revenue 인 해당 영화의 title 을 high_movie 로 지정
        if revenue.get('revenue') >= high_revenue:
            high_revenue = revenue.get('revenue')
            high_movie = revenue.get('title')
        
    return high_movie

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
