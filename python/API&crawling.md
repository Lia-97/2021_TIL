# crawling & API



#### 딕셔너리 구조 이해하기

영화정보에 대한 딕셔너리 구조를 보고, 필요한 값을 출력한다.

```python
movie = {
    'movieInfo': {
        'movieNm': '광해, 왕이 된 남자',
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [
            {
            'nationNm': '한국'
            }
        ],
        'genres': [
            {
            'genreNm': '사극'
            },
            {
            'genreNm': '드라마'
            }
        ],
        'directors': [
            {
            'peopleNm': '추창민',
            'peopleNmEn': 'CHOO Chang-min'
            }
        ],
        'actors': [
            {
            'peopleNm': '이병헌',
            'peopleNmEn': 'LEE Byung-hun',
            'cast': '광해/하선'
            },
            {
            'peopleNm': '류승룡',
            'peopleNmEn': 'RYU Seung-ryong',
            'cast': '허균'
            },
            {
            'peopleNm': '한효주',
            'peopleNmEn': 'HAN Hyo-joo',
            'cast': '중전'
            }
        ]
    }
}

# 1. 영화의 제목을 출력하시오
print(movie.get('movieInfo').get('movieNm'))

# 2. movie의 감독의 영어이름을 출력하시오
print(movie.get('movieInfo').get('directors')[0].get('peopleNmEn'))

# 3. 배우의 인원을 출력하시오
print(len(movie.get('movieInfo').get('actors')))
```





#### beatifulsoup 활용해 웹페이지 크롤링하기

네이버의 환율정보를 가져오는 코드를 작성한다.

```python
#필요한 외장함수 import
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/' # 크롤링하고자 하는 웹페이지의 주소
res = requests.get(url) # url 의 주소를 요청한다.

soup = BeautifulSoup(res.text,'html.parser')
print(soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text) # 환율값의 셀럭터
```





####  API 요청을 통해 데이터를 가져오기

json 형식을 dict 형식으로 바꾸는 연습을 할 수 있다.

*import ppprint* 의 사용법을 알게 되었다.

```python
import requests
import pprint

key = key
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'

res = requests.get(url)
# print(type(res.text)) # str -> json 이라는 것을 알 수 있음

# print(type(res.json())) # str이었던 데이터 형태가 dict로 변경됨
# pprint.pprint(res.json()) # 가독성이 좋아짐

# '광진구'의 미세먼지 농도 가져오기
pprint.pprint(res.json().get('response').get('body').get('items')[0].get('pm10Value'))
```

