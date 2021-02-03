import json
from pprint import pprint


def movie_info(movies, genres):
    # 평점 높은 20개의 영화를 담을 빈 리스트 준비
    movie_20 = []
    # 20개의 영화가 담겨있는 리스트 movies를 순회하면서 딕셔너리를 생성한다.
    for movie in movies:
        movie_id = movie.get('id')
        title = movie.get('title')
        poster_path = movie.get('poster_path')
        vote_average = movie.get('vote_average')
        overview = movie.get('overview')
        genre_ids = movie.get('genre_ids')
        for id in range(len(genre_ids)):
            for genre in genres:
                if genre.get('id') == genre_ids[id]:
                    genre_ids[id] = genre.get('name')
        
        # 빈 딕셔너리를 생성하고
        new_movie_info = {}

        # 딕셔너리에 정보를 넣는다.
        new_movie_info['genre_names'] = genre_ids
        new_movie_info['id'] = movie_id
        new_movie_info['overview'] = overview
        new_movie_info['poster_path'] = poster_path
        new_movie_info['title'] = title
        new_movie_info['vote_average'] = vote_average
        
        # 딕셔너리를 리스트에 추가
        movie_20.append(new_movie_info) 
    
    return movie_20
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))