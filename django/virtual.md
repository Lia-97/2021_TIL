python -m venv venv : venv 라는 모듈을 실행할건데, venv 라는 이름의 폴더를 만들겠다.

source venv/Scripts/activate : activate 실행 (가상환경 만들어줌)

deactivate 가상환경 끄는 명령어



pip freeze > requirements.txt : pip freeze 의 데이터를 req~에 넣어줘

pip  install -r requirements.txt : req~ 에 있는거 전부다 한번에 install 해줘



dumpdata

python manage.py dumpdata [app_name].[model] #json 파일로 입력된 데이터를 만들고 싶을때

ex) python manage.py dumpdata articles.article

python manage.py dumpdata --indent 4 [app_name].[model] : json 예쁘게 보고싶을때

python manage.py dumpdata articles.article > movies.json : 결과물을 movies.json에 저장

fixtures 라는 폴더를 생성해서 movies.json 을 거기에 저장함.



해당 데이터를 받은 사람은 migrate를 한다.

python manage.py loaddata movies/movies.json

(구조는 template과 같음 fixtures>movies>movies.json)

그럼 데이터가 sqlite 파일에 저장됨