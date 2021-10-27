# 01. javascript_event

> 2021.10.27

**Event**

*"HTML 문서 내에서 일어나는 사건(일)"*

`click`, `submit`, `load`, `keydown`, `mouseover`, `submit`, `change` ...

**addEventListener**

*"대상에 특정 이벤트가 발생하면, 할 일을 등록하자"*

```javascript
EventTarget.addEventListener(type, listener)
```

1. `EventTarget` *대상*
   - 이벤트 감지를 위한 요소
2. `addEventListener`
   - EventTarget에 이벤트를 등록할 때 사용하는 이벤트 핸들러
3. `type` *특정 이벤트*
   - 반응 할 이벤트 유형 
4. `listener` *할 일*
   - (콜백) 함수
   - 이벤트가 발생하면 실행되는 함수

## `event.preventDefault()`

> "각 태그의 고유한(== 기본으로 설정된) 이벤트가 브라우저에서 동작하지 않도록 막는 행위"

이벤트 취소

1. 해당 이벤트의 기본 동작을 확인하고
2. 기본 동작을 막아보자

```django
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>preventDefault</title>
	<style>
    body {
      height: 10000px;
    }
  </style>
</head>
<body>
  <!-- 1. checkbox -->
  <input type="checkbox" id="myCheckBox">
  <hr>

  <!-- 2. submit -->
  <form action="/articles/" id="myForm">
    <input type="text">
    <input type="submit">
  </form>
  <hr>

  <!-- 3. link -->
  <a href="https://google.com" target="_blank" id="myLink">GoToGoogle</a>
  <hr>

  <!-- 4. input -->
  <input type="text" id="myInput">
  
  <script>// 아래의 코드가 여기에 들어갑니다.</script>
</body>
</html>
```

`script` 태그는 생략

```javascript
//1. checkbox
const checkBox = document.querySelector('#myCheckBox')

checkBox.addEventListener('click', function (event) {
    // cancelable -> 이벤트가 취소 가능한지 여부를 true/false로 반환
    console.log(event)
    console.log(event.cancelable)
    event.preventDefault()
})

//2. form
const form = document.querySelector('#myForm')

form.addEventListener('submit', function (event) {
    console.log(event)
    console.log(event.cancelable)
    event.preventDefault() 
    // event.target.reset() // value 값 초기화
})

//3. link
const link = document.querySelector('#myLink')

link.addEventListener('click', function (event) {
    console.log(event)
    console.log(event.cancelable)
    event.preventDefault()
})

//4. input
const input = document.querySelector('#myInput')

input.addEventListener('keydown', function (event) {
    console.log(event)
    console.log(event.cancelable)
    event.preventDefault()
})

//5. preventDefault가 불가능한 이벤트
document.addEventListener('scroll', function (event) {
    console.log(event.cancelable) 
    event.preventDefault()
})
```

