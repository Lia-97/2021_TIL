# git command

> git 기초 명령어 정리



### 설정

#### init

- `git init`
- 폴더를 git으로 관리하기 위해 `.git` 폴더를 생성하는 명령어
- 최초에 한번만 실행하면 된다.



#### status

- `git status`
- 현재 git의 상태를 출력



#### log

- `git log`
- 현재 쌓아였는 commit history 를 출력



#### diff

- `git diff`
- 마지막 commit 과 지금 working directory 의 상태를 비교



#### remote add

- `git remote add <별명> <주소>`
- 원격저장소 주소를 등록



### 조작

#### add

- `git add <파일이름>`
  - `<파일이름>` 에 `.` 을 입력하면 전체 파일이 추가된다.
- workingdirectory에 잇는 파일을 staging  area(INDEX) 에 올림



#### commit

- `git commit -m '커밋메세지'` 
- staging area 에 올라간 파일들을 스냅샷으로 저장 



#### push

- `git push <원격저장소 이름> <올린 브랜치 이름>`
  - `git push origin master`
- commit history  를 원격 저장소에 업로드







