# 02. vue_CLI & `vue_router`

> 2021.11.08

## Vue Router

Vue.js 공식 라우터

```markdown
# 프로젝트 생성 및 이동
$ vue create my-router-app
$ cd my-router-app

# Vue Router plugin 설치 (Vue CLI 환경)
$ vue add router
```

> [주의] 기존 프로젝트를 진행하고 있던 도중에 추가하면 App.vue를 덮어씀 -> 필요한 경우 백업 필수

#### Vue Router로 인한 변화

1. `App.vue` 코드
2. `router/index.js`  생성
   * 라우터에 관련된 정보 및 설정이 작성되는 곳
3. `views` 디렉토리 생성

##### router-link

* 사용자 네비게이션을 가능하게 하는 컴포넌트

* a 태그지만 우리가 알고 있는 GET 요청을 보내는 a 태그와 조금 다르게, 기본 GET 요청을 보내는 이벤트를 제거한 형태로 구성됨

##### router-view

* 주어진 라우트에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트

#### History mode

* HTML History API를 사용해서 router를 구현한 것
* 페이지를 다시 로드하지 않고 URL을 탐색할 수 있음
  * SPA의 단점 중 하나인 `"URL이 변경되지 않는다."`를 해결

| 선언적 방식              | 프로그래밍 방식     |
| ------------------------ | ------------------- |
| `<router-link to="...">` | `$router.push(...)` |

