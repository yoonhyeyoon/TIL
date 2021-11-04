# 01_Vuejs syntax

> 2021.11.03

## 핵심

### Vue Instance

https://kr.vuejs.org/v2/guide/instance.html

1. 모든 Vue앱은 Vue  함수로 새 인스턴스를 만드는 것부터 시작
2. Vue Instance === View Component
3. View와 Model 사이의 중개자 역할을 한다.

```javascript
const app = new Vue({
  el: '#app',
  data: {
    a: 1
  },
  methods: {
    myFunc: function () {
      console.log(this) // Vue instance
    },
    yourFunc: () => {
      console.log(this) // window 
    }
  }
})
```



### Interpolation (보간법)

[https://kr.vuejs.org/v2/guide/syntax.html#%EB%B3%B4%EA%B0%84%EB%B2%95-Interpolation](https://kr.vuejs.org/v2/guide/syntax.html#보간법-Interpolation)

1. data object는 Vue Instance 내부에 들어가면 DOM과 반응형으로 연결된다.
2. 데이터 바인딩의 가장 기본 형태는 콧수염 태그(`{{ }}`)를 사용한 텍스트 보간법이다.
3. DOM에서 `{{ }}` 태그를 활용해 data의 특정 속성값을 보여줄 수 있다.
4. data가 변화하면 DOM이 다시 렌더링된다.

`v-text` `v-html`

### 1. `v-text`, `v-html`

[https://kr.vuejs.org/v2/guide/syntax.html#%EC%9B%90%EC%8B%9C-HTML](https://kr.vuejs.org/v2/guide/syntax.html#원시-HTML)

1. `v-text`는 우리가 사용하는 가장 기본 텍스트 보간법인 `{{ }}`과 같다.

2. ```
   v-html
   ```

   은 원시 HTML을 DOM에 렌더링 한다.

   - 신뢰하지 않는 외부의 입력을 받는 경우 '절대' 사용하면 안된다.

## Directive

### 2. `v-show`

[https://kr.vuejs.org/v2/guide/conditional.html](https://kr.vuejs.org/v2/guide/conditional.html)

1. `display: none;` 의 스타일을 적용하여 렌더링은 되지만 가시적으로 볼 수 없게 만든다.

2. `v-if` 디렉티브와 렌더링 & 토글 비용을 비교해서 적절한 순간에 활용할 수 있어야 한다.

   - 렌더링이 자주 되지 않는 경우는 `v-if`가 유리하고 자주 토글되는 환경에서는 `v-show`가 유리하다.

   | 디렉티브 | 렌더링 비용 | 토글 비용 |
   | -------- | ----------- | --------- |
   | v-if     | 낮다.       | 높다.     |
   | v-show   | 높다.       | 낮다.     |

### 3. `v-if`

https://kr.vuejs.org/v2/guide/conditional.html

1. 기본적인 조건문으로 사용한다.
2. `v-else-if`와 `v-else` 구문을 사용할 수 있다.
3. `v-show`와 비교하여 필요한 상황에 더 적절한 디렉티브를 사용하면 된다.
   * `v-show` - Expensive initial load, cheap toggle
   * `v-if` - cheap initial load, Expensive toggle

### 4. `v-for`

https://kr.vuejs.org/v2/guide/list.html

1. 기본적인 반복문으로 사용한다.

2. ```
   key 반드시 작성하기
   ```


### 5. `v-on`

https://kr.vuejs.org/v2/guide/events.html

1. 이벤트 리스너의 역할을 하는 디렉티브

2. `.`을 통해 여러 이벤트를 연결할 수 있다.

3. shorcut

   [https://kr.vuejs.org/v2/guide/syntax.html#v-bind-%EC%95%BD%EC%96%B4](https://kr.vuejs.org/v2/guide/syntax.html#v-bind-약어)

   - `v-on` -> `@`

### 6. `v-bind`

https://kr.vuejs.org/v2/guide/class-and-style.html

1. HTML 표준 속성 바인딩

2. class 바인딩

3. 하위 컴포넌트에게 데이터를 내려 줄 때 활용

4. shortcut

   [https://kr.vuejs.org/v2/guide/syntax.html#v-bind-%EC%95%BD%EC%96%B4](https://kr.vuejs.org/v2/guide/syntax.html#v-bind-약어)

   - `v-bind` -> `:`

### 7. `v-model`

https://kr.vuejs.org/v2/guide/forms.html

1. 폼 input과 textarea 그리고 select와 같은 HTMl Element에 양방향 데이터 바인딩을 할 수 있다.
2. `v-bind`와 `v-on`을 사용해서 구현하는 양방향 바인딩을 한번에 처리할 수 있다.
3. `.lazy` `.number` `.trim`

## lodash

* 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리