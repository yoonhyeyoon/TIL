# 모듈(Module)

> 파일 단위의 코드 재사용

| 용어                      | 정의                                                         |
| ------------------------- | ------------------------------------------------------------ |
| 모듈                      | 특정 기능을 `.py` **파일 단위**로 작성한 것.                 |
| 패키지                    | 특정 기능과 관련된 여러 **모듈들의 집합**. 패키지 안에는 또다른 서브 패키지를 포함 할수도 있음. |
| 파이썬 표준 라이브러리    | 파이썬에 **기본적으로 설치된 모듈과 내장 함수**를 묶어서 파이썬 표준 라이브러리 (Python Standard Library, PSL) 라 불림. |
| 패키지 관리자(** `pip`**) | `PyPI` 에 저장된 외부 패키지들을 설치하도록 도와주는 패키지. |

## 1. 모듈(Module)

> 특정 기능을 하는 코드를 담고 있는 파일(또는 스크립트)

* 사용법

```python
import module
from module import var, function, Class
from module import *
```

* `import`
  * 모듈을 활용하기 위해서 `import`문을 통해 내장 모듈을 이름 공간으로 가져와야함

## 2. 패키지(Package)

> 점(`.`)으로 구분된 모듈 이름(`package.module`) 을 써서 모듈을 구조화하는 방법

* 사용법

```python
from package import module
from package.module import var, function, Class
```

- `__init__.py`

  > python3.3 버전부터는 `__init__.py` 파일이 없어도 패키지로 인식(PEP 420). 하지만 하위 버전 호환 및 일부 프레임워크에서의 올바른 동작을 위해 `__init__.py` 파일을 생성하는 것이 권장됨

