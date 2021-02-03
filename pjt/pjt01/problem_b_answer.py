import json
from pprint import pprint


def movie_info(movie, genres):
    # 딕셔너리에서 원소 가져오기
    movie_id = movie.get('id')
    title = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')
    # id 에 name 을 대입
    for id in range(len(genre_ids)):
        for genre in genres:
            if genre.get('id') == genre_ids[id]:
                genre_ids[id] = genre.get('name')
    # 빈 딕셔너리 생성
    new_movie_info = {}
    # 딕셔너리에 각 원소 대입
    new_movie_info['genre_names'] = genre_ids
    new_movie_info['id'] = movie_id
    new_movie_info['overview'] = overview
    new_movie_info['poster_path'] = poster_path
    new_movie_info['title'] = title
    new_movie_info['vote_average'] = vote_average
    
    return new_movie_info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))