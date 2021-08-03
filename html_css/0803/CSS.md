# CSS(Cascading Style Sheets)

> 스타일, 레이아웃 등을 통해서 문서를 표시하는 방법을 지정하는 언어

- CSS 적용 방법

  1. inline 

     * 관리하기 힘듦

     ```html
     <div style="background-color: red;"></div>
     ```

  2. 내부 참조 방식 

     * 하나의 html에서만 적용

     ```html
     <style> h1 {color: red;} </style>
     ```

  3. 외부 참조 방식 

     * css 정의를 파일 단위로 묶어서 필요한 html 문서 마다 적용이 가능 
     * 유지보수가 쉬움
     * 파일을 따로 만들어서 관리를 해야하기 때문에 css 파일을 잘 챙겨야 함

- CSS 정의 방법

  ```css
  Selector {
      propertyName: value;
  }
  ```

  #### 선택자 

  * 특정한 요소를 선택하여서 스타일링을 하기 위해 반드시 필요

  - 기초 선택자

    - 타입(요소, 태그) 선택자, 아이디 선택자, 클래스 선택자, 전체 선택자

  - 고급 선택자

    - 자손 선택자 

      * 하위의 모든 요소 (띄워쓰기로 구분)

      * 선택자1 선택자2 { 속성: 속성값 } 

        `article p { color: red; }`

    - 자식 선택자 : 바로 아래의 요소 ( > 로 구분)

      * 선택자1 > 선택자2 {속성: 속성값} 

        `div > p { color: blue; }`

    - 형제 요소 선택자 : 같은 레벨에 있는 요소 (~로 구분)

      * 선택자1 ~ 선택자2 {속성: 속성값}

         `p~section { color: yellow; }`

    - 인접 형제 요소 선택자 : 바로 붙어 있는 형제 요소 (+로 구분)

      * 선택자1 + 선택자2 {속성: 속성값} 

        `div + p { color: purple; }`

  #### **CSS 적용 우선순위**

  1. 중요도 : `!important` 로 나타냄, 디버깅이 어렵기 때문에 사용시 주의

  2. 우선 순위

     1. inline style : 태그에 직접 스타일을 적용한 것

     2. id 선택자

     3. class 선택자

     4. 속성 선택자

        - 셀렉터[속성] : 해당 속성을 가진 요소를 선택
        - 셀렉터[속성-속성값] : 해당 속성값을 가진 요소를 선택

     5. 수도 클래스 선택자

        - 셀렉터: hover : 해당 셀렉터 위에 마우스를 오버했을 때

     6. 요소(타입, 태그) 선택자

        > 범용(*)선택자, ('' , +, -, >) 결합자는 우선 순위에 영향을 미치지 않음

  3. 코드에 정의된 순서

  #### CSS 단위

  - px, %(기준 사이즈에서 배율), em(상속받은 사이즈에서 배수), rem(root 사이즈에서 배수)
  - vw(뷰포트 너비의 1%), vh(뷰포트 높이의 1%), vmin(뷰포트에서 가로세로 중에서 짧은쪽의 1%), vmax
  - Hex(#), rgb, hsl, rgba, hsla

  #### Box Model

  - `margin`: 바깥 여백
  - `border`: 테두리
  - `padding`: 안쪽 여백
  - `content`: 글이나 이미지 등의 실제 요소
  - `box-sizing`
    - content-box: default 값, 콘텐츠 영역의 크기
    - border-box: 박스 모델 테두리 기준으로 크기 조절

  #### 마진 상쇄

  - 수직 간의 형제 요소에서 주로 발생
  - margin 대신 padding을 이용해서 해결 가능

  #### CSS Display

  - `block`
    - div, ul, ol, li, p, hr, form
  - `inline`
    - span, a, img, input, label, b, em, i, strong
    - 컨텐츠의 너비 만큼 공간을 차지
    - width, height, margin-top, margin-bottom은 지정할 수 없음
  - `inline-block`
    - 컨텐츠 너비 만큼 공간을 차지
    - width, height, margin-top, margin-bottom 지정 가능
  - `none`: 공간을 없애 버림
    - visiblilty : hidden은 공간은 차지하나 화면에 표시만 안함

  #### CSS Position

  - `static` : 기본적인 배치 순서에 따름(기본 값)
  - `relative` : static 위치를 기준으로 이동
  - `absolute` : static 속성이 아닌 가장 가까운 부모 / 조상 요소를 기준으로 이동
    - 기본적인 배치 순서에서 제외됨
  - `fixed`: 부모 요소와 관계 없이 브라우저를 기준으로 위치
  - `sticky` : relative 처럼 기본 배치 순서는 가지고 있음
    - 화면 밖으로 벗어나면 fixed 처럼 위치에 고정되어 있음
    - 부모의 영역이 화면 밖으로 벗어나면 다시 일반적인 흐름을 따름