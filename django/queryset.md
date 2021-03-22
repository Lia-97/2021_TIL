# create 하는 3가지 방법



article = Article()

article.title = ''

article.content = ''

article.save()



article = Article(title='', content='')

article.save()



Article.objects.create(title='', content='')



# 조회(read)

Article.objects.get(pk=1)



models.py 에

```python
def __str__(self):
    return self.title
```

shell 에 title로 출력된다.



조회의 역할을 하는 쿼리셋 메서드

1. all

2. get

   찾고자하는 객체가 없을때?? doesnotexist 에러 발생

   Article.objects.get(content='withoutsave')  --> 컨텐트 내용을 지정해서 get 할 수도 있음

   겹치느 ㄴ컨텐트 내용을 get하려고 하면 multiple object error 발생

   따라서 .get은 유니크한 값 혹은 NOT NULL 특징을 가진 경우에만 사용 가능 --> pk!!!! 를 조회할 때 사용한다.

3. filter : 쿼리셋으로 리턴함

   Article.objects.filter(content='django!')

   django!가 content 인 값이 여러개 있으면 쿼리셋으로 모두 반환함.

   하나여도 쿼리셋 안에 데이터 하나 들어간 상태로 반환.



- filter lookup

  In [6]: Article.objects.filter(content__contains='!')
  Out[6]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>



# delete

save 없이 바로 가능





# admin.py

$ python manage.py createsuperuserㄴ