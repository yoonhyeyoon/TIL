# 05. django_rest_api

> 2021.10.25

### RESTful API

### HTTP

* 요청 (request)

![image-20211025211901386](C:\Users\HOME\AppData\Roaming\Typora\typora-user-images\image-20211025211901386.png)

* 응답 (response)

![image-20211025211917472](C:\Users\HOME\AppData\Roaming\Typora\typora-user-images\image-20211025211917472.png)

##### 기본 특성

* Stateless
* Connectless

#### URL

> Uniform Resource Locator

* 통합 자원 위치
* 네트워크 상에 자원이 어디 있는지 알려주기 위한 약속
* 과거에는 실제 자원의 위치를 나타냄 / 현재는 추상화된 의미론적인 구성
* '웹 주소', '링크' 라고 불림

#### URN

> Uniform Resource Name

* 통합 자원 이름
* URL과 달리 자원의 위치에 영향을 받지않는 유일한 이름 역할을 함

#### URI

> Uniform Resource Identifier

* 통합 자원 식별자
* 인터넷의 자원을 식별하는 유일한 주소 (정보의 자원을 표현)
* 하위개념
  * URL, URN
  * URN을 사용하는 비중이 매우 적기 때문에 일반적으로 URL은 URI와 같은 의미처럼 사용하기도 함

* Scheme (protocol)

`http://`www.example.com:80/path/to/myfile.html/?key=value#quick-start

* Host (Domain name)

http://`www.example.com`:80/path/to/myfile.html/?key=value#quick-start

* Port

http://www.example.com`:80`/path/to/myfile.html/?key=value#quick-start

* Path

http://www.example.com:80`/path/to/myfile.html`/?key=value#quick-start

* Query (Identifier)

http://www.example.com:80/path/to/myfile.html/`?key=value`#quick-start

* Fragment

http://www.example.com:80/path/to/myfile.html/?key=value`#quick-start`

### RESTful API

> Application Programming Interface

* REST 원리를 따르는 시스템
* 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
* Web API
* 응답 데이터 타입
  * HTML, XML, JSON, ...

#### REST

* API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론

#### JSON

> JavaScript Object Notation

* key-value 형태의 구조를 갖고 있음 -> 파싱 용이

##### REST의 핵심 규칙

1. `정보`는 URI로 표현
2. 자원에 대한 `행위`는 HTTP Method로 표현 (GET, POST, PUT, DELETE)

### Response

#### Serialization

* 직렬화
* Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어 준다

#### Django REST Framework (DRF)

* Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리
* DRF의 Serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 구성되고 작동함

### Single Model

### 1:N Relation

