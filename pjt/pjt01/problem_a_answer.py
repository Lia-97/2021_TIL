import json
from pprint import pprint


def movie_info(movie):
    # 딕셔너리에서 원소 가져오기
    movie_id = movie_dict.get('id')
    title = movie_dict.get('title')
    poster_path = movie_dict.get('poster_path')
    vote_average = movie_dict.get('vote_average')
    overview = movie_dict.get('overview')
    genre_ids = movie_dict.get('genre_ids')
    
    # 빈 딕셔너리 생성
    new_movie_info = {}
    # 딕셔너리에 각 원소 대입
    new_movie_info['genre_ids'] = genre_ids
    new_movie_info['id'] = movie_id
    new_movie_info['overview'] = overview
    new_movie_info['poster_path'] = poster_path
    new_movie_info['title'] = title
    new_movie_info['vote_average'] = vote_average

    return new_movie_info



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))