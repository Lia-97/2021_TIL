import requests
from tmdb import URLMaker
from pprint import pprint


def recommendation(title):
    # 발급받은 key
    key = 'c4ee76695f8af7078e89ed5b529516ff'
    # url 이라는 클래스 인스턴스를 만든다.
    url = URLMaker(key)
    # 영화 id 값이 있다면
    if url.movie_id(title):
        # movie_id 메서드로 아이디를 찾고
        mid = url.movie_id(title)
        # 해당 아이디를 넣어서 추천 url 을 가져온다. 
        reco_url = url.get_url('movie', f'{mid}/recommendations', language='ko')
        # url 을 요청하고
        res = requests.get(reco_url)
        # 이를 딕셔너리로 만든다.
        recommend = res.json()
        # 딕셔너리에서 results 키값을 recommend_list 에 저장하고
        recommend_list = recommend.get('results')
        # recommend_list 가 비지 않았다면
        if recommend_list:
            # 반환할 빈 리스트를 만들고
            result = []
            # recommend list 를 순회해서
            for r in recommend_list:
                # 각 원소(딕셔너리)의 title 키값을 result 에 추가한다.
                result.append(r.get('title'))
            # result 를 반환한다.
            return result

        # recommend list 가 비었다면 빈 리스트를 반환한다.
        else:
            return []
    
    else:
        return None
        
    


if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    # => None
