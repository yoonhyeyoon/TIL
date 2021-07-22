# 함수(function)

> 특정한 기능(function)을 하는 코드의 묶음

:pushpin: 공식문서를 애용하자

 [파이썬 문서 : : Built-in Functions](https://docs.python.org/ko/3/library/functions.html) / [Python tutor : : 실행순서](http://pythontutor.com/visualize.html#code=num1 %3D 0 num2 %3D 1 def func1(a, b)%3A    return a %2B b     def func2(a, b)%3A    return a - b     def func3(a, b)%3A    return func1(a, 5) %2B func2(5, b)     result %3D func3(num1, num2) print(result)&cumulative=false&curInstr=10&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=[]&textReferences=false) 

* 함수를 쓰는 이유
  * 가독성
  * 재사용성
  * 유지보수

![61181742-2984fd80-a665-11e9-9d5c-c90e8c64953e](함수(function).assets/61181742-2984fd80-a665-11e9-9d5c-c90e8c64953e.png)

* 함수의 선언과 호출

  * 함수의 선언은 `def` 키워드를 활용한다.


  * `들여쓰기(4spaces)`로 함수의 body(코드 블록)를 작성한다.
      * Docstring은 함수 body 앞에 선택적으로 작성 가능


  * 함수는 `매개변수(parameter)`를 넘겨줄 수도 있다.


  * 함수는 동작후에 `return`을 통해 결과값을 전달한다.
      * 반드시 하나의 객체를 반환한다. (`return` 값이 없으면, `None`을 반환)


  * 함수는 호출은 `함수명()`으로 한다. 
      * 예) `func()` / `func(val1, val2)`

* 함수의 구조

```python
def <함수이름>(parameter1, parameter2):
    <코드 블럭>
    return value
```

## 함수의 Output

* 함수의 `return`
  * 함수는 반환되는 값이 항상 있으며, 이는 어떠한 종류(~~의 객체~~)라도 상관없다.
  * 단, **오직 한 개의 객체**만 반환된다.
  * 함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아간다.

## 함수의 Input

### 1. 매개변수(parameter) & 전달인자(argument)

> 주로 혼용해서 사용하지만 엄밀하게 따지면 둘은 다르게 구분되어 사용된다.

* 매개변수(parameter)

입력을 받아 함수 내부에서 활용할 `변수`

```python
def func(x): # x가 매개변수
      return x + 2
```

* 전달인자(argument)

실제로 전달되는 `입력값`

```python
func(2) # 2가 (전달)인자
```

함수를 호출하는 부분에서 볼 수 있다.

### 2. 함수의 인자

* 위치인자 (Positional Arguments)

기본적으로 인자는 위치에 따라 함수 내에 전달된다.

* 기본 인자 값 (Default Argument Values)

함수를 정의할 때, 기본값을 지정하여 함수를 호출할 때 인자의 값을 설정하지 않을 수 있다.

```python
def func(p1=v1):
    return p1
```

* 키워드 인자 (Keyword Arguments)

함수를 호출할 때 직접 변수의 이름으로 특정 인자를 전달할 수 있다.

```python
def greeting(age, name):
    return f'{name}은 {age}살입니다.'

greeting(name='철수', age=24)
```

### 3. 정해지지 않은 여러개의 인자처리

* 가변(임의) 인자 리스트(Arbitrary Argument Lists)

함수를 정의할 때, 가변 인자 리스트`*args`를 활용한다.

```python
def func(a, b, *args):
```

\>> `tuple` 형태로 처리

* 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

 함수를 정의할 때, 가변 키워드 인자 `**kwargs`를 활용한다.

```python
def func(**kwargs):
```

\>>`dict` 형태로 처리

### 4. 인자 순서

```python
def func(a, b=v, *args, **kwargs) 
```

## 함수와 스코프(scope)

* **전역 스코프(`global scope`)**: 코드 어디에서든 참조할 수 있는 공간
* **지역 스코프(`local scope`)**: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간


* **전역 변수(`global variable`)**: 전역 스코프에 정의된 변수
* **지역 변수(`local variable`)**: 로컬 스코프에 정의된 변수

### 1. 수명주기(lifecycle)

- **빌트인 스코프`(built-in scope)`**: 파이썬이 실행된 이후부터 영원히 유지

- **전역 스코프`(global scope)`**: 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날 때 까지 유지

- **지역(함수) 스코프`(local scope)`**: 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### 2. 이름 검색(resolution) 규칙

이름(식별자)들은 이름공간(namespace)에 저장되어 있다.

> `LEGB Rule` 
>
> 1. `L`ocal scope: 함수
> 2. `E`nclosed scope: 특정 함수의 상위 함수
> 3. `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
> 4. `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

## 재귀함수

> 재귀 함수는 함수 내부에서 자기 자신을 호출 하는 함수

* 팩토리얼 

```python
# 반복문 이용
def fact(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

# 재귀함수 이용
def factorial(n):
    if n == 1: #<- base case
        return n 
    return n * factorial(n-1)
```

반드시, `base case`가 존재

* 피보나치 수열

```python
# 반복문 이용
def fib_loop(n):
    fib_list = [0,1]
    
    for i in range(2, n+1):
        fib_list += [fib_list[i-1] + fib_list[i-2]]
    print(fib_list)

# 재귀함수 이용
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
```

재귀 호출은 `변수 사용` 을 줄여줄 수 있다.
