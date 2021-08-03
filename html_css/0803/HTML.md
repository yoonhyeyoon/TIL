# HTML(Hypertext Markup Language)

> 웹페이지를 작성하기 위한 언어
>
> 웹 컨텐츠의 의미와 구조를 정의

* 기본 구조

```html
<!DOCTYPE html> # html 문서 정의
<html>
    <head> </head>	# 해당 html 문서의 정보를 담고 있다.
    				# (제목, 문자의 인코딩, 외부 로딩 파일 지정)
    				# 브라우저에는 나타나지 않음
    <body> </body>	# 브라우저 화면에 실질적으로 나타나는 정보
</html>
```

* DOM tree : 부모, 형제 관계

![1200px-DOM-model.svg](HTML.assets/1200px-DOM-model.svg.png)

- 요소(element) : 태그와 컨텐츠로 구성

  - 태그 별로 속성이 있는데 각 태그마다 사용하는 속성은 다르다.

  - 시멘틱 태그 

    * 의미론적 요소를 담은 태그

    - 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹으로 표현 가능

  - 그룹 컨텐츠

    - `p`,`hr`, `ol`, `ul`, `li`, `pre`, `blockquote`, `div`

  - 텍스트 관련

    - `a`, `b`, `i`, `strong`, `em`, `span`, `br`, `img`

  - 테이블 관련

    - `tr`, `td`, `th`, `thead`, `tbody`, `tfoot`, `caption`

  - `form` : 서버에 처리될 데이터를 제공하는 역할

    - `input` : 다양한 타입을 가지는 입력 데이터필드
      - 공통 속성 : `name`, `placeholder`, `required`, `autofocus`
      - `type` : `text`, `radio`, `checkbox`, `date`, `password`
      - `label` 태그 : 서식 입력 요소의 캡션