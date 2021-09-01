# 00. django_intro

> :pushpin:  2021.08.31

# Django

> Python 언어 기반 Web framework
>
> * 대규모 서비스에도 안정적이며 오랫동안 세계적인 기업들에 의해 사용됨

# Framwork Architecture

### MVC Design Pattern 

> Model - View - Controller

### MTV Pattern

> Model - Template - View

* Model
  * 응용프로그램의 데이터 구조를 정의하고 **데이터베이스**의 기록을 관리 (추가, 수정, 삭제)

* Template
  * 파일의 구조나 레이아웃을 정의
  * 실제 내용을 보여주는 데 사용
* View
  * HTTP 요청을 수신하고  HTTP응답을 반환
  * Model과 Template를 관리, 컨트롤

| MVC Pattern | MTV (Django) |
| ----------- | ------------ |
| Model       | Model        |
| View        | Template     |
| Controller  | View         |

---

# Django Intro

```
# 가상환경 생성
$ python -m venv venv

# 가상환경 활성화
$ source venv/Scripts/activate

# django 설치 
$ pip install django

# 설치 확인
$ pip list
# python -m django --version
```

```
# project 생성
$ django-admin startproject config .

# django 서버 실행
$ python manage.py runserver # 로켓 확인
```

```
# application 생성
$ python manage.py startapp <articles> # 복수형 권장
```

프로젝트에서 앱을 사용하기 위해 `config - settings - INSTALLED_APPS 리스트 - application (articles)` 등록

```python
# settings.py

INSTALLED_APPS = [
		'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

* INSTALLED_APPS의 app order

```python
INSTALLED_APPS = [
    # Local apps
    'blogs.apps.BlogsConfig',

    # Third party apps
    'haystack',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
]
```

**Internationalization**

> https://docs.djangoproject.com/en/3.1/topics/i18n/

```
# settings.py

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

### 프로젝트 구조

> Project는 Application의 집합 collection of apps)

* `__init__.py`
  * python 패키지로 다루도록 지시
* `asgi.py`
  * Asynchronous Server Gateway Interface
  * 웹 서버와 연결 및 소통하는 것을 도움
* `settings.py`
  * 설정
* `urls.py`
  * 사이트의 url과 적절한 views의 연결을 지정
* `wsgi.py`
  * Web Server Gateway Interface
* `manage.py`

### Application 구조

> 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당

* `admin.py`
* `apps.py`
* `models.py`
  * 앱에서 사용하는 Model 정의
* `test.py`
* `views.py`

---

## 코드 작성 순서

> 데이터 흐름에 맞추어 작성

![image-20210901101855027](Template, View, Routing.assets/image-20210901101855027.png)



### 1. urls.py

`urls.py -  urlpatterns - path` 등록

### 2. vies.py

`<app> - views.py`에 함수 등록 (반드시 `request`를 첫번째 매개변수로 등록해야함)

```python
def index(request):
	return render(request, 'index.html')
```

### 3. templates

`<app>/templates/.html`  *TemplatesDoseNotExist 오타, 잘못된 위치 주의*

---

# Template

### Static web page

> 정적 웹 페이지

### Dynamic web page

> 동적 웹 페이지
>
> 방문자와 상호작용 -> 페이지 내용 그때그때 다름

## Django Template

> **D**jango **T**emplate **L**anguage, **DTL**
>
> built-in template system

:pushpin:  https://docs.djangoproject.com/en/3.2/ref/templates/builtins/

```django
# Variable

{{ variable }}
```

```django
# Filters

{{ variable|filter }}
```

```django
# Tags

{{% tag %}}
```

```django
# Comments

{# #}
```

---

# Template Inheritance

> https://docs.djangoproject.com/ko/3.1/ref/templates/language/#template-inheritance

**템플릿 상속**

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춘다.

**작성**

- `base.html` 파일을 `firstapp/templates/base.html` 에 생성

- Django는 기본적으로 `<app>/templates` 를 바라보게 설정되어있다. (`APP_DIRS=True` 설정)

- 우리가 옮긴 위치는 `project폴더/templates` 이므로, Django는 현재 상태에서 해당 template 파일을 찾을 수 없다.

- 각 앱 내의 `templates` 폴더가 아닌 임의의 위치에 있는 template을 읽기 위해서는 Django에서 그 위치를 알려줘야 한다.

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'first_project' / 'templates'],
          ...,
  ]
  ```

**템플릿 상속을 위한 기본 세팅**

- 프로젝트 폴더에서 `templates` 폴더 만든 후에 `base.html` 파일 생성

  ```django
  <!-- /templates/base.html -->
  
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="UTF-8">
    <title>Hello World!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  </head>
  
  <body>
    ...
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

### `block` tag

- 하위 템플릿에서 재 지정(overriden)할 수있는 블록을 정의
- 하위 템플릿이 채울 수 있는 공간

### `extends` tag

- 이(자식) 템플릿이 부모 템플릿을 확장한다는 것을 알림

