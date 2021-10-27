# 00. JavaScript Intro_DOM 

> 2021.10.27

**DOM(Document Object Model)**

HTML, XML 등과 같은 문서를 다루기 위한 독립적인 문서 모델 인터페이스

- 모든 문서의 노드는 'DOM Tree'라고 불리는 트리 구조의 모습을 갖는다.
- 브라우저는 DOM을 해석. Parsing -> JS로 조작
- `window`, `document`와 같은 객체들이 존재 하는데, `window`는 브라우저의 최상위 객체를 의미하며 생략 가능
- JS는 DOM을 조작하는 유일한 언어이다.

##### DOM 조작 순서

1. 선택 (Select)
2. 변경 (Manipulation)

**DOM Manipulation**

*문서 모델을 객체를 통해 조작*

> "각각의 요소를 직접 `console.log`를 통해 확인 해보세요."

1. 선택 (Selection)

   ```javascript
    //1. Selection - querySelector / querySelectorAll
   //1-1. window & document
   // console.log(window)
   // console.log(document)
   // console.log(window.document)
   
   //1-2. querySelector
   const mainHeader = document.querySelector('h1')
   const langHeader = document.querySelector('#langHeader')
   const frameHeader = document.querySelector('#frameHeader')
   // console.log(mainHeader, langHeader, frameHeader)
   
   //1-3. querySelectorAll
   const langLi = document.querySelectorAll('.lang')
   const frameworkLi = document.querySelectorAll('.framework')
   // console.log(langLi, frameworkLi)
   
   //1-4. 여러 개의 요소 -> 첫 번째로 일치하는 요소
   const selectOne= document.querySelector('.lang')
   // console.log(selectOne)
   
   //1-5. 복합 선택자
   const selectDescendant = document.querySelector('body li')
   // const selectDescendant = document.querySelectorAll('body li')
   const selectChild = document.querySelector('body > li')
   // console.log(selectDescendant) 
   // console.log(selectChild) 
   
   //1-6. getElementById, getElementByClassName 
   const selectSepcialLang = document.getElementById('specialLang')
   const selectAllLangs = document.getElementsByClassName('framework')
   const selectAllLiTags = document.getElementsByTagName('li')
   // console.log(selectSepcialLang, selectAllLangs, selectAllLiTags)
   ```

   - 단일 노드

     `document.getElementById(id)`

      id만 활용하여 선택할 수 있다. (querySelector에 비해 유연성이 떨어진다.)

     :heavy_check_mark: `document.querySelector(selector)`

     id, class, tag, 복합 선택자(자손, 자식 선택자) 등을 모두 활용하여 선택할 수 있다.​​

   - 여러 개의 요소 (유사배열)

     - HTMLCollection (live)

       `document.getElementsByTagName(tagName)`

       `document.getElementsByClassName(class)`

     - NodeList (non-live)

       :heavy_check_mark: `document.querySelectorAll(selector)`

2. 변경, 조작 (Manipulation)

   ```javascript
   //2. Manipulation
   //2-1. Creation
   const browserHeader = document.createElement('h2')
   const ul = document.createElement('ul')
   const li1 = document.createElement('li')
   const li2 = document.createElement('li')
   const li3 = document.createElement('li')
   // console.log(browserHeader, li1, li2, li3) 
   
   
   //2-2. innerText & innerHTML / append & appendChild
   browserHeader.innerText = 'Browsers'
   li1.innerText = 'IE'
   li2.innerText = '<strong>FireFox</strong>'
   li3.innerHTML = '<strong>Chrome</strong>'
   // console.log(browserHeader, li1, li2, li3)
   
   
   //2-3. append DOM 
   const body = document.querySelector('body')
   body.appendChild(browserHeader)
   body.appendChild(ul)
   
   // append와 appendChild의 차이점도 같이 확인
   ul.append(li1, li2, li3) 
   // ul.appendChild(li1, li2, li3) 
   
   
   //2-4. Delete
   // removeChild
   // ul.removeChild(li1) 
   // ul.removeChild(li2)
   
   // remove
   // ul.remove()
   // body.remove()
   
   
   //2-5. Element Styling
   li1.style.cursor = 'pointer'
   li2.style.color = 'blue'
   li3.style.background = 'red'
   
   // setAttribute
   li3.setAttribute('id', 'king')
   
   // getAttribute
   const getAttr = li1.getAttribute('style')
   const getAttr2 = li3.getAttribute('style')
   console.log(getAttr)
   console.log(getAttr2)
   ```

   - 속성 변경

     `innerText` & `innerHTML`

     `setAttribute(attribute, value)` & `getAttribute(attribute)`

   - 생성해서 DOM에 부착

     `document.createElement(tagName)`

     `appendChild` & `append`

     `removeChild` & `remove`

