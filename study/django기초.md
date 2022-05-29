# MVC, MTV 
### MVC: Model, View, Controller
### MTV
![](https://velog.velcdn.com/images/jiinkyung/post/d8b23700-a4b7-460f-8681-db74b75ff73e/image.png)


- Model: 데이터베이스와 상호작용 담당
- Template: 사용자의 인터페이스 담당
- View: 웹 서비스 내부 동작의 논리 담당
> 예를 들면..
1 . 브라우저에 ```instagram.com``` 을 요청 = ```instagram.com```에 해당하는 웹 사이트를 보여줘! 라는 **GET 요청** 
2 . 요청을 받은 해당 url이 있는지 확인 -> controller를 통해 최종적으로 사용자들의 눈에 보이는 화면이 view를 통해 보여지게 됨.
3 . 사용자가 instagram에 글을 썼다면?
=> 내가 방금 쓴 글/댓글 처리해줘! 라는 **POST 요청**
controller를 통해 db의 이 위치에 글을 저장해야겠다는 처리를 하고, model을 통해 해당 글을 저장하게됨.

----------------------------------------------------------

# 가상환경은 왜 사용하는걸까?

가상환경 이용하는 이유?
 > **독립적인** 개발환경 만들기 위해서

if... 가상환경 없이 그냥 컴퓨터에 장고를 설치한다?
개발환경의 범위는 내 컴퓨터 전체가 될 것!
장고 관련 패키지를 설치/삭제/업데이트하면 내 컴퓨터 전체에 영향 미치게 됨.

++ 특정 패키지를 삭제 및 변경했을 때, 이것이 다른 시스템에 어떤 영향을 미치는지 고려해야함.
++ 두개 이상의 프로젝트 진행시 다른 프로젝트에서 생성한 패키지의 영향을 받을 것.
ex) 각 프로젝트에셔 사용해야 하는 패키지의 버전이 다를 경우 문제 발생.

그렇기 때문에 `가상환경 사용!`
가상환경을 사용함으로써 하나의 프로젝트가 영향을 미치는 범위 줄여줌.

----------------------------------------------------------

# 개발환경 세팅하기
### 가상환경 만들고 실행하기
- 가상환경 만들기: `python -m venv 가상환경이름`
- 가상환경 실행하기: `source 가상환경이름/Scripts/activate`
- 가상환경 끄기: `deactivate`

### 장고 설치
`pip install django`
- 설치된 패키지 확인: `pip freeze`

### 프로젝트 만들기
`django-admin startproject 프로젝트명`



----------------------------------------------------------


# 장고 세부파일 살펴보기
## 1. __init__.py
- 내가 만든 프로젝트가 (폴더가) 패키지에요~ 라는 걸 알려줌. 약속된 이름임

## 2. urls.py
: url 관리
- ex) www.codelion.net이라는 이름으로 만든 사이트가 있다?
- codelion.net/login 에서는 로그인 창 보여줌.
- codelion.net/payment 에서는 결제창을 보여줌

## 3. settings.py
- 안에 있는 내용이 중요
1. BASE_DIR: 프로젝트의 기본위치 manage.py가 있는위치
2. SECRET_KEY: 암호를 만들어주는 해쉬를 만들어주는(암호화해주는) 문자열
3. DEBUG = True 어떻게 서버를 킬건지 결정 (true: 개발자용/false: 배포용) 
4. INSTALLED_APPS: application 목록
5. DATABASES: 어떤 DB들을 쓸것인지, 그 DB는 어디에 있는지
6. STATIC_URL: html, css, javascript 처럼 우리 웹사이트에서 미리 준비한 static 파일들이 어디 위치하는지 
 
## 4. manage.py 
- 어떻게 활용할지가 중요
### 1) 서버 실행
서버 실행하기: `python manage.py runserver`
서버 중지하기: `ctrl+c`

### 2) Application 만들기
`python manage.py startapp 어플리케이션명`

### 3) Database 초기화 및 변경사항 반영
`python manage.py migrate`

### 4) 관리자 계정 만들기
`python manage.py createsuperuser`
=> username, email-address, password 입력

----------------------------------------------------------

### Application 만들기
application? 장고 프로젝트를 이루는 단위
- 특정 기능을 담당하는 application 만들고 이 application들이 모여서 하나의 웹사이트가 만들어짐.
- app을 만들어주는 명령어: `python manage.py startapp 어플리케이션명`

application 만들었으면 settings.py (INSTALLED _APPS)에 **"등록"**해야함.
> settings.py의 installed_apps에 만든 앱 이름 등록.

- 만든 앱 아래 `templates 폴더` 생성 후 그 안에 `.html` 생성
- 만든 html 파일(이하 index)을 보여줘라! 하는 명령 필요 
: `views.py`에 작성
: 어떤 요청이 들어오면 index 파일 보여줘! 하는 함수 작성

```python
def home(request): 
	return render(request, 'index.html') 
# 요청이 들어왔을 때 html을 찍어서 보내주는데, index.html을 띄워보내줘(render)!!
```

=> 그렇다면, home이라는 함수는 **"언제"** 실행되는가? 
: `urls.py`에 작성해주면 됨.
    
- 서버 실행하기: `python manage.py runserver`
서버 실행하면, `http:/127.0.0.1:8000`  띄워짐.
- `views.py`의 `urlpatterns` 안에 
```python
path('home/', myapp.views.home)
# http:/127.0.0.1:8000/home으로 들어가게되면 myapp안에 view 안에 home이라는 함수를 띄워라
```
`views.py`에는 어떤 상황에서 어떻게 동작하는지의 논리 작성
`models.py`에는 데이터베이스와 상호작용하는 것과 관련한 코드 작성





