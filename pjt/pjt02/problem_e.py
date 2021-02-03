import requests
from tmdb import URLMaker
from pprint import pprint


def credits(title):
    # 발급받은 key
    key = 'c4ee76695f8af7078e89ed5b529516ff'
    # url 이라는 클래스 인스턴스를 만든다.
    url = URLMaker(key)
    # movie_id 메서드로 'title' 이라는 제목을 가진 영화의 id 를 찾는다.
    mid = url.movie_id(title)
    # mid 가 있으면
    if mid:
        # 해당 영화의 credits 를 보여주는 url 을 가져온다.
        url = url.get_url(feature=f'{mid}/credits', language='ko')
        # url 에 요청을 보내고
        res = requests.get(url)
        # 딕셔너리 형태로 가져온다.
        movie_credits = res.json()
        # cast, crew, result 라는 빈 자료형을 만든다.
        cast = []
        crew = []
        result = {}
        # movie_credits 의 cast 키값을 순회하는데
        for c in movie_credits.get('cast'):
            # 해당 키값의 cast_id 라는 키값이 10보다 작으면
            if c.get('cast_id') < 10:
                # 해당 키값의 name 이라는 키값을 cast 에 추가한다.
                cast.append(c.get('name'))
        # movie_credits 의 crew 키값을 순회하는데
        for c in movie_credits.get('crew'):
            # 해당 키값의 department 라는 키값이 Directing 이면
            if c.get('department') == 'Directing':
                # 해당 키값의 name 이라는 키값을 crew 에 추가한다.
                crew.append(c.get('name'))
        # result 딕셔너리에 cast 와 crew 키를 만들어 각각 cast 와 crew 를 value 로 추가해준다.
        result['cast'] = cast
        result['crew'] = crew

        return result
    
    # mid 가 없으면 None 을 반환하다.
    else:
        return None
if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None