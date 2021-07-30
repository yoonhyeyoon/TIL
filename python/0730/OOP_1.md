# OOP I

1. 객체(Object)
2. 객체지향프로그래밍(Object Oriented Programming)
3. 클래스(Class)와 객체(Object)
4. 인스턴스 & 클래스 변수
5. 인스턴스 & 클래스간의 이름공간
6. 인스턴스 & 클래스 메서드(+ 스태틱 메서드)

# 1. 객체(Object)

> python에서 모든 것은 객체이다
>
> 모든 객체는 **타입(type), 속성(attribute), 조작법(method)**을 가진다.
>
> - **타입(type)**: 어떤 연산자(operator)와 조작(method)이 가능한가?
> - **속성(attribute)**: 어떤 상태(데이터)를 가지는가?
> - **조작법(method)**: 어떤 행위(함수)를 할 수 있는가?

| type   | instance                 |
| ------ | ------------------------ |
| `int`  | `0`, `1`, `2`            |
| `str`  | `''`, `'hello'`, `'123'` |
| `list` | `[]`, `['a', 'b']`       |
| `dict` | `{}`, `{'key': 'value'}` |

* 타입(Type)
  * 공통된 속성(attribute)과 조작법(method)을 가진 객체들의 분류
* 인스턴스(Instance)
  * 특정 타입(type)의 실제 데이터 예시(instance)
  * 파이썬에서 모든 것은 객체이고, **모든 객체는 특정 타입의 인스턴스**

```python
# a는 int타입의 인스턴스
a = 10
print(type(a) is int) #=> True
isinstance(a, int) #=> True 
```

| type      | attributes       | methods                                |
| --------- | ---------------- | -------------------------------------- |
| `complex` | `.real`, `.imag` |                                        |
| `str`     | _                | `.capitalize()`, `.join()`, `.split()` |
| `list`    | _                | `.append()`, `.reverse()`, `.sort()`   |
| `dict`    | _                | `.keys()`, `.values()`, `.items()`     |

* 속성(Attribute)

  * 객체(object)의 상태/데이터

  ```python
  <객체>.<속성>
  3+4j.real
  ```

* 메서드(Method)

  * 특정 객체에 적용할 수 있는 행위(behavior)

  ```python
  <객체>.<메서드>()
  [3, 2, 1].sort()
  ```

# 2. 객체 지향 프로그래밍(Object-Oriented Programming)

> Object가 중심(oriented)이 되는 프로그래밍
>
> > 객체 지향 프로그래밍(영어: Object-Oriented Programming, OOP)은 컴퓨터 프로그래밍의 패러다임의 하나입니다.
> >
> > 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것입니다.
> >
> > \- <wikipedia - 객체지향 프로그래밍> -

* 절차 중심 vs. Object 중심

  + 프로그래밍 패러다임 : 어떻게 프로그램을 작성할 것인가

* Object 중심의 장점

  > 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용됩니다.
  >
  > 또한 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며,
  >
  > 보다 직관적인 코드 분석을 가능하게 하는 장점을 갖고 있습니다.
  >
  > \- <wikipedia - 객체지향 프로그래밍> -

  * 코드의 **직관성**
  * 활용의 **용이성**
  * 변경의 **유연성**

# 3. 클래스(Class)와 인스턴스(Instance)

>  `class`: 객체들의 분류(class)를 정의할 때 쓰이는 키워드
>
> `instance`: 객체의 실체와 예, 인스턴스(instance)를 활용

* 클래스(Class) 생성

  * <클래스의 이름>은 `PascalCase`로 정의
  * 클래스 내부에는 데이터와 함수를 정의
  * 데이터 = **속성(attribute)**
  * 함수 = **메서드(method)**
  * 활용법

  ```python
  class <클래스이름>:
      <statement>
  class ClassName:
      statement
  ```

* 인스턴스(Instance) 생성

  * 정의된 클래스(`class`)에 속하는 객체 =  해당 클래스의 인스턴스(instance)
  * `type()` 함수를 통해 생성된 객체의 클래스를 확인
  * 활용법

  ```python
  # 인스턴스 = 클래스()
  person1 = Person()
  ```

  * `person1`은 사용자가 정의한(user-defined) `Person`이라는 데이터 타입(data type)의 인스턴스