- `{% extends '' %}` 는 반드시 문서의 최상단에 위치해야 한다.

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>안녕하세요! 반갑습니다!!</h1>
  {% endblock %}
  ```

**django 설계 철학 (Template)**

> https://docs.djangoproject.com/ko/3.1/misc/design-philosophies/#template-system

- 표현과 로직(view)을 분리

  - 우리는 템플릿 시스템이 **표현**을 제어하는 도구이자 표현에 관련된 로직일 뿐이라고 본다.
  - 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 한다,

- 중복을 배제

  - 대다수의 동적 웹사이트는 공통 헤더, 푸터, 네이게이션 바 같은 사이트 공통 디자인을 갖는다.

    Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 한다.

  - 이것이 **템플릿 상속**의 기초가 되는 철학

---

# HTML Form

**Form**

- 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당하는 HTML 태그
- form은 한 페이지에서 다른 페이지로 데이터를 전달하기 위해서 사용한다.
- 핵심 속성
  - `action` —> 입력 데이터가 **전송될 URL** 지정
  - `method`—> 입력 데이터 **전달 방식** 지정

**Input**

- form 태그 중에서 가장 중요한 태그로 **사용자로부터 데이터를 입력 받기 위해** 사용
- input 태그의 속성
  - `name`
    - 중복 가능, form을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있다.
    - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name 은 key , value 는 value)로 `?key=value&key=value` 형태로 전달된다.

**HTTP method `GET`**

> https://developer.mozilla.org/ko/docs/Web/HTTP/Methods

- 서버로부터 **정보를 조회**하는 데 사용

* 서버의 데이터나 상태를 변경 시키지 않아야 하기 때문에 조회(html)를 할 때 사용
* 우리는 서버에 요청을 하면 HTML 문서 파일 한 장을 받는데 이때 사용하는 요청의 방식이 GET 방식이다.

### throw & catch 실습

- throw

  ```python
  # first_project/urls.py
  
  path('throw/', views.throw),
  ```

  ```python
  # articles/views.py 
  
  def throw(request):
      return render(request, 'throw.html')
  ```

  ```django
  <!-- articles/templates/throw.html -->
  
  <form action="/catch/" method="GET">
    <label for="message">Throw</label>
    <input type="text" id="message" name="message">
    <input type="submit">
  </form>
  ```

- catch

  ```python
  # first_project/urls.py
  
  path('catch/', views.catch),
  ```

  ```python
  # articles/views.py
  
  def catch(request):
      message = request.GET.get('message')
      context = {
          'message': message,
      }
      return render(request, 'catch.html', context)
  ```

  ```django
  <!-- articles/templates/catch.html -->
  
  <h1>너가 던져서 내가 받은건 {{ message }}야!</h1>
  <a href="/throw/">뒤로</a>
  ```

---

## URL 분리

> 각 app 폴더에 urls.py를 각각 작성함으로써 코드 유지보수에 긍정적인 구조로 변경

**두번째 app 생성 및 등록**

```python
$ python manage.py startapp accounts
INSTALLED_APPS = [
    'accounts',
    'articles',
    ...,
]
```

**프로젝트 urls.py**

```python
# config/urls.py

from django.urls import path, include


urlpatterns = [
    # accounts app에서 하는 일
    path('accounts/', include('accounts.urls')),
    # path('accounts/index/', acc_views.index),

    # articles app에서 하는 일
    path('articles/', include('articles.urls')),
    # path('<username>/<article_number>/', art_views.read),
    # path('catch/', art_views.catch),
    # path('throw/', art_views.throw),
    # path('greeting/', art_views.greeting),
    # path('articles/index/', art_views.index),
```

- 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 도와준다.
- Django가 함수 `include()`를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include 된 URLconf로 전달한다.

```python
# articles/urls.py
# accouts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    
]
```

---

## URL Name

> path() 함수의 name value를 작성해 `{% url %}` template tag로 호출

**url template tag**

- django 는 path() 함수에서 name 인수(optional) 를 정의해, `{% url %}` template tag 를 사용하여 URL 설정에 정의된 특정한 URL 경로들의 의존성을 제거할 수 있다.

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  app_name = 'articles' # URL Namespace 이름공간 생성
  urlpatterns = [
      path('<username>/<article_number>/', views.read, name='read'),
      path('catch/', views.catch, name='catch'),
      path('throw/', views.throw, name='throw'),
      path('greeting/', views.greeting, name='greeting'),
      path('index/', views.index, name='index'),
  ]
  
  # accounts/urls.py 도 같은 구조로 작성
  ```

  ```django
  <!-- throw.html -->
  ...
    <a href="{% url 'articles:index' %}">Articles Index로 이동</a>
  
    <form action = "{% url 'articles:catch' %}">
      <label> 제목을 입력하세요 :
        <input type='text' name='title'>
      </label>
      <button>전달</button>
    </form>
  ...
  ```

---

## Django Namespace

> Namespace
>
> 이름공간 또는 네임스페이스(Namespace)는 객체를 구분할 수 있는 범위를 나타내는 말로 일반적으로 하나의 이름 공간에서는 하나의 이름이 단 하나의 객체만을 가리키게 된다.

* django에서는 서로 다른 app의 같은 이름을 가진 url name은 app_name을 설정해서 구분
* templates, static 등 django는 정해진 경로 하나로 모아서 보기 때문에 중간에 폴더를 임의로 만들어 줌으로써 이름공간을 설정한다.

#### 파일트리 예시

```python
├── articles
│   ├── templates
│   │   └── articles
│   │       ├── catch.html
│   │       ├── dinner.html
│   │       ├── dtl_practice.html
│   │       ├── hello.html
│   │       ├── index.html
│   │       └── throw.html

# articles/views.py 
return render(request, 'articles/index.html')
```

