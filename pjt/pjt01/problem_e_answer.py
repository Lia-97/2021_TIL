import json


def dec_movies(movies):
    # 빈 리스트 생성
    december_list = []
    # movies의 각 id 를 파일명으로 하는 json 파일 open
    for movie in movies:
        id_num = movie.get('id')
        release_json = open('data/movies/' + str(movie.get('id')) + '.json', encoding='UTF8')
        release_json = json.load(release_json)
        # release_date 의 월이 12 인 영화 title 을 december_list 에 append
        if release_json.get("release_date")[5:7] == '12':
            december_list.append(release_json.get('title'))

    return december_list
    
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))