* 메서드(Method) 정의

  ```python
  class Person:
      # 메서드(method)
      def talk(self):    # 인자로 self를 정의
          print('안녕')
      
      def eat(self, food='치킨'):
          print(f'냠냠 {food}먹고싶다..')
  ```

  * `self`

    * 인스턴스 자신(self)
    * Python에서 인스턴스 메서드 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
    * 보통 매개변수명으로 `self`를 첫번째 인자로 정의 (다른 이름도 가능하지만 추천 X)

  * 생성자(constructor) 메서드

    * 인스턴스 객체가 생성될 때 호출되는 함수
    * 반드시 `__init__` 이라는 이름으로 정의
    * 인스턴스가 생성될 때 인스턴스의 속성을 정의
    * 활용법

    ```python
    class MyClass:
        def __init__(self):
            print('생성될 때 자동으로 호출되는 메서드입니다.')
    ```

  * 소멸자(destructor) 메서드

    * 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 함수
    * 반드시 `__del__` 이라는 이름으로 정의
    * 활용법

    ```python
    def __del__(self):
        print('소멸될 때 자동으로 호출되는 메서드입니다.')
    ```

    ```python
    class Person:
        def __init__(self):
            print('응애!')
    
        def __del__(self):
            print('떠날게..')
    ```

    

* 속성(Attribute) 정의

  * `self.<속성명> = <값>` 혹은 `<인스턴스>.<속성명> = <값>`으로 설정

  ```python
  class Person:
      def __init__(self, name):
          self.name = name
  
      def talk(self):
          print(f'안녕, 나는 {self.name}')
  ```

* 매직(스페셜) 메서드

  * 더블언더스코어(`__`)가 있는 메서드는 특별한 일을 하기 위해 만들어진 메서드이기 때문에 `스페셜 메서드` 혹은 `매직 메서드`

  ```python
  '__str__(self)',
  '__len__(self)',
  '__repr__(self)',
  '__lt__(self, other)',
  '__le__(self, other)',
  '__eq__(self, other)',
  '__ne__(self, other)',
  '__gt__(self, other)',
  '__ge__(self, other)',
  ```

  * `__str__`

  ```python
  class Person:
      def __str__(self):
          return '객체 출력(print)시 보여줄 내용'
  ```

  

# 4. 인스턴스 & 클래스 변수

* 인스턴스 변수

  * 인스턴스의 속성(attribute)
  * 각 인스턴스들의 고유한 변수
  * 생성자 메서드에서 `self.변수명`로 정의
  * 인스턴스가 생성된 이후 `인스턴스.변수명`로 접근 및 할당
  * 활용법

  ```python
  class Person:
      def __init__(self, name):    # 인스턴스 메서드 (생성자) 
          self.name = name         # 인스턴스 변수
          
  print(person.name) # <인스턴스명>.<인스턴스변수>
  ```

* 클래스 변수

  * 클래스의 속성(attribute)
  * 모든 인스턴스가 공유
  * 클래스 선언 내부에서 정의
  * `클래스.변수명`으로 접근 및 할당
  * 활용법

  ```python
  class Circle:
      pi = 3.14  # 클래스 변수
      
  print(Circle.pi) # <클래스명>.<클래스변수>
  ```

# 5. 인스턴스 & 클래스간의 이름공간

* 이름공간 탐색 순서

  * 인스턴스에서 특정 속성에 접근하게 되면 **인스턴스 => 클래스** 순으로 탐색
  * 인스턴스에 해당 이름이 없으면 클래스에서 탐색

  ```python
  class Person:
      name = 'unknwon'
      
  p1 = Person()
  p1.name #=> 'unknwon'
  
  # 인스턴스의 어트리뷰트가 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장
  p1.name = 'Yoon'
  print(p1.name) #=> 'Yoon'
  ```

# 6. 메서드의 종류

* 인스턴스 메서드(instance method)

  * 인스턴스가 사용할 메서드
  * 클래스 내부에 정의되는 메서드의 기본값은 인스턴스 메서드
  * 호출시, 첫번째 인자로 인스턴스 자기자신 `self` 전달

  ```python
  class MyClass:
      def instance_method(self, arg1, arg2, ...):
          ...
  ```

* 클래스 메서드(class method)

  * 클래스가 사용할 메서드
  * `@classmethod` 데코레이터를 사용하여 정의
  * 호출시, 첫 번째 인자로 클래스 `cls` 전달

  ```python
  class MyClass:
      @classmethod
      def class_method(cls, arg1, arg2, ...):
          ...
  ```

  * **클래스 자체(`cls`)와 그 속성에 접근할 필요가 있을 때** 

* 스태틱 메서드(static method)

  * 클래스가 사용할 메서드
  * `@staticmethod` 데코레이터를 사용하여 정의
  * 호출시, 어떠한 인자도 전달되지 않음

  ```python
  class MyClass:
      @staticmethod
      def static_method(arg1, arg2, ...):
          ...
  
  # 아무런 일도 자동으로 일어나지 않음
  MyClass.static_method(.., ..)
  ```

  * **클래스와 클래스 속성에 접근할 필요가 없을 때**

## ! 유의할 점 !

* 인스턴스는 3가지 메서드 모두에 접근 가능
* but, 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계
* 인스턴스에서 클래스 메서드와 스태틱 메서드는 되도록 호출하지 않아야 한다 (가능하다 != 사용한다)